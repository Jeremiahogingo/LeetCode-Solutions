#!/usr/bin/env python3
"""Generate LeetCode README tables from a small catalog and solution metadata.

A solution file can be discovered automatically when its first 60 lines include:
    Problem: LeetCode 125 - Valid Palindrome
    Difficulty: Easy
    Topics: Two Pointers, String

The Problem line also accepts forms such as "LeetCode #125: Valid Palindrome".
Alternatively, name a file/folder like "125_Valid_Palindrome.py" and put it
under Easy/, Medium/, or Hard/. The data/problems.json file seeds/backs up entries
for existing solutions that do not yet have standardized metadata headers.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
CATALOG_PATH = ROOT / "data" / "problems.json"

SOURCE_ROOTS = ("Easy", "Medium", "Hard", "Shell", "Databases")
SOURCE_SUFFIXES = {
    ".py": "Python",
    ".java": "Java",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".mjs": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".c": "C",
    ".go": "Go",
    ".sql": "SQL",
    ".sh": "Bash",
    ".bash": "Bash",
    ".php": "PHP",
    ".rs": "Rust",
    ".cs": "C#",
    ".rb": "Ruby",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".scala": "Scala",
}
DIFFICULTY_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}

MARKERS = {
    "stats": ("<!-- AUTO_STATS:START -->", "<!-- AUTO_STATS:END -->"),
    "problems": ("<!-- AUTO_PROBLEMS:START -->", "<!-- AUTO_PROBLEMS:END -->"),
    "languages": ("<!-- AUTO_LANGUAGES:START -->", "<!-- AUTO_LANGUAGES:END -->"),
}


def slugify(title: str) -> str:
    """Create a LeetCode-style slug when the URL is not supplied."""
    value = title.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def normalized_comment_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^(?://|#|--|\*+|/\*+|<!--|-->)+\s*", "", line)
    line = re.sub(r"\s*\*/\s*$", "", line)
    return line.strip()


def infer_path_metadata(path: Path) -> dict[str, Any]:
    """Infer ID/title/difficulty from a numbered path if it follows the convention."""
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path

    difficulty = next(
        (part.title() for part in rel.parts if part.lower() in VALID_DIFFICULTIES),
        "",
    )

    candidates = list(rel.parts[:-1]) + [path.stem]
    for candidate in reversed(candidates):
        match = re.match(
            r"^(?:leetcode[-_ ]*)?(\d{1,5})[._ -]+(.+?)\s*$",
            candidate,
            flags=re.IGNORECASE,
        )
        if not match:
            continue
        problem_id = int(match.group(1))
        raw_title = match.group(2).replace("_", " ").replace("-", " ").replace(".", " ")
        raw_title = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", raw_title)
        title = re.sub(r"\s+", " ", raw_title).strip().title()
        if title:
            return {"id": problem_id, "title": title, "difficulty": difficulty}
    return {"difficulty": difficulty}


def parse_solution_metadata(path: Path, text: str) -> dict[str, Any] | None:
    """Parse metadata comments from a source file or infer it from a numbered path."""
    lines = [normalized_comment_line(line) for line in text.splitlines()[:60]]
    problem_id: int | None = None
    title = ""
    difficulty = ""
    topics: list[str] = []
    url = ""

    # Supports: Problem: LeetCode 125 - Title; LeetCode #125: Title; Problem: #125 - Title.
    problem_patterns = (
        re.compile(
            r"^(?:problem\s*:\s*)?(?:leetcode\s*)?#?\s*(\d{1,5})\s*[-:|.–—]\s*(.*?)\s*$",
            re.IGNORECASE,
        ),
        re.compile(
            r"^problem\s*:\s*(?:leetcode\s*)?#?\s*(\d{1,5})\s*$",
            re.IGNORECASE,
        ),
    )

    for line in lines:
        for pattern in problem_patterns:
            match = pattern.match(line)
            if match:
                problem_id = int(match.group(1))
                if len(match.groups()) > 1 and match.group(2).strip():
                    title = match.group(2).strip().strip("-:|. ")
                break

        label_match = re.match(r"^(title|difficulty|topics?|url|problem url)\s*:\s*(.*?)\s*$", line, re.I)
        if label_match:
            label = label_match.group(1).lower()
            value = label_match.group(2).strip()
            if label == "title" and value:
                title = value
            elif label == "difficulty" and value.title() in VALID_DIFFICULTIES:
                difficulty = value.title()
            elif label in ("topic", "topics") and value:
                topics = [item.strip() for item in re.split(r"[,;]", value) if item.strip()]
            elif label in ("url", "problem url") and value.startswith("http"):
                url = value

    inferred = infer_path_metadata(path)
    if problem_id is None:
        problem_id = inferred.get("id")
    if not title:
        title = inferred.get("title", "")
    if not difficulty:
        difficulty = inferred.get("difficulty", "")

    if problem_id is None or not title:
        return None

    if difficulty not in VALID_DIFFICULTIES:
        difficulty = ""

    if not url:
        url = f"https://leetcode.com/problems/{slugify(title)}/"

    return {
        "id": problem_id,
        "title": title,
        "difficulty": difficulty,
        "topics": topics,
        "url": url,
        "languages": [],
    }


def load_seed_catalog() -> dict[int, dict[str, Any]]:
    if not CATALOG_PATH.exists():
        return {}
    try:
        raw = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"Could not read {CATALOG_PATH}: {exc}") from exc
    if not isinstance(raw, list):
        raise RuntimeError("data/problems.json must contain a JSON array of problem objects.")

    results: dict[int, dict[str, Any]] = {}
    for item in raw:
        if not isinstance(item, dict):
            continue
        try:
            problem_id = int(item["id"])
            title = str(item["title"]).strip()
        except (KeyError, ValueError, TypeError):
            continue
        if not title:
            continue
        difficulty = str(item.get("difficulty", "")).title()
        if difficulty not in VALID_DIFFICULTIES:
            difficulty = ""
        topics = item.get("topics", [])
        if isinstance(topics, str):
            topics = [part.strip() for part in re.split(r"[,;]", topics) if part.strip()]
        languages = item.get("languages", [])
        if isinstance(languages, str):
            languages = [languages]
        url = str(item.get("url", "")).strip() or f"https://leetcode.com/problems/{slugify(title)}/"
        results[problem_id] = {
            "id": problem_id,
            "title": title,
            "difficulty": difficulty,
            "topics": list(dict.fromkeys(str(x).strip() for x in topics if str(x).strip())),
            "url": url,
            "languages": list(dict.fromkeys(str(x).strip() for x in languages if str(x).strip())),
        }
    return results


def scan_solution_files(problems: dict[int, dict[str, Any]]) -> None:
    skipped: list[str] = []
    for root_name in SOURCE_ROOTS:
        source_root = ROOT / root_name
        if not source_root.exists():
            continue
        for path in sorted(source_root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
                continue
            if any(part.startswith(".") or part in {"__pycache__", "node_modules", "vendor"} for part in path.parts):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            meta = parse_solution_metadata(path, text)
            if not meta:
                skipped.append(path.relative_to(ROOT).as_posix())
                continue

            language = SOURCE_SUFFIXES[path.suffix.lower()]
            problem_id = meta["id"]
            if problem_id not in problems:
                problems[problem_id] = {
                    "id": problem_id,
                    "title": meta["title"],
                    "difficulty": meta.get("difficulty", ""),
                    "topics": meta.get("topics", []),
                    "url": meta.get("url", ""),
                    "languages": [],
                }
            existing = problems[problem_id]
            # Source-file metadata updates a seed's details only when that metadata is present.
            if meta.get("title"):
                existing["title"] = meta["title"]
            if meta.get("difficulty"):
                existing["difficulty"] = meta["difficulty"]
            if meta.get("topics"):
                existing["topics"] = list(dict.fromkeys(existing.get("topics", []) + meta["topics"]))
            if meta.get("url"):
                existing["url"] = meta["url"]
            existing["languages"] = list(dict.fromkeys(existing.get("languages", []) + [language]))

    if skipped:
        print(
            f"Warning: skipped {len(skipped)} source file(s) without a problem ID/title. "
            "Add a metadata header or use a numbered path such as 125_Valid_Palindrome.py.",
            file=sys.stderr,
        )
        for item in skipped[:10]:
            print(f"  - {item}", file=sys.stderr)
        if len(skipped) > 10:
            print(f"  ... and {len(skipped) - 10} more", file=sys.stderr)


def validate_problems(problems: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for problem in problems.values():
        if problem.get("difficulty") not in VALID_DIFFICULTIES:
            # An older source without a difficulty can use the matching top-level directory.
            continue
        problem["topics"] = problem.get("topics") or ["—"]
        problem["languages"] = sorted(set(problem.get("languages", [])), key=str.casefold)
        problem["url"] = problem.get("url") or f"https://leetcode.com/problems/{slugify(problem['title'])}/"
        result.append(problem)
    return sorted(result, key=lambda p: (int(p["id"]), p["title"].casefold()))


def build_stats(rows: list[dict[str, Any]]) -> str:
    difficulty_counts = Counter(row["difficulty"] for row in rows)
    implementation_pairs = {(row["id"], language) for row in rows for language in row["languages"]}
    total_implementations = len(implementation_pairs)
    language_counts = Counter(language for _, language in implementation_pairs)
    return "\n".join(
        [
            "| Difficulty | Problems |",
            "|---|---:|",
            f"| 🟢 Easy | {difficulty_counts['Easy']} |",
            f"| 🟡 Medium | {difficulty_counts['Medium']} |",
            f"| 🔴 Hard | {difficulty_counts['Hard']} |",
            f"| **Total unique problems** | **{len(rows)}** |",
            f"| **Problem-language implementations** | **{total_implementations}** |",
        ]
    )


def build_problem_table(rows: list[dict[str, Any]]) -> str:
    output = [
        "| # | Problem | Difficulty | Topics | Language(s) |",
        "|---:|---|---|---|---|",
    ]
    for row in rows:
        emoji = DIFFICULTY_EMOJI[row["difficulty"]]
        topics = ", ".join(row["topics"])
        languages = ", ".join(row["languages"]) if row["languages"] else "—"
        title = row["title"].replace("[", "\\[").replace("]", "\\]")
        output.append(
            f"| {row['id']} | [{title}]({row['url']}) | {emoji} {row['difficulty']} | {topics} | {languages} |"
        )
    if len(rows) == 0:
        output.append("| — | No problems detected yet | — | Add solution metadata | — |")
    return "\n".join(output)


def build_language_table(rows: list[dict[str, Any]]) -> str:
    pairs = {(row["id"], language) for row in rows for language in row["languages"]}
    counts = Counter(language for _, language in pairs)
    output = ["| Language | Tracked implementations |", "|---|---:|"]
    for language, count in sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold())):
        output.append(f"| {language} | {count} |")
    if not counts:
        output.append("| — | 0 |")
    return "\n".join(output)


def replace_marked_section(content: str, section: str, replacement: str) -> str:
    start_marker, end_marker = MARKERS[section]
    if content.count(start_marker) != 1 or content.count(end_marker) != 1:
        raise RuntimeError(
            f"README.md must contain exactly one {start_marker} and one {end_marker} marker."
        )
    start = content.index(start_marker) + len(start_marker)
    end = content.index(end_marker)
    if end < start:
        raise RuntimeError(f"README markers are out of order for section: {section}")
    return content[:start] + "\n" + replacement.rstrip() + "\n" + content[end:]


def main() -> int:
    if not README_PATH.exists():
        print(f"README.md not found at {README_PATH}", file=sys.stderr)
        return 1

    problems = load_seed_catalog()
    scan_solution_files(problems)
    rows = validate_problems(problems)

    readme = README_PATH.read_text(encoding="utf-8")
    readme = replace_marked_section(readme, "stats", build_stats(rows))
    readme = replace_marked_section(readme, "problems", build_problem_table(rows))
    readme = replace_marked_section(readme, "languages", build_language_table(rows))

    current = README_PATH.read_text(encoding="utf-8")
    if readme == current:
        print(f"README is already up to date ({len(rows)} tracked problems).")
        return 0

    README_PATH.write_text(readme, encoding="utf-8", newline="\n")
    print(
        f"Updated README.md: {len(rows)} unique problems, "
        f"{len({(row['id'], lang) for row in rows for lang in row['languages']})} problem-language implementations."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
