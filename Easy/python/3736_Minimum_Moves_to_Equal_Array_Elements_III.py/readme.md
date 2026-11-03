# LeetCode 3736: Minimum Moves to Equal Array Elements III

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topics](https://img.shields.io/badge/Topics-Array%20%7C%20Math-purple)

## Problem Description

Given an integer array `nums`, find the minimum number of moves required to make all elements equal.

In one move, you can increase any single element `nums[i]` by exactly `1`.

Return the minimum total number of moves needed to make every element equal.

**Problem link:** [LeetCode 3736 — Minimum Moves to Equal Array Elements III](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/)

## Approach: Greedy and Mathematics

Since elements can only be increased, the final target must be at least the maximum value in the array.

To minimize the number of moves, choose the current maximum element as the target. Choosing a larger target would require unnecessary additional increments.

The number of moves required for each element is:

\[
moves_i = \max(nums) - nums[i]
\]

Summing the differences gives:

\[
\boxed{Moves = n \times \max(nums) - \sum nums}
\]

### Algorithm

1. Find the maximum value in the array.
2. Use that maximum as the common target.
3. Calculate the difference between the target and every element.
4. Sum all differences and return the result.

## Python Solution

```python
from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)

        return sum(target - num for num in nums)
```

## Examples

**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `3`

Explanation:

The maximum value is `3`.

```text
[2, 1, 3] → [3, 2, 3] → [3, 3, 3]
```

The total moves are:

\[
(3-2)+(3-1)+(3-3)=1+2+0=3
\]

**Example 2**

- Input: `nums = [4, 4, 5]`
- Output: `2`

Explanation:

The maximum value is `5`.

```text
[4, 4, 5] → [5, 5, 5]
```

The total moves are:

\[
(5-4)+(5-4)+(5-5)=2
\]

## Complexity Analysis

Let \(n\) be the number of elements in `nums`.

- **Time Complexity:** \(O(n)\) — finding the maximum and calculating the total differences each require a linear traversal.
- **Auxiliary Space Complexity:** \(O(1)\) — only a constant amount of additional space is used.

## Key Takeaways

- When only increments are allowed, the final target cannot be smaller than the current maximum.
- Choosing the maximum minimizes the number of required increments.
- The solution does not require sorting or additional data structures.
- A mathematical observation reduces the problem to a simple linear traversal.
- This problem demonstrates how operation constraints determine the optimal target.

## Related Problems

These problems explore similar array-equalization and mathematical optimization techniques.

| Problem | Difficulty | Connection |
|---|---|---|
| [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) | Medium | Equalize an array using a different increment operation. |
| [462. Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) | Medium | Uses the median when both increments and decrements are allowed. |
| [296. Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) | Hard | Uses the median to minimize total distance. |
| [2033. Minimum Operations to Make a Uni-Value Grid](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/) | Medium | Finds a common target using median-based optimization. |
| [2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/) | Hard | Extends array equalization to weighted operation costs. |

## Repository Structure

```text
LeetCode-Solutions/
└── Easy/
    └── Python/
        ├── 3736_Minimum_Moves_to_Equal_Array_Elements_III.py
        └── README.md
```

## References

- [LeetCode Problem 3736](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html#max)
- [Python `sum()` Documentation](https://docs.python.org/3/library/functions.html#sum)