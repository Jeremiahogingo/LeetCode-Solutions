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

            # Elements immediately around each partition.
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # Check whether the partition is valid.
            if left1 <= right2 and left2 <= right1:

                # Odd total: return the largest left element.
                if (m + n) % 2:
                    return float(max(left1, left2))

                # Even total: average the two middle elements.
                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                right = i - 1

            else:
                left = i + 1

        return 0.0