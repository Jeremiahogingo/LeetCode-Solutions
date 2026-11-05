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