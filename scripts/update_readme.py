#!/usr/bin/env python3
"""Update the repository README from solution files and the optional problem catalog.

Supported repository layout (case-insensitive language-folder names):
    Easy/<Language>/<solution files>
    Medium/<Language>/<solution files>
    Hard/<Language>/<solution files>
    Shell/<Difficulty>/<solution files>
    Databases/<Difficulty>/<solution files>

A file is identified from one of these sources, in order:
1. Metadata comments in the first 60 lines (recommended for ambiguous filenames).
2. A numbered filename/folder, e.g. ``125_Valid_Palindrome.py``.
3. A descriptive filename, e.g. ``ValidPalindrome.py`` or
   ``letter-combinations-of-a-phone-number.js``.

When a descriptive filename has no problem number, the README displays an em dash
in the number column, but still counts the problem and links to its LeetCode slug.
The data/problems.json catalog can supply IDs/topics for existing solutions.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
README_CANDIDATES = ("README.md", "Readme.md", "readme.md")
README_PATH = next(
    (ROOT / filename for filename in README_CANDIDATES if (ROOT / filename).is_file()),
    ROOT / "README.md",
)
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
DIFFICULTY_LOOKUP = {name.casefold(): name for name in VALID_DIFFICULTIES}
LANGUAGE_FOLDER_NAMES = {
    "golang", "go", "java", "javascript", "python", "c++", "cpp", "c",
    "typescript", "sql", "bash", "shell", "php", "rust", "c#", "ruby",
    "kotlin", "swift", "scala",
}
GENERIC_STEMS = {
    "solution", "main", "index", "app", "test", "tests", "answer",
    "program", "submission", "runner", "leetcode_solution", "leetcode-solution",
}
TOPIC_FOLDER_NAMES = {
    "array", "arrays", "string", "strings", "hashmap", "hashmaps", "hash_map",
    "linkedlist", "linkedlists", "linked_list", "math", "tree", "trees", "graph",
    "graphs", "dynamicprogramming", "dynamic_programming", "dp", "greedy",
    "backtracking", "stack", "stacks", "queue", "queues", "binarysearch",
    "binary_search", "heap", "heaps", "trie", "tries", "twopointers", "two_pointers",
}
MARKERS = {
    "stats": ("<!-- AUTO_STATS:START -->", "<!-- AUTO_STATS:END -->"),
    "problems": ("<!-- AUTO_PROBLEMS:START -->", "<!-- AUTO_PROBLEMS:END -->"),
    "languages": ("<!-- AUTO_LANGUAGES:START -->", "<!-- AUTO_LANGUAGES:END -->"),
}


def slugify(title: str) -> str:
    value = title.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def normalized_comment_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^(?://|#|--|\*+|/\*+|<!--|-->)+\s*", "", line)
    line = re.sub(r"\s*\*/\s*$", "", line)
    return line.strip()


def title_from_raw(raw: str) -> str:
    """Convert a descriptive filename/folder name to a readable problem title."""
    value = raw.strip()
    value = re.sub(r"^(?:leetcode|problem)[\s_.-]*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[\s_.-]*(?:solution|answer)$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    value = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", value)
    value = re.sub(r"[_\-.]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip(" -_\t")
    if not value or value.casefold() in GENERIC_STEMS:
        return ""
    return value.title()


def infer_path_metadata(path: Path) -> dict[str, Any]:
    """Infer metadata from difficulty segments, numbered path segments, or a title filename."""
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path

    difficulty = ""
    for part in rel.parts:
        if part.casefold() in DIFFICULTY_LOOKUP:
            difficulty = DIFFICULTY_LOOKUP[part.casefold()]
            break

    # Prefer numbered names in any parent folder or the filename.
    candidates = list(rel.parts[:-1]) + [path.stem]
    number_pattern = re.compile(
        r"^(?:leetcode[\s_-]*)?#?\s*(\d{1,5})\s*[._\-\s]+\s*(.+?)\s*$",
        re.IGNORECASE,
    )
    for candidate in reversed(candidates):
        match = number_pattern.match(candidate.strip())
        if not match:
            continue
        title = title_from_raw(match.group(2))
        if title:
            return {"id": int(match.group(1)), "title": title, "difficulty": difficulty}

    # A descriptive filename is enough to track a problem even when it has no ID.
    # This also handles title-only filenames in Easy/python, Medium/Java, etc.
    title = title_from_raw(path.stem)
    if not title:
        # Handle per-problem folders that contain generically named solution files,
        # but do not accidentally interpret language/difficulty/topic folders as titles.
        for candidate in reversed(rel.parts[:-1]):
            normalized = re.sub(r"[^a-z0-9]+", "", candidate.casefold())
            if (
                candidate.casefold() in DIFFICULTY_LOOKUP
                or candidate.casefold() in LANGUAGE_FOLDER_NAMES
                or normalized in TOPIC_FOLDER_NAMES
                or candidate.casefold() in {name.casefold() for name in SOURCE_ROOTS}
            ):
                continue
            title = title_from_raw(candidate)
            if title:
                break

    result: dict[str, Any] = {"difficulty": difficulty}
    if title:
        result["title"] = title
    return result


def parse_solution_metadata(path: Path, content: str) -> dict[str, Any] | None:
    """Parse metadata comments, falling back to information in the file path."""
    lines = [normalized_comment_line(line) for line in content.splitlines()[:60]]
    problem_id: int | None = None
    title = ""
    difficulty = ""
    topics: list[str] = []
    url = ""

    problem_patterns = (
        re.compile(
            r"^(?:problem\s*:\s*)?(?:leetcode\s*)?#?\s*(\d{1,5})\s*[-:|.–—.]\s*(.*?)\s*$",
            re.IGNORECASE,
        ),
        re.compile(r"^problem\s*:\s*(?:leetcode\s*)?#?\s*(\d{1,5})\s*$", re.IGNORECASE),
    )

    for line in lines:
        for pattern in problem_patterns:
            match = pattern.match(line)
            if match:
                problem_id = int(match.group(1))
                if len(match.groups()) > 1 and match.group(2).strip():
                    title = match.group(2).strip().strip("-:|. ")
                break

        label = re.match(
            r"^(problem|title|difficulty|topics?|url|problem url)\s*:\s*(.*?)\s*$",
            line,
            re.IGNORECASE,
        )
        if not label:
            continue
        name, value = label.group(1).casefold(), label.group(2).strip()
        if name == "problem" and value:
            # A plain "Problem: Valid Palindrome" is valid title metadata too.
            found = re.match(
                r"^(?:leetcode\s*)?#?\s*(\d{1,5})\s*[-:|.–—.]\s*(.+?)\s*$",
                value,
                re.IGNORECASE,
            )
            if found:
                problem_id = int(found.group(1))
                title = found.group(2).strip()
            elif not title and not re.fullmatch(r"(?:leetcode\s*)?#?\s*\d{1,5}", value, re.I):
                title = value
        elif name == "title" and value:
            title = value
        elif name == "difficulty" and value.casefold() in DIFFICULTY_LOOKUP:
            difficulty = DIFFICULTY_LOOKUP[value.casefold()]
        elif name in {"topic", "topics"} and value:
            topics = [part.strip() for part in re.split(r"[,;]", value) if part.strip()]
        elif name in {"url", "problem url"} and value.startswith("http"):
            url = value

    inferred = infer_path_metadata(path)
    if problem_id is None:
        problem_id = inferred.get("id")
    if not title:
        title = inferred.get("title", "")
    if not difficulty:
        difficulty = inferred.get("difficulty", "")

    if not title:
        return None
    title = title_from_raw(title) or title.strip()
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


def load_seed_catalog() -> dict[str, dict[str, Any]]:
    if not CATALOG_PATH.exists():
        return {}
    try:
        raw = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"Could not read {CATALOG_PATH}: {exc}") from exc
    if not isinstance(raw, list):
        raise RuntimeError("data/problems.json must contain a JSON array of problem objects.")

    problems: dict[str, dict[str, Any]] = {}
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
        problems[str(problem_id)] = {
            "id": problem_id,
            "title": title,
            "difficulty": difficulty,
            "topics": list(dict.fromkeys(str(x).strip() for x in topics if str(x).strip())),
            "url": url,
            "languages": list(dict.fromkeys(str(x).strip() for x in languages if str(x).strip())),
        }
    return problems


def matching_key(problems: dict[str, dict[str, Any]], meta: dict[str, Any]) -> str | None:
    """Find an existing entry by ID first, then by normalized title."""
    problem_id = meta.get("id")
    if problem_id is not None and str(problem_id) in problems:
        return str(problem_id)
    target_slug = slugify(str(meta.get("title", "")))
    if target_slug:
        for key, problem in problems.items():
            if slugify(str(problem.get("title", ""))) != target_slug:
                continue
            # An unnumbered file can inherit the ID from the catalog. Conversely,
            # do not merge two different numbered problems solely because titles match.
            existing_id = problem.get("id")
            if problem_id is None or existing_id is None or existing_id == problem_id:
                return key
    return None


def scan_solution_files(problems: dict[str, dict[str, Any]]) -> tuple[int, list[str]]:
    """Scan all language subfolders and return source-file count plus skipped paths."""
    skipped: list[str] = []
    discovered_files = 0

    for root_name in SOURCE_ROOTS:
        source_root = ROOT / root_name
        if not source_root.is_dir():
            continue

        for path in sorted(source_root.rglob("*")):
            if not path.is_file() or path.suffix.casefold() not in SOURCE_SUFFIXES:
                continue
            if any(
                part.startswith(".") or part.casefold() in {"__pycache__", "node_modules", "vendor"}
                for part in path.relative_to(ROOT).parts
            ):
                continue
            discovered_files += 1
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            meta = parse_solution_metadata(path, content)
            if not meta:
                skipped.append(path.relative_to(ROOT).as_posix())
                continue

            language = SOURCE_SUFFIXES[path.suffix.casefold()]
            key = matching_key(problems, meta)
            if key is None:
                key = str(meta["id"]) if meta.get("id") is not None else f"title:{slugify(meta['title'])}"
                problems[key] = {
                    "id": meta.get("id"),
                    "title": meta["title"],
                    "difficulty": meta.get("difficulty", ""),
                    "topics": [],
                    "url": meta.get("url", ""),
                    "languages": [],
                }
            else:
                # If a title-only entry is later found with a numbered filename,
                # promote it to its canonical LeetCode ID without double-counting it.
                if meta.get("id") is not None and problems[key].get("id") is None:
                    old_key = key
                    key = str(meta["id"])
                    entry = problems.pop(old_key)
                    entry["id"] = meta["id"]
                    problems[key] = entry

            current = problems[key]
            if meta.get("title") and (not current.get("title") or current.get("id") is None):
                current["title"] = meta["title"]
            if meta.get("difficulty"):
                current["difficulty"] = meta["difficulty"]
            if meta.get("topics"):
                current["topics"] = list(dict.fromkeys(current.get("topics", []) + meta["topics"]))
            if meta.get("url"):
                current["url"] = meta["url"]
            current["languages"] = list(dict.fromkeys(current.get("languages", []) + [language]))

    return discovered_files, skipped


def validate_problems(problems: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for problem in problems.values():
        if problem.get("difficulty") not in VALID_DIFFICULTIES or not problem.get("title"):
            continue
        normalized = dict(problem)
        normalized["topics"] = problem.get("topics") or ["—"]
        normalized["languages"] = sorted(set(problem.get("languages", [])), key=str.casefold)
        normalized["url"] = problem.get("url") or f"https://leetcode.com/problems/{slugify(problem['title'])}/"
        rows.append(normalized)
    return sorted(rows, key=lambda item: (item.get("id") is None, item.get("id") or 0, item["title"].casefold()))


def build_stats(rows: list[dict[str, Any]], discovered_files: int) -> str:
    difficulty_counts = Counter(row["difficulty"] for row in rows)
    implementation_pairs = {(row["id"] if row.get("id") is not None else slugify(row["title"]), language)
                            for row in rows for language in row["languages"]}
    return "\n".join([
        "| Difficulty | Problems |",
        "|---|---:|",
        f"| 🟢 Easy | {difficulty_counts['Easy']} |",
        f"| 🟡 Medium | {difficulty_counts['Medium']} |",
        f"| 🔴 Hard | {difficulty_counts['Hard']} |",
        f"| **Total unique problems** | **{len(rows)}** |",
        f"| **Problem-language implementations** | **{len(implementation_pairs)}** |",
        f"| **Solution source files scanned** | **{discovered_files}** |",
    ])


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
        problem_number = row.get("id") if row.get("id") is not None else "—"
        output.append(
            f"| {problem_number} | [{title}]({row['url']}) | {emoji} {row['difficulty']} | {topics} | {languages} |"
        )
    if not rows:
        output.append("| — | No problems detected yet | — | Add source files or a metadata header | — |")
    return "\n".join(output)


def build_language_table(rows: list[dict[str, Any]]) -> str:
    pairs = {(row["id"] if row.get("id") is not None else slugify(row["title"]), language)
             for row in rows for language in row["languages"]}
    counts = Counter(language for _, language in pairs)
    output = ["| Language | Tracked problem-language pairs |", "|---|---:|"]
    for language, count in sorted(counts.items(), key=lambda item: (-item[1], item[0].casefold())):
        output.append(f"| {language} | {count} |")
    if not counts:
        output.append("| — | 0 |")
    return "\n".join(output)


def replace_marked_section(content: str, section: str, replacement: str) -> str:
    start_marker, end_marker = MARKERS[section]
    if content.count(start_marker) != 1 or content.count(end_marker) != 1:
        raise RuntimeError(
            f"README must contain exactly one {start_marker} and one {end_marker} marker."
        )
    start = content.index(start_marker) + len(start_marker)
    end = content.index(end_marker)
    if end < start:
        raise RuntimeError(f"README markers are out of order for section: {section}")
    return content[:start] + "\n" + replacement.rstrip() + "\n" + content[end:]


def main() -> int:
    if not README_PATH.is_file():
        print(f"README not found at {README_PATH}", file=sys.stderr)
        return 1

    problems = load_seed_catalog()
    discovered_files, skipped = scan_solution_files(problems)
    rows = validate_problems(problems)

    current = README_PATH.read_text(encoding="utf-8")
    updated = current
    updated = replace_marked_section(updated, "stats", build_stats(rows, discovered_files))
    updated = replace_marked_section(updated, "problems", build_problem_table(rows))
    updated = replace_marked_section(updated, "languages", build_language_table(rows))

    if updated != current:
        README_PATH.write_text(updated, encoding="utf-8", newline="\n")
        print(f"Updated {README_PATH.name}.")
    else:
        print(f"{README_PATH.name} is already up to date.")

    implementations = len({
        (row.get("id") if row.get("id") is not None else slugify(row["title"]), language)
        for row in rows for language in row["languages"]
    })
    print(
        f"Tracked {len(rows)} unique problems, {implementations} problem-language pairs, "
        f"and scanned {discovered_files} solution source files."
    )
    if skipped:
        print(
            f"Warning: {len(skipped)} source file(s) could not be identified by title or ID. "
            "Rename them descriptively or add metadata comments at the top of each file.",
            file=sys.stderr,
        )
        for item in skipped[:15]:
            print(f"  - {item}", file=sys.stderr)
        if len(skipped) > 15:
            print(f"  ... and {len(skipped) - 15} more", file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
