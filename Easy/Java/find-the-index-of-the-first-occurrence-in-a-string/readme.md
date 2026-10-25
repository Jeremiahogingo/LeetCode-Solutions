# LeetCode 28: Find the Index of the First Occurrence in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-Java-orange)
![Topic](https://img.shields.io/badge/Topic-String%20Matching-blue)

## Problem Description

Given two strings, `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`. If `needle` does not occur in `haystack`, return `-1`.

If `needle` is an empty string, return `0`.

**Problem link:** [LeetCode 28 — Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Approach: Brute Force

Use a sliding starting position in `haystack` and compare the characters of `needle` against the corresponding characters in `haystack`.

1. Iterate through every valid starting index in `haystack`.
2. Compare characters until a mismatch occurs or the entire `needle` matches.
3. Return the starting index when all characters match.
4. If no match is found, return `-1`.

Java handles the empty-string case naturally: when `needle` is empty, the inner loop performs no comparisons, and the method returns `0`.

## Java Solution

```java
class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length();
        int m = needle.length();

        for (int i = 0; i <= n - m; i++) {
            int j = 0;

            while (j < m &&
                   haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }

            if (j == m) {
                return i;
            }
        }

        return -1;
    }
}
```

## Examples

**Example 1**

- Input: `haystack = "sadbutsad"`, `needle = "sad"`
- Output: `0`
- Explanation: `"sad"` first appears at index `0`.

**Example 2**

- Input: `haystack = "leetcode"`, `needle = "leeto"`
- Output: `-1`
- Explanation: The substring `"leeto"` does not occur in `"leetcode"`.

**Example 3**

- Input: `haystack = "hello"`, `needle = "ll"`
- Output: `2`
- Explanation: `"ll"` first appears at index `2`.

## Complexity Analysis

Let \(n\) be the length of `haystack` and \(m\) the length of `needle`.

- **Time Complexity:** \(O(nm)\) — in the worst case, up to \(m\) characters are compared at each of \(O(n)\) starting positions.
- **Space Complexity:** \(O(1)\) — only a constant number of variables are used.

## Key Takeaways

- A substring can be found by checking each valid starting position.
- The search must stop at index \(n-m\) to avoid accessing characters beyond the end of `haystack`.
- Returning immediately after a complete match guarantees the first occurrence is returned.
- For larger-scale string matching, algorithms such as Knuth–Morris–Pratt (KMP) can improve the worst-case time complexity to \(O(n+m)\).

## References

- [LeetCode Problem 28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- [Java String Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)
