# LeetCode 1385: Find the Distance Value Between Two Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topics](https://img.shields.io/badge/Topics-Array%20%7C%20Sorting%20%7C%20Binary%20Search-purple)

## Problem Description

Given two integer arrays, `arr1` and `arr2`, and an integer `d`, return the distance value between the two arrays.

The distance value is the number of elements in `arr1` for which there is no element in `arr2` satisfying:

\[
|arr1[i] - arr2[j]| \leq d
\]

In other words, an element from `arr1` qualifies only when its absolute difference from every element in `arr2` is strictly greater than `d`.

**Problem link:** [LeetCode 1385 — Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/)

## Approach: Sorting and Binary Search

Sort `arr2` and use binary search to efficiently identify the closest elements to each value in `arr1`.

1. Sort `arr2` in ascending order.
2. Iterate through each element in `arr1`.
3. Use `bisect_left()` to find the insertion position of the current element in `arr2`.
4. Check the closest element on the left and the closest element on the right.
5. If both differences are strictly greater than `d`, increment the distance-value counter.
6. Return the final count.

Because `arr2` is sorted, the closest value must be either at the insertion position or immediately before it.

## Python Solution

```python
from bisect import bisect_left
from typing import List

class Solution:
    def findTheDistanceValue(
        self, arr1: List[int], arr2: List[int], d: int
    ) -> int:

        arr2.sort()
        count = 0

        for num in arr1:
            index = bisect_left(arr2, num)

            # Check the closest value on the right.
            right_valid = (
                index == len(arr2)
                or arr2[index] - num > d
            )

            # Check the closest value on the left.
            left_valid = (
                index == 0
                or num - arr2[index - 1] > d
            )

            if left_valid and right_valid:
                count += 1

        return count
```

## Examples

**Example 1**

- Input: `arr1 = [4,5,8]`, `arr2 = [10,9,1,8]`, `d = 2`
- Output: `2`

Explanation:

After sorting `arr2`:

```text
arr2 = [1, 8, 9, 10]
```

| arr1 element | Closest distance | Qualifies? |
|---:|---:|---|
| 4 | 3 | Yes |
| 5 | 3 | Yes |
| 8 | 0 | No |

Only `4` and `5` satisfy the distance requirement.

**Example 2**

- Input: `arr1 = [1,4,2,3]`, `arr2 = [-4,-3,6,10,20,30]`, `d = 3`
- Output: `2`

**Example 3**

- Input: `arr1 = [2,1,100,3]`, `arr2 = [-5,-2,10,-3,7]`, `d = 6`
- Output: `1`

## Complexity Analysis

Let:
- \(n\) be the length of `arr1`.
- \(m\) be the length of `arr2`.

**Time Complexity:** \(O(m\log m+n\log m)\)

- Sorting `arr2` takes \(O(m\log m)\).
- Binary searching for each element in `arr1` takes \(O(n\log m)\).
- Checking the two neighboring elements takes \(O(1)\) per iteration.

**Auxiliary Space Complexity:** \(O(m)\) worst case for Python's sorting implementation.

The sorting operation modifies `arr2` in place.

## Key Takeaways

- Sorting enables efficient binary search.
- `bisect_left()` finds the insertion position of an element in a sorted list.
- The closest possible values are the elements immediately surrounding the insertion position.
- The comparison must use `> d`, not `>= d`, because a distance equal to `d` does not qualify.
- Binary search reduces the need for repeated linear comparisons.

## Related Problems

These problems reinforce sorting, binary search, insertion positions, and finding nearby elements.

| Problem | Difficulty | Connection |
|---|---|---|
| [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Fundamental binary search implementation. |
| [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Finds the insertion position of a target. |
| [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | Uses sets and array comparisons. |
| [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | Easy | Combines sorting and two-pointer techniques. |
| [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Medium | Uses binary search to locate nearby elements. |

## Repository Structure

```text
LeetCode-Solutions/
└── Easy/
    └── Python/
        └── 1385_Find_the_Distance_Value_Between_Two_Arrays.py
```

## References

- [LeetCode Problem 1385](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/)
- [Python bisect Documentation](https://docs.python.org/3/library/bisect.html)
- [Python Sorting Documentation](https://docs.python.org/3/howto/sorting.html)