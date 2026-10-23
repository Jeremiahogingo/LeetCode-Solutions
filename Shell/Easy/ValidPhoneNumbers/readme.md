# 193. Valid Phone Numbers

![LeetCode](https://img.shields.io/badge/LeetCode-193-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-Bash-black?logo=gnubash)
![Topic](https://img.shields.io/badge/Topic-Regular%20Expressions-blue)

## Problem Overview

Given a text file named `file.txt` containing one phone number per line, print only the lines that match either of the two valid formats:

- `xxx-xxx-xxxx`
- `(xxx) xxx-xxxx`

Each `x` represents a digit from `0` to `9`. The output must preserve the original lines and exclude invalid entries.

**LeetCode:** [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/description/)

## Approach: Bash + Extended Regular Expressions

The solution uses `grep -E` to filter lines according to a regular expression. Extended regular expressions support grouping, alternation, and repetition, making it possible to describe both formats in a single pattern.

### Algorithm

1. Read the contents of `file.txt`.
2. Match each line against the two permitted phone number formats.
3. Use `^` and `$` to require the entire line to match.
4. Print only matching lines, preserving their original order.

## Bash Implementation

```bash
grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
```

## Regular Expression Breakdown

| Pattern | Meaning |
|---|---|
| `^` | Beginning of the line |
| `\(` | Literal opening parenthesis |
| `[0-9]{3}` | Exactly three digits |
| `\)` | Literal closing parenthesis |
| ` ` | Exactly one space |
| `\|` | Not used here; the actual alternation operator is `\|` only in basic regex, while `grep -E` uses `|` |
| `[0-9]{3}-` | Three digits followed by a hyphen |
| `[0-9]{3}-[0-9]{4}` | Three digits, a hyphen, and four digits |
| `$` | End of the line |

The grouped prefix:

```text
(\([0-9]{3}\) |[0-9]{3}-)
```

matches either `(xxx) ` or `xxx-`. The remainder:

```text
[0-9]{3}-[0-9]{4}
```

matches `xxx-xxxx`.

Together, they describe both valid formats.

## Example Walkthrough

### Input

`file.txt`

```text
987-123-4567
123 456 7890
(123) 456-7890
```

### Expected Output

```text
987-123-4567
(123) 456-7890
```

### Explanation

- `987-123-4567` matches `xxx-xxx-xxxx`, so it is printed.
- `123 456 7890` uses spaces instead of the required hyphens, so it is excluded.
- `(123) 456-7890` matches `(xxx) xxx-xxxx`, so it is printed.

## Edge Cases

| Input line | Expected behavior | Reason |
|---|---|---|
| `111-222-3333` | Include | Valid hyphen-separated format |
| `(111) 222-3333` | Include | Valid parenthesized format |
| `111 222 3333` | Exclude | Incorrect separators |
| `(111)-222-3333` | Exclude | Missing required space after `)` |
| `11-222-3333` | Exclude | First group has too few digits |
| `111-222-333` | Exclude | Last group has too few digits |
| `abc-222-3333` | Exclude | First group contains letters |
| `111-222-3333 extra` | Exclude | Extra characters after the number |
| `extra 111-222-3333` | Exclude | Extra characters before the number |
| Empty line | Exclude | Does not match either format |

The problem guarantees that lines contain no leading or trailing whitespace, so the solution does not need to trim them.

## Complexity Analysis

Let \(N\) be the total number of characters in the input file.

- **Time Complexity:** \(O(N)\), because each line is checked against a fixed-length pattern.
- **Auxiliary Space Complexity:** \(O(1)\) for the pattern and matching state, excluding implementation-specific buffering.

## Key Takeaways

- `grep -E` enables extended regular expressions.
- `[0-9]{3}` matches exactly three digits.
- `|` represents alternation in extended regular expressions.
- Escaped parentheses `\(` and `\)` match literal parentheses.
- Anchors `^` and `$` prevent partial matches.
- A concise regular expression can validate multiple fixed formats in one command.

## Related Problems

- [195. Tenth Line](https://leetcode.com/problems/tenth-line/)
- [194. Transpose File](https://leetcode.com/problems/transpose-file/)
- [192. Word Frequency](https://leetcode.com/problems/word-frequency/)

## References

- [LeetCode #193 — Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/description/)
- [GNU grep Manual](https://www.gnu.org/software/grep/manual/grep.html)

---

*Part of my [LeetCode Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions) repository.*