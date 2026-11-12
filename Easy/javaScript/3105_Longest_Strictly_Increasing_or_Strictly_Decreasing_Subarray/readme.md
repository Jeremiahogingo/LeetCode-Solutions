# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Array%20%7C%20Greedy-purple)
![LeetCode](https://img.shields.io/badge/LeetCode-3105-blue)

## Problem

**[Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/)**

Given an integer array `nums`, find the length of the longest contiguous subarray that is either:

- **Strictly increasing:** Every element is greater than the previous element.
- **Strictly decreasing:** Every element is smaller than the previous element.

Return the maximum length among these two types of subarrays.

A subarray must contain consecutive elements from the original array. Equal adjacent elements break both strictly increasing and strictly decreasing sequences.

## Approach: Single-Pass Greedy

The solution uses three variables to track the current sequences and the maximum length found.

### Variables

| Variable | Purpose |
|---|---|
| `increasing` | Length of the current strictly increasing subarray |
| `decreasing` | Length of the current strictly decreasing subarray |
| `maxLength` | Longest valid subarray encountered |

All variables are initially set to `1` because an individual element forms a valid subarray of length one.

### Algorithm

Traverse the array starting from index `1`, comparing each element with its predecessor.

**1. Strictly Increasing**

When:

```javascript
nums[i] > nums[i - 1]
```

- Increment `increasing`.
- Reset `decreasing` to `1`.

**2. Strictly Decreasing**

When:

```javascript
nums[i] < nums[i - 1]
```

- Increment `decreasing`.
- Reset `increasing` to `1`.

**3. Equal Elements**

When:

```javascript
nums[i] === nums[i - 1]
```

- Reset both counters to `1`.
- Neither monotonic sequence can continue.

After each comparison, update `maxLength` using the larger of the two counters.

## JavaScript Solution

```javascript
/**
 * LeetCode 3105 - Longest Strictly Increasing or
 * Strictly Decreasing Subarray
 *
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    let increasing = 1;
    let decreasing = 1;
    let maxLength = 1;

    for (let i = 1; i < nums.length; i++) {

        if (nums[i] > nums[i - 1]) {
            // Continue the increasing sequence.
            increasing++;
            decreasing = 1;

        } else if (nums[i] < nums[i - 1]) {
            // Continue the decreasing sequence.
            decreasing++;
            increasing = 1;

        } else {
            // Equal elements break both sequences.
            increasing = 1;
            decreasing = 1;
        }

        // Update the longest valid subarray.
        maxLength = Math.max(
            maxLength,
            increasing,
            decreasing
        );
    }

    return maxLength;
};
```

## Examples and Dry Runs

### Example 1: Mixed Increasing and Decreasing Values

**Input:**

```javascript
nums = [1, 4, 3, 3, 2];
```

**Dry Run:**

| Index | Previous | Current | Comparison | Increasing | Decreasing | Maximum |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 1 | 4 | Increasing | 2 | 1 | 2 |
| 2 | 4 | 3 | Decreasing | 1 | 2 | 2 |
| 3 | 3 | 3 | Equal | 1 | 1 | 2 |
| 4 | 3 | 2 | Decreasing | 1 | 2 | 2 |

The longest valid subarrays have length `2`.

**Output:**

```javascript
2
```

### Example 2: All Elements Equal

**Input:**

```javascript
nums = [3, 3, 3, 3];
```

Every comparison encounters equal adjacent elements, so both counters reset to `1`.

**Output:**

```javascript
1
```

### Example 3: Strictly Decreasing Array

**Input:**

```javascript
nums = [3, 2, 1];
```

The decreasing sequence progresses as follows:

- `[3]` has length `1`.
- `[3, 2]` has length `2`.
- `[3, 2, 1]` has length `3`.

**Output:**

```javascript
3
```

### Example 4: Increasing Then Decreasing

**Input:**

```javascript
nums = [1, 2, 3, 2, 1];
```

The array contains two valid monotonic subarrays:

- Increasing: `[1, 2, 3]`, length `3`.
- Decreasing: `[3, 2, 1]`, length `3`.

**Output:**

```javascript
3
```

## Complexity Analysis

Let `n` represent the length of the input array.

| Complexity | Value | Explanation |
|---|---|---|
| Time | `O(n)` | Each element is visited exactly once. |
| Auxiliary Space | `O(1)` | Only three tracking variables are maintained. |

**Time Complexity: `O(n)`**

The algorithm performs one traversal and a constant number of comparisons and updates for each element.

**Auxiliary Space Complexity: `O(1)`**

No additional arrays, lists, or data structures proportional to the input size are created.

## Important Edge Cases

| Scenario | Input | Output |
|---|---|---:|
| Single element | `[5]` | 1 |
| All elements equal | `[3,3,3,3]` | 1 |
| Strictly increasing | `[1,2,3,4]` | 4 |
| Strictly decreasing | `[4,3,2,1]` | 4 |
| Alternating values | `[1,3,2,4,3]` | 2 |
| Mixed directions | `[1,2,3,2,1]` | 3 |

## Common Mistakes

**1. Confusing Subarrays with Subsequences**

A subarray must contain consecutive elements. Skipping elements changes the problem into a subsequence problem.

**2. Ignoring Strict Comparisons**

The conditions must use `>` and `<`, not `>=` or `<=`.

Equal adjacent values cannot extend either sequence.

**3. Forgetting to Reset the Opposite Counter**

When an increasing sequence continues, the decreasing counter must reset. The reverse applies when a decreasing sequence continues.

**4. Not Updating the Maximum**

Both increasing and decreasing sequences must be considered when updating the answer.

## Key Takeaways

- A contiguous subarray cannot skip elements.
- Strictly increasing and decreasing sequences can be tracked independently.
- Equal adjacent elements break both monotonic sequences.
- Greedy tracking avoids nested loops and unnecessary data structures.
- A single traversal is sufficient to obtain the optimal result.
- Maintaining the current state and resetting it when conditions change is a useful pattern for array problems.

## Related Problems

| Problem | Difficulty | Main Concept |
|---|---|---|
| [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | Easy | Increasing Subarray |
| [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Dynamic Programming / Binary Search |
| [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/) | Easy | Greedy / Array |
| [978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) | Medium | Array / Dynamic Programming |

## Repository Structure

```text
LeetCode-Solutions/
└── Easy/
    └── JavaScript/
        ├── 3105_Longest_Strictly_Increasing_or_Strictly_Decreasing_Subarray.js
        └── README.md
```

## References

- [LeetCode – Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)
- [MDN – JavaScript Math.max()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max)

---

**Problem:** 3105  
**Difficulty:** Easy  
**Language:** JavaScript  
**Topics:** Array, Greedy, Monotonic Subarray  
**Time Complexity:** `O(n)`  
**Auxiliary Space:** `O(1)`