# 11. Container With Most Water

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topics](https://img.shields.io/badge/Topics-Two%20Pointers%20%7C%20Greedy-blue)

## Problem

Given an integer array `height` of length `n`, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container capable of holding the maximum amount of water.

Return the maximum amount of water that the container can store.

> **LeetCode:** https://leetcode.com/problems/container-with-most-water/

---

## Example

### Input

```text
height = [1,8,6,2,5,4,8,3,7]
```

### Output

```text
49
```

### Explanation

The maximum area is formed by the lines with heights **8** and **7**.

* Width = `8 - 1 = 7`
* Height = `min(8, 7) = 7`
* Area = `7 × 7 = 49`

---

# Approach

## Brute Force

The straightforward approach is to examine every possible pair of lines.

For each pair:

1. Compute the width.
2. Determine the limiting height using the shorter line.
3. Calculate the area.
4. Keep track of the maximum.

### Time Complexity

```text
O(n²)
```

Since every pair is checked, this solution becomes inefficient for large inputs.

---

# Optimized Approach — Two Pointers

Instead of checking every pair, use two pointers.

* Place one pointer at the beginning.
* Place the other at the end.
* Calculate the area formed by the two lines.
* Update the maximum area if necessary.

### Key Observation

The amount of water is limited by the **shorter** line.

Moving the taller line inward always reduces the width while keeping the limiting height the same or lower, so it cannot produce a larger area.

Therefore:

* If the left line is shorter, move the left pointer.
* Otherwise, move the right pointer.

This guarantees that every potentially optimal container is considered in linear time.

---

# Algorithm

1. Initialize two pointers:

   * `left = 0`
   * `right = n - 1`
2. While `left < right`

   * Calculate the width.
   * Calculate the area.
   * Update the maximum area.
   * Move the pointer pointing to the shorter line.
3. Return the maximum area.

---

# Python Solution

```python
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current = width * min(height[left], height[right])
            max_area = max(max_area, current)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

# Java Solution

```java
class Solution {
    public int maxArea(int[] height) {

        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {

            int width = right - left;
            int area = width * Math.min(height[left], height[right]);

            maxArea = Math.max(maxArea, area);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
```

---

# Complexity Analysis

| Metric | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

---

# Key Concepts

* Two Pointers
* Greedy Strategy
* Array Traversal
* Optimization
* Interview Pattern

---

# Takeaways

* The brute-force solution checks all pairs and runs in **O(n²)**.
* The optimal solution uses the **Two Pointers** technique to achieve **O(n)** time.
* Always move the pointer pointing to the shorter line because only doing so can potentially increase the container's height while sacrificing width.

---

## Related Problems

* Two Sum
* Trapping Rain Water
* Largest Rectangle in Histogram
* Longest Valid Parentheses

---

### Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • LeetCode Enthusiast
