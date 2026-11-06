# LeetCode 4: Median of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topics](https://img.shields.io/badge/Topics-Array%20%7C%20Binary%20Search%20%7C%20Divide%20and%20Conquer-purple)

## Problem Description

Given two sorted arrays, `nums1` and `nums2`, return the median of the two arrays combined.

The median is:
- The middle element when the total number of elements is odd.
- The average of the two middle elements when the total number of elements is even.

The solution must achieve logarithmic time complexity rather than merging the arrays completely.

**Problem link:** [LeetCode 4 — Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

## Approach: Binary Search on Partitions

Use binary search on the smaller array to find a partition that divides both arrays into two balanced halves.

A valid partition must satisfy two conditions:

\[
Left_1 \leq Right_2
\]

\[
Left_2 \leq Right_1
\]

These conditions ensure that every element in the combined left partition is less than or equal to every element in the combined right partition.

Once a valid partition is found:

- For an odd total length, the median is the largest element in the left partition.
- For an even total length, the median is the average of the largest left element and the smallest right element.

### Algorithm

1. Ensure `nums1` is the smaller array to minimize the binary search range.
2. Calculate the number of elements required in the left partition.
3. Initialize binary search boundaries from `0` to the length of `nums1`.
4. Calculate the partition positions in both arrays.
5. Identify the four boundary values around the partitions.
6. Check whether the partition is valid.
7. If the first partition contains an element that is too large, move the binary search left.
8. Otherwise, move it right.
9. Calculate and return the median once a valid partition is found.

Use negative and positive infinity to handle empty partitions safely.

## Python Solution

```python
from typing import List

class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        # Always binary search the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            # Partition positions.
            i = (left + right) // 2
            j = half - i

            # Values around the partitions.
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # Check whether the partition is valid.
            if left1 <= right2 and left2 <= right1:

                # Odd total length.
                if (m + n) % 2:
                    return float(max(left1, left2))

                # Even total length.
                return (
                    max(left1, left2) +
                    min(right1, right2)
                ) / 2

            elif left1 > right2:
                right = i - 1

            else:
                left = i + 1

        return 0.0
```

## Examples

**Example 1**

- Input: `nums1 = [1,3]`, `nums2 = [2]`
- Output: `2.0`

Explanation:

The combined sorted array would be `[1,2,3]`.

Since the total number of elements is odd, the middle element is `2`.

**Example 2**

- Input: `nums1 = [1,2]`, `nums2 = [3,4]`
- Output: `2.5`

Explanation:

The combined sorted array would be `[1,2,3,4]`.

Since the total number of elements is even:

\[
Median = \frac{2+3}{2}=2.5
\]

**Example 3**

- Input: `nums1 = []`, `nums2 = [1]`
- Output: `1.0`

Explanation:

One array is empty, so the median is simply the only element in the non-empty array.

**Example 4**

- Input: `nums1 = [2]`, `nums2 = [3,4,5,6]`
- Output: `4.0`

Explanation:

The combined sorted order is `[2,3,4,5,6]`, making `4` the middle element.

## Complexity Analysis

Let:
- \(m\) be the length of `nums1`.
- \(n\) be the length of `nums2`.

- **Time Complexity:** \(O(\log(\min(m,n)))\) — binary search is performed only on the smaller array.
- **Auxiliary Space Complexity:** \(O(1)\) — only a constant number of variables are maintained.

The arrays are never merged or sorted again.

## Key Takeaways

- Binary search can be applied to partition positions rather than individual target values.
- Always search the smaller array to keep the search range minimal.
- Four boundary values are sufficient to validate a partition.
- Negative and positive infinity handle empty partitions safely.
- Odd-sized arrays use the maximum left partition value as the median.
- Even-sized arrays use the average of the maximum left and minimum right values.
- The correct partition eliminates the need to merge the arrays.

## Related Problems

These problems reinforce binary search, sorted-array partitioning, and divide-and-conquer techniques.

| Problem | Difficulty | Connection |
|---|---|---|
| [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Binary search for an insertion position. |
| [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Fundamental binary search implementation. |
| [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Binary search on modified sorted data. |
| [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Binary search using partition properties. |
| [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Medium | Binary search for an optimal position in sorted data. |
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Work with multiple sorted data structures. |

## Repository Structure

```text
LeetCode-Solutions/
└── Hard/
    └── Python/
        └── 4_Median_of_Two_Sorted_Arrays.py
```

## References

- [LeetCode Problem 4](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
- [Python Binary Search Documentation](https://docs.python.org/3/library/bisect.html)
- [Binary Search — Algorithm Explanation](https://en.wikipedia.org/wiki/Binary_search_algorithm)