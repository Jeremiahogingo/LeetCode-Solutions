# 2914. Minimum Number of Changes to Make Binary String Beautiful

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Time Complexity](https://img.shields.io/badge/Time-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space-O(1)-brightgreen)

## Problem

**LeetCode:** [Minimum Number of Changes to Make Binary String Beautiful](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/)

**Difficulty:** Medium

**Language:** JavaScript

Given a binary string `s`, determine the minimum number of character changes required to make it beautiful.

A binary string is considered beautiful if it can be partitioned into one or more substrings such that:

- Every substring has an even length.
- Every substring contains only identical characters (`0`s or `1`s).

Each operation changes one character from `0` to `1` or from `1` to `0`.

Return the minimum number of operations required.

## Approach: Greedy

The key observation is that every valid substring has an even length. Consequently, every partition boundary must occur at an even index.

We can therefore divide the string into non-overlapping pairs:

```text
s[0], s[1] | s[2], s[3] | s[4], s[5] | ...
```

For each pair:

- If both characters are equal (`00` or `11`), no changes are needed.
- If the characters differ (`01` or `10`), exactly one character must be changed.

Count the mismatched pairs to obtain the minimum number of operations.

## JavaScript Solution

**File:** `2914_Minimum_Number_of_Changes_to_Make_Binary_String_Beautiful.js`

```javascript
/**
 * LeetCode 2914 - Minimum Number of Changes
 * to Make Binary String Beautiful
 *
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    let changes = 0;

    // Process the string in non-overlapping pairs.
    for (let i = 0; i < s.length; i += 2) {
        // Every pair must contain identical characters.
        if (s[i] !== s[i + 1]) {
            changes++;
        }
    }

    return changes;
};
```

## Examples

### Example 1

**Input:**
```text
s = "1001"
```

**Pair analysis:**
```text
10 | 01
```

Both pairs contain different characters, so each requires one change.

**Output:**
```text
2
```

One valid resulting string is `1100`, which can be partitioned into `11 | 00`.

### Example 2

**Input:**
```text
s = "10"
```

**Pair analysis:**
```text
10
```

One character must be changed.

**Output:**
```text
1
```

### Example 3

**Input:**
```text
s = "0000"
```

**Pair analysis:**
```text
00 | 00
```

Both pairs already contain identical characters.

**Output:**
```text
0
```

## Complexity Analysis

Let `n` represent the length of the input string.

| Complexity | Value | Explanation |
|---|---|---|
| Time | `O(n)` | Each character is examined once as part of a pair. |
| Auxiliary Space | `O(1)` | Only a counter and loop variable are used. |

## Key Takeaways

1. **Recognize structural constraints:** Even-length partitions imply that valid boundaries occur at even indices.
2. **Use greedy decisions:** Each mismatched pair independently requires exactly one change.
3. **Avoid unnecessary complexity:** No dynamic programming, recursion, or additional data structures are needed.
4. **Optimize space:** A single counter is sufficient.

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── JavaScript/
        ├── 2914_Minimum_Number_of_Changes_to_Make_Binary_String_Beautiful.js
        └── README.md
```

## References

- [LeetCode Problem 2914](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/)
- [Greedy Algorithms](https://en.wikipedia.org/wiki/Greedy_algorithm)

---

**Solution Status:** Completed

**Approach:** Greedy — Pairwise Comparison

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`