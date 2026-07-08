class Solution {

    public int maxArea(int[] height) {

        int left = 0;
        int right = height.length - 1;

        int maxArea = 0;

        while (left < right) {

            // Width between the two lines
            int width = right - left;

            // Height is determined by the shorter line
            int currentArea = width * Math.min(height[left], height[right]);

            // Update maximum area
            maxArea = Math.max(maxArea, currentArea);

            // Move the shorter pointer
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }

        }

        return maxArea;

    }

}