class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            # Distance between the two lines
            width = right - left

            # Height is limited by the shorter line
            current_area = width * min(height[left], height[right])

            # Update maximum area found
            max_area = max(max_area, current_area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area