# √ Sqrt(x)

[![LeetCode](https://img.shields.io/badge/LeetCode-69-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/sqrtx/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=flat-square)](https://leetcode.com/problems/sqrtx/)
[![Language](https://img.shields.io/badge/Language-Java-orange?style=flat-square\&logo=openjdk)](https://www.java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Binary%20Search-purple?style=flat-square)](https://leetcode.com/problems/sqrtx/)

## 📌 Overview

Given a non-negative integer `x`, return the **integer square root** of `x`.

The result is the largest integer `r` such that:

```text
r² ≤ x
```

The decimal portion is discarded.

### Example

```text
Input:
x = 8

Output:
2

Explanation:
√8 ≈ 2.828
The integer square root is 2.
```

---

## 💡 Approach

Use **binary search** over the possible square-root values.

For each `mid`:

```text
mid² ≤ x
```

* If true, `mid` is a possible answer, so search to the right for a larger value.
* If false, `mid` is too large, so search to the left.

To prevent integer overflow, instead of calculating:

```java
mid * mid
```

check:

```java
mid <= x / mid
```

---

## 💻 Implementation

```java
class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 1;
        int right = x / 2;
        int answer = 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Avoid integer overflow
            if (mid <= x / mid) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return answer;
    }
}
```

---

## 🔍 Example Walkthrough

For:

```text
x = 8
```

The possible answer is between `1` and `4`.

```text
mid = 2
2² = 4 ≤ 8
```

So `2` is valid. Search for a larger value.

```text
mid = 3
3² = 9 > 8
```

So `3` is too large.

Therefore:

```text
answer = 2
```

---

## ⚠️ Edge Cases

| Case                        |        Input |  Output | Behavior                       |
| --------------------------- | -----------: | ------: | ------------------------------ |
| Zero                        |          `0` |     `0` | Returns immediately            |
| One                         |          `1` |     `1` | Returns immediately            |
| Non-perfect square          |          `8` |     `2` | Discards the decimal portion   |
| Perfect square              |         `16` |     `4` | Returns the exact root         |
| Smallest non-perfect square |          `2` |     `1` | Returns the floor of √2        |
| Large perfect square        | `2147395600` | `46340` | Handles large values safely    |
| Maximum `int`               | `2147483647` | `46340` | Avoids multiplication overflow |

---

## ⏱️ Complexity

| Metric      | Complexity |
| ----------- | ---------- |
| Time        | `O(log x)` |
| Extra Space | `O(1)`     |

Binary search eliminates roughly half of the remaining search space after every iteration.

---

## 🎯 Key Takeaways

* Use **binary search** to find the integer square root.
* Search for the largest value satisfying `mid² ≤ x`.
* Use `x / mid` instead of `mid * mid` to prevent integer overflow.
* Return the largest valid `mid` when `x` is not a perfect square.

### Key Pattern

```text
Search range
     ↓
Choose mid
     ↓
mid² ≤ x ?
  ↙       ↘
Yes       No
 ↓         ↓
Go right  Go left
     ↓
Largest valid value
```

---

## 🔗 Related Problems

| Problem                   | Difficulty | Concept               |
| ------------------------- | ---------- | --------------------- |
| Binary Search #704        | Easy       | Binary Search         |
| Valid Perfect Square #367 | Easy       | Binary Search         |
| Pow(x, n) #50             | Medium     | Binary Exponentiation |
| Find Peak Element #162    | Medium     | Binary Search         |

---

## 📁 Repository Structure

```text
Easy/
└── Java/
    └── Sqrt-x/
        ├── Solution.java
        └── README.md
```

---

## 📖 Reference

* [LeetCode — Sqrt(x)](https://leetcode.com/problems/sqrtx/)
* [Java Documentation](https://docs.oracle.com/en/java/)

---

<p align="center">
  <b>LeetCode #69 • Sqrt(x)</b>
  <br>
  Binary Search • Integer Arithmetic • Java
</p>
