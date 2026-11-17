# 2911. Minimum Changes to Make K Semi-palindromes

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Dynamic%20Programming-blue)

## Problem

**[Minimum Changes to Make K Semi-palindromes](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/)**

Given a string `s` and an integer `k`, split `s` into exactly `k` non-empty contiguous substrings.

A substring is a **semi-palindrome** if there exists a proper divisor `d` of its length such that, for every remainder from `0` to `d - 1`, the characters at positions with that remainder modulo `d` form a palindrome.

You may replace any character with another lowercase English letter.

Return the minimum number of character replacements required to make all `k` substrings semi-palindromes.

### Examples

**Example 1**

```text
Input: s = "abcac", k = 2
Output: 1
```

**Example 2**

```text
Input: s = "abcdef", k = 2
Output: 2
```

**Example 3**

```text
Input: s = "aabbaa", k = 3
Output: 0
```

### Constraints

- `2 <= s.length <= 200`
- `1 <= k <= s.length / 2`
- `s` contains only lowercase English letters.

---

## Approach: Precomputation + Dynamic Programming

The solution separates the problem into two stages:

1. Precompute the minimum cost of converting every substring into a semi-palindrome.
2. Use dynamic programming to find the minimum total cost of splitting the string into exactly `k` valid substrings.

### 1. Precompute proper divisors

For a substring of length `L`, a valid divisor `d` must satisfy:

- `d < L`
- `L % d === 0`

We precompute all valid divisors for every possible substring length.

### 2. Calculate semi-palindrome conversion costs

For each substring `s[i...j]`:

- Try every proper divisor `d` of its length.
- Divide the substring's positions into groups based on their index modulo `d`.
- Each group must form a palindrome.
- Compare mirrored characters within each group.
- Every mismatched pair requires one replacement.

The minimum number of replacements across all valid divisors becomes:

```javascript
cost[i][j]
```

### 3. Dynamic programming

Define:

```text
dp[p][i] = minimum replacements needed to divide
           the first i characters into exactly p
           semi-palindromic substrings.
```

**Base case:**

```javascript
dp[0][0] = 0;
```

All other states initially contain `Infinity`.

**Transition:**

If the final substring begins at index `j` and ends at `i - 1`:

```text
dp[p][i] = min(
    dp[p][i],
    dp[p - 1][j] + cost[j][i - 1]
)
```

The final substring must contain at least two characters, and enough characters must remain for the other required substrings.

The answer is:

```javascript
dp[k][n]
```

---

## JavaScript Solution

**File:** `2911_Minimum_Changes_to_Make_K_Semi_palindromes.js`

```javascript
/**
 * LeetCode 2911 - Minimum Changes to Make K Semi-palindromes
 *
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var minimumChanges = function(s, k) {
    const n = s.length;
    const INF = Infinity;

    // Precompute all proper divisors for possible substring lengths.
    const divisors = Array.from({ length: n + 1 }, () => []);

    for (let d = 1; d < n; d++) {
        for (let len = d * 2; len <= n; len += d) {
            divisors[len].push(d);
        }
    }

    // cost[i][j] = minimum changes to make s[i...j]
    // a semi-palindrome.
    const cost = Array.from(
        { length: n },
        () => Array(n).fill(INF)
    );

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const len = j - i + 1;

            for (const d of divisors[len]) {
                let changes = 0;

                // Compare corresponding positions in each
                // modulo-d group from opposite ends.
                for (let offset = 0; offset < d; offset++) {
                    let left = i + offset;
                    let right = j - d + 1 + offset;

                    while (left < right) {
                        if (s[left] !== s[right]) {
                            changes++;
                        }

                        left += d;
                        right -= d;
                    }
                }

                cost[i][j] = Math.min(
                    cost[i][j],
                    changes
                );
            }
        }
    }

    // dp[p][i] = minimum changes to partition the first i
    // characters into exactly p semi-palindromes.
    const dp = Array.from(
        { length: k + 1 },
        () => Array(n + 1).fill(INF)
    );

    dp[0][0] = 0;

    for (let p = 1; p <= k; p++) {
        // Each substring must contain at least 2 characters.
        const minEnd = p * 2;
        const maxEnd = n - (k - p) * 2;

        for (let i = minEnd; i <= maxEnd; i++) {
            // The final substring is s[j...i-1].
            // It must have a length of at least 2.
            for (let j = (p - 1) * 2; j <= i - 2; j++) {
                if (dp[p - 1][j] === INF) {
                    continue;
                }

                dp[p][i] = Math.min(
                    dp[p][i],
                    dp[p - 1][j] + cost[j][i - 1]
                );
            }
        }
    }

    return dp[k][n];
};
```

---

## Complexity Analysis

Let `n` be the length of the input string and `k` the required number of substrings.

| Operation | Complexity |
|---|---|
| Divisor precomputation | `O(n log n)` |
| Substring cost precomputation | `O(n³ log n)` upper bound |
| Dynamic programming | `O(kn²)` |
| Cost matrix | `O(n²)` |
| DP table | `O(kn)` |

**Overall time complexity:** `O(n³ log n + kn²)` (conservative upper bound).

**Overall auxiliary space complexity:** `O(n² + kn)`.

---

## Key Takeaways

- Precomputation avoids repeatedly calculating semi-palindrome conversion costs during DP transitions.
- Modular indexing provides a way to identify the character groups that must independently form palindromes.
- A mismatch between mirrored characters requires exactly one replacement.
- Partition DP is useful when a sequence must be divided into an exact number of valid contiguous segments.
- Restricting DP transitions using minimum segment lengths avoids considering impossible states.

## Repository Structure

```text
LeetCode-Solutions/
└── Hard/
    └── JavaScript/
        ├── 2911_Minimum_Changes_to_Make_K_Semi_palindromes.js
        └── README.md
```

## References

- [LeetCode Problem 2911](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Divisor](https://en.wikipedia.org/wiki/Divisor)

---

**Author:** [Jeremiah Ogingo](https://github.com/Jeremiahogingo)

**Repository:** [LeetCode-Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions)