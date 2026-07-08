# 🌧️ 42. Trapping Rain Water

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Topics](https://img.shields.io/badge/Topics-Two%20Pointers%20%7C%20Dynamic%20Programming%20%7C%20Arrays-blue)

## 📖 Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water can be trapped after raining.

The goal is to determine the **total amount of rainwater** that can be stored between the bars.

> **LeetCode:** https://leetcode.com/problems/trapping-rain-water/

---

## 📝 Example

### Input

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

### Output

```text
6
```

### Explanation

After raining, water accumulates in the valleys formed between taller bars.

```
                █
        █~~~~~~█
        █~~█~~~██~█
    █~~~██~██~████
____██████████████
```

The total trapped rainwater is **6 units**.

---

# 💡 Intuition

For each position, the amount of water trapped depends on:

* The tallest bar to its **left**
* The tallest bar to its **right**

The water level is limited by the **shorter** of these two walls.

Mathematically,

```text
Water at index i =
min(MaxLeft, MaxRight) - height[i]
```

If this value is negative, no water is trapped.

---

# 🚀 Approaches

## Approach 1: Brute Force

For every bar:

* Find the tallest bar on its left.
* Find the tallest bar on its right.
* Compute the trapped water.

### Complexity

| Time  | Space |
| ----- | ----- |
| O(n²) | O(1)  |

Although simple, this approach repeatedly scans the array and is inefficient for large inputs.

---

## Approach 2: Prefix & Suffix Maximum Arrays

Precompute:

* `leftMax[i]` → Maximum height from the beginning up to index `i`.
* `rightMax[i]` → Maximum height from the end down to index `i`.

Then calculate:

```text
water += min(leftMax[i], rightMax[i]) - height[i]
```

### Complexity

| Time | Space |
| ---- | ----- |
| O(n) | O(n)  |

This avoids repeated scans by storing intermediate results.

---

## ⭐ Approach 3: Two Pointers (Optimal)

Instead of storing two additional arrays, maintain:

* Left pointer
* Right pointer
* Maximum height seen from the left
* Maximum height seen from the right

### Key Observation

If

```text
leftMax < rightMax
```

then the water trapped at the left pointer depends **only on `leftMax`**, because the right side is guaranteed to be tall enough.

Similarly,

if

```text
rightMax <= leftMax
```

the trapped water on the right side depends only on `rightMax`.

This allows the problem to be solved in **one pass** while using constant extra space.

---

# 🛠 Algorithm

1. Initialize two pointers:

   * `left = 0`
   * `right = n - 1`
2. Maintain:

   * `leftMax`
   * `rightMax`
3. While `left < right`

   * Update the maximum heights.
   * Calculate trapped water.
   * Move the appropriate pointer inward.
4. Return the accumulated water.

---

# 🐍 Python Solution

```python
class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        trapped_water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]

                right -= 1

        return trapped_water
```

---

# ☕ Java Solution

```java
class Solution {

    public int trap(int[] height) {

        int left = 0;
        int right = height.length - 1;

        int leftMax = 0;
        int rightMax = 0;

        int trappedWater = 0;

        while (left < right) {

            if (height[left] < height[right]) {

                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    trappedWater += leftMax - height[left];
                }

                left++;

            } else {

                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    trappedWater += rightMax - height[right];
                }

                right--;
            }
        }

        return trappedWater;
    }
}
```

---

# 📊 Complexity Analysis

| Approach               | Time     | Space    |
| ---------------------- | -------- | -------- |
| Brute Force            | O(n²)    | O(1)     |
| Prefix & Suffix Arrays | O(n)     | O(n)     |
| Two Pointers           | **O(n)** | **O(1)** |

---

# 🔑 Key Concepts

* Arrays
* Two Pointers
* Prefix Maximum
* Suffix Maximum
* Dynamic Programming (Prefix/Suffix Technique)
* Space Optimization

---

# 📚 What I Learned

* The amount of trapped water at any position depends on the **minimum** of the tallest bars on both sides.
* Prefix and suffix arrays reduce repeated computations from **O(n²)** to **O(n)**.
* The two-pointer technique further optimizes the solution by eliminating the need for extra arrays, achieving **O(n)** time and **O(1)** space.

---

# 🎯 Related Problems

* 11. Container With Most Water
* 84. Largest Rectangle in Histogram
* 85. Maximal Rectangle
* 42. Trapping Rain Water II
* 739. Daily Temperatures

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver
