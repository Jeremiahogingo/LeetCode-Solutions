from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)

        return sum(target - num for num in nums)