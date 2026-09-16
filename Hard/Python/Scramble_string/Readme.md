# 🔀 Scramble String

[![LeetCode](https://img.shields.io/badge/LeetCode-87-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/scramble-string/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)](https://leetcode.com/problems/scramble-string/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square\&logo=python)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Memoized%20DFS-purple?style=flat-square)](https://leetcode.com/problems/scramble-string/)

## 📌 Overview

Given two strings `s1` and `s2` of the same length, determine whether `s2` can be formed by recursively splitting and optionally swapping parts of `s1`.

For example:

```text
s1 = "great"
s2 = "rgeat"

Output: true
```

Because:

```text
great
→ gr | eat
→ rg | eat
→ rgeat
```

---

## 💡 Approach

Use **memoized DFS** to compare substrings.

Define:

```text
dfs(i, j, length)
```

as whether:

```text
s1[i : i + length]
```

can be transformed into:

```text
s2[j : j + length]
```

For every split, check two possibilities:

```text
1. No swap
s1: [A | B]
s2: [A | B]

2. Swap
s1: [A | B]
s2: [B | A]
```

Before splitting, compare character frequencies. If the substrings contain different characters, they cannot be scrambles.

Memoization stores previously solved states.

---

## 🧠 Algorithm

1. Start with the complete strings.
2. Return `True` if the current substrings are identical.
3. Return `False` if their character frequencies differ.
4. Try every possible split.
5. Check both swapped and non-swapped arrangements.
6. Cache each `(i, j, length)` state.
7. Return the result for the original strings.

---

## 💻 Implementation

```python
from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        @cache
        def dfs(i: int, j: int, length: int) -> bool:
            if s1[i:i + length] == s2[j:j + length]:
                return True

            if sorted(s1[i:i + length]) != sorted(s2[j:j + length]):
                return False

            for split in range(1, length):

                # No swap
                if (
                    dfs(i, j, split)
                    and dfs(
                        i + split,
                        j + split,
                        length - split
                    )
                ):
                    return True

                # Swap
                if (
                    dfs(
                        i,
                        j + length - split,
                        split
                    )
                    and dfs(
                        i + split,
                        j,
                        length - split
                    )
                ):
                    return True

            return False

        return dfs(0, 0, n)
```

---

## 🔍 Example

For:

```text
s1 = "great"
s2 = "rgeat"
```

Split `s1` as:

```text
gr | eat
```

Swap the first part:

```text
rg | eat
```

Both resulting parts can be matched recursively, so the answer is:

```text
True
```

---

## ⏱️ Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | `O(n⁴)`    |
| Space  | `O(n³)`    |

There are `O(n³)` possible `(i, j, length)` states, with up to `O(n)` split positions considered per state.

---

## 🎯 Key Takeaways

* **Memoization** eliminates repeated recursive states.
* **Character-frequency pruning** rejects impossible matches early.
* Every split has two possibilities: **swap** or **no swap**.
* The problem is a combination of **DFS, recursion, and dynamic programming**.

### Key Pattern

```text
Recursive State
      ↓
Try Every Split
      ↓
Swap / No Swap
      ↓
Memoize Result
```

---

## 🔗 Related Problems

| Problem                         | Difficulty | Concept          |
| ------------------------------- | ---------- | ---------------- |
| Word Break #139                 | Medium     | Memoization / DP |
| Interleaving String #97         | Medium     | String DP        |
| Regular Expression Matching #10 | Hard       | Recursive DP     |
| Wildcard Matching #44           | Hard       | String DP        |

---

## 📖 Reference

* [LeetCode — Scramble String](https://leetcode.com/problems/scramble-string/)
* [Python — functools.cache](https://docs.python.org/3/library/functools.html)

---

<p align="center">
  <b>LeetCode #87 • Scramble String</b>
  <br>
  Memoized DFS • Dynamic Programming • Python
</p>
