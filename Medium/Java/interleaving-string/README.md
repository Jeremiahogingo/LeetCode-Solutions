# LeetCode 97: Interleaving String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Java-orange)
![Topic](https://img.shields.io/badge/Topic-Dynamic%20Programming-blue)

## Problem Description

Given strings `s1`, `s2`, and `s3`, determine whether `s3` is formed by interleaving `s1` and `s2`.

An interleaving combines characters from both strings while preserving the relative order of characters within each original string.

**Problem link:** [LeetCode 97 — Interleaving String](https://leetcode.com/problems/interleaving-string/description/)

## Approach: Dynamic Programming

Use a one-dimensional boolean array to determine whether prefixes of `s1` and `s2` can form the corresponding prefix of `s3`.

1. If the combined lengths of `s1` and `s2` differ from the length of `s3`, return `false`.
2. Initialize the DP array to handle prefixes formed using only `s2`.
3. Iterate through `s1` and update the DP states for each character of `s2`.
4. At each state, check whether the current character of `s3` can come from either `s1` or `s2`.
5. Return the final DP state.

The array is updated in place, reducing space complexity from \(O(mn)\) to \(O(n)\).

## Java Solution

```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length();
        int n = s2.length();

        if (m + n != s3.length()) {
            return false;
        }

        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int j = 1; j <= n; j++) {
            dp[j] = dp[j - 1]
                && s2.charAt(j - 1) == s3.charAt(j - 1);
        }

        for (int i = 1; i <= m; i++) {
            dp[0] = dp[0]
                && s1.charAt(i - 1) == s3.charAt(i - 1);

            for (int j = 1; j <= n; j++) {
                char target = s3.charAt(i + j - 1);

                boolean fromS1 = dp[j]
                    && s1.charAt(i - 1) == target;

                boolean fromS2 = dp[j - 1]
                    && s2.charAt(j - 1) == target;

                dp[j] = fromS1 || fromS2;
            }
        }

        return dp[n];
    }
}
```

## Examples

**Example 1**

- Input: `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbcbcac"`
- Output: `true`
- Explanation: The characters can be interleaved while preserving the order within both source strings.

**Example 2**

- Input: `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbbaccc"`
- Output: `false`
- Explanation: No valid interleaving produces `s3` while preserving the order of both source strings.

**Example 3**

- Input: `s1 = ""`, `s2 = ""`, `s3 = ""`
- Output: `true`
- Explanation: Both source strings are empty, so their interleaving is also empty.

## Complexity Analysis

Let \(m = |s1|\) and \(n = |s2|\).

- **Time Complexity:** \(O(mn)\) — each DP state is computed in constant time.
- **Space Complexity:** \(O(n)\) — a one-dimensional array stores the DP states.

## Key Takeaways

- Dynamic programming is useful when a problem can be broken into overlapping subproblems.
- Character order must be preserved within each source string.
- The length check eliminates impossible cases immediately.
- Space optimization allows the solution to use one DP array instead of a two-dimensional table.

## References

- [LeetCode Problem 97](https://leetcode.com/problems/interleaving-string/description/)
- [Dynamic Programming — Introduction](https://en.wikipedia.org/wiki/Dynamic_programming)
