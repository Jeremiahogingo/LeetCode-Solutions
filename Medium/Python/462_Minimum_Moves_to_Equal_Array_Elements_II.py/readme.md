# LeetCode 462: Minimum Moves to Equal Array Elements II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topics](https://img.shields.io/badge/Topics-Array%20%7C%20Math%20%7C%20Sorting-purple)

## Problem Description

Given an integer array `nums`, return the minimum number of moves required to make all elements equal.

In one move, you can increment or decrement any element by `1`.

The objective is to find a target value that minimizes the total number of moves required to make every array element equal to that target.

**Problem link:** [LeetCode 462 — Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)

## Approach: Sorting and Median

The optimal target is the **median** of the array because it minimizes the sum of absolute differences between all elements and a common target.

1. Sort the array in ascending order.
2. Select the middle element as the target median.
3. Calculate the absolute difference between every element and the median.
4. Sum the differences to obtain the minimum number of moves.

For an even-length array, either of the two middle values produces the same minimum number of moves.

## Python Solution

```python
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        median = nums[len(nums) // 2]

        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves
```

## Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `2`

Explanation:

The median is `2`.

```text
[1, 2, 3] → [2, 2, 3] → [2, 2, 2]
```

Total moves:

\[
|1-2| + |2-2| + |3-2| = 2
\]

**Example 2**

- Input: `nums = [1, 10, 2, 9]`
- Output: `16`

Explanation:

After sorting:

```text
[1, 2, 9, 10]
```

The selected median is `9`.

\[
|1-9| + |2-9| + |9-9| + |10-9| = 16
\]

## Complexity Analysis

Let \(n\) be the number of elements in `nums`.

- **Time Complexity:** \(O(n\log n)\) — sorting dominates the execution time, while calculating the total moves takes \(O(n)\).
- **Auxiliary Space Complexity:** \(O(n)\) worst case for Python's sorting implementation, which may require temporary storage.

The sorting operation modifies the original input array.

## Key Takeaways

- The median minimizes the sum of absolute differences.
- Sorting makes it straightforward to identify a median.
- Absolute differences measure the moves required to reach a common target.
- For even-sized arrays, either middle element is an optimal target.
- This problem demonstrates how a mathematical observation can simplify an optimization problem.

## Related Problems

These problems reinforce median-based optimization, absolute differences, and array transformations.

| Problem | Difficulty | Connection |
|---|---|---|
| [296. Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) | Hard | Uses the median to minimize total Manhattan distance. |
| [2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/) | Hard | Extends median-based optimization using weighted costs. |
| [2033. Minimum Operations to Make a Uni-Value Grid](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/) | Medium | Uses the median to find an optimal common target. |
| [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) | Medium | Explores a related array-equalization problem with a different operation. |

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── Python/
        ├── 462_Minimum_Moves_to_Equal_Array_Elements_II.py
        └── README.md
```

## References

- [LeetCode Problem 462](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)
- [Median — Mathematical Explanation](https://en.wikipedia.org/wiki/Median)
- [Python Sorting Documentation](https://docs.python.org/3/howto/sorting.html)