# 44. Wildcard Matching

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Approach](https://img.shields.io/badge/Approach-Dynamic_Programming-blue)
![Time Complexity](https://img.shields.io/badge/Time-O(m%C3%97n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space-O(n)-brightgreen)

## Problem

**LeetCode:** [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

**Difficulty:** Hard

**Language:** JavaScript

Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for two special characters:

- `?` — Matches exactly one character.
- `*` — Matches any sequence of characters, including an empty sequence.

All other characters must match literally.

The pattern must match the **entire input string**, not just a substring.

Return `true` if the pattern matches the input string; otherwise, return `false`.

## Approach: Dynamic Programming with Space Optimization

We use dynamic programming to determine whether prefixes of the input string match prefixes of the pattern.

Instead of maintaining a two-dimensional DP table, we optimize the solution to use a one-dimensional array.

### DP State

Let:

`dp[j]` represent whether the currently processed prefix of `s` matches the first `j` characters of `p`.

Initially:

```javascript
dp[0] = true;
```

This represents the fact that two empty strings match.

### State Transitions

There are three possible cases.

**1. Normal character**

If the current pattern character matches the current string character:

```text
dp[i][j] = dp[i-1][j-1]
```

Both characters must match, and the preceding prefixes must also match.

**2. Question mark (`?`)**

The `?` wildcard matches exactly one character:

```text
dp[i][j] = dp[i-1][j-1]
```

The same diagonal transition applies because `?` consumes one character.

**3. Asterisk (`*`)**

The `*` wildcard can match an empty sequence or consume another character:

```text
dp[i][j] = dp[i][j-1] OR dp[i-1][j]
```

- `dp[i][j-1]`: The `*` matches an empty sequence.
- `dp[i-1][j]`: The `*` consumes one additional character.

### JavaScript Solution

**File:** `44_Wildcard_Matching.js`

```javascript
/**
 * LeetCode 44 - Wildcard Matching
 *
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    const m = s.length;
    const n = p.length;

    // dp[j] indicates whether the current prefix of s
    // matches the first j characters of p.
    const dp = Array(n + 1).fill(false);

    // Two empty strings match.
    dp[0] = true;

    // Leading '*' characters can match an empty string.
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*') {
            dp[j] = dp[j - 1];
        } else {
            break;
        }
    }

    // Process each character in s.
    for (let i = 1; i <= m; i++) {
        // Previous row's first column is always false.
        let diagonal = dp[0];
        dp[0] = false;

        for (let j = 1; j <= n; j++) {
            // Preserve the previous row's value.
            const previous = dp[j];

            if (p[j - 1] === '*') {
                // '*' matches an empty sequence or
                // consumes one additional character.
                dp[j] = dp[j - 1] || previous;
            } else {
                // '?' matches any single character.
                // Normal characters must match exactly.
                dp[j] =
                    diagonal &&
                    (p[j - 1] === '?' || p[j - 1] === s[i - 1]);
            }

            // Preserve the previous diagonal for the next cell.
            diagonal = previous;
        }
    }

    return dp[n];
};
```

## Example Walkthroughs

### Example 1

**Input:**

```text
s = "aa"
p = "a"
```

**Output:**

```text
false
```

**Explanation:**

The pattern contains only one character, while the input contains two. Without `*`, the pattern cannot match the entire string.

### Example 2

**Input:**

```text
s = "aa"
p = "*"
```

**Output:**

```text
true
```

**Explanation:**

The `*` wildcard can match the entire input string.

### Example 3

**Input:**

```text
s = "cb"
p = "?a"
```

**Output:**

```text
false
```

**Explanation:**

- `?` matches `c`.
- `a` does not match `b`.

### Example 4

**Input:**

```text
s = "adceb"
p = "*a*b"
```

**Output:**

```text
true
```

**Explanation:**

One valid interpretation is:

| Pattern character | Matched sequence |
|---|---|
| `*` | Empty string |
| `a` | `a` |
| `*` | `dce` |
| `b` | `b` |

The entire input string is successfully matched.

### Example 5

**Input:**

```text
s = "acdcb"
p = "a*c?b"
```

**Output:**

```text
false
```

**Explanation:**

No valid assignment of characters to `*` allows the remaining pattern to match the entire input string.

## Space Optimization

A conventional dynamic programming solution uses a two-dimensional table:

```text
dp[m + 1][n + 1]
```

This requires `O(m × n)` auxiliary space.

However, each state depends only on:

- The previous row's same column.
- The current row's previous column.
- The previous row's previous column.

These values can be preserved using:

- A one-dimensional DP array.
- A `diagonal` variable.
- A temporary `previous` variable.

This reduces auxiliary space to `O(n)` without changing the time complexity.

## Complexity Analysis

Let:

- `m` = length of the input string `s`.
- `n` = length of the pattern `p`.

| Complexity | Value | Explanation |
|---|---|---|
| Time | `O(m × n)` | Every DP state is processed once. |
| Auxiliary Space | `O(n)` | Only one DP array of size `n + 1` is maintained. |

## Edge Cases

| Input string | Pattern | Expected output |
|---|---|---|
| `""` | `""` | `true` |
| `""` | `"*"` | `true` |
| `""` | `"?"` | `false` |
| `"abc"` | `"***"` | `true` |
| `"abc"` | `"a*c"` | `true` |
| `"abc"` | `"a*d"` | `false` |
| `"abc"` | `"???"` | `true` |
| `"abc"` | `"??"` | `false` |

## Key Takeaways

1. **Dynamic Programming:** Useful when matching decisions create multiple possible paths.
2. **Wildcard `?`:** Consumes exactly one character.
3. **Wildcard `*`:** Can consume zero or more characters.
4. **State transitions:** A wildcard's behavior determines which previous DP states are combined.
5. **Space optimization:** A two-dimensional DP table can be compressed when transitions depend only on adjacent rows.
6. **Diagonal tracking:** Preserves the previous row's previous-column state during in-place updates.
7. **Full-string matching:** Both the input and pattern must be completely matched.

## Repository Structure

```text
LeetCode-Solutions/
└── Hard/
    └── JavaScript/
        └── 44_Wildcard_Matching.js
```

## References

- [LeetCode 44 — Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Wildcard Character](https://en.wikipedia.org/wiki/Wildcard_character)

---

**Solution Status:** Completed

**Primary Approach:** Dynamic Programming — Space Optimized

**Language:** JavaScript

**Time Complexity:** `O(m × n)`

**Auxiliary Space Complexity:** `O(n)`

**Key Concepts:** Dynamic Programming, String Matching, Wildcards, Rolling DP, Space Optimization