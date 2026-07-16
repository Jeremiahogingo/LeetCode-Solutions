# 🔢 9. Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Topics](https://img.shields.io/badge/Topics-Math%20%7C%20Number%20Manipulation-blue)

## 📖 Problem Statement

Given an integer `x`, return **true** if `x` is a palindrome and **false** otherwise.

A palindrome is a number that reads the same forward and backward.

> **LeetCode:** https://leetcode.com/problems/palindrome-number/

---

# 📝 Examples

### Example 1

**Input**

```text
x = 121
```

**Output**

```text
true
```

**Explanation**

Reading the number from left to right and right to left gives the same result.

---

### Example 2

**Input**

```text
x = -121
```

**Output**

```text
false
```

**Explanation**

The negative sign appears only at the beginning, making it impossible for the number to be a palindrome.

---

### Example 3

**Input**

```text
x = 10
```

**Output**

```text
false
```

**Explanation**

Reversing the number gives `01`, which is `1`.

---

# 💡 Intuition

A straightforward solution is to convert the integer into a string and compare it with its reverse.

Although simple, this approach uses extra memory.

A more efficient solution reverses **only half of the number**.

### Key Observations

* Negative numbers are never palindromes.
* Numbers ending with `0` (except `0` itself) cannot be palindromes.
* We only need to reverse half of the digits because once the reversed half becomes greater than or equal to the remaining half, we've processed enough digits.

---

# 🚀 Optimal Approach — Reverse Half of the Number

Instead of reversing the entire number:

1. Reject invalid cases immediately.
2. Repeatedly move the last digit from the original number into a new reversed number.
3. Stop when the reversed half is greater than or equal to the remaining half.
4. Compare both halves.

For numbers with an odd number of digits, ignore the middle digit by dividing the reversed half by `10`.

---

# 🛠 Algorithm

1. If the number is negative, return `False`.
2. If the number ends with `0` but is not `0`, return `False`.
3. Initialize `reversed_half = 0`.
4. While `x > reversed_half`:

   * Remove the last digit from `x`.
   * Append it to `reversed_half`.
5. Return:

```text
x == reversed_half
```

or

```text
x == reversed_half // 10
```

to handle odd-length numbers.

---

# 🐍 Python Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
```

---

# ☕ Java Solution

```java
class Solution {

    public boolean isPalindrome(int x) {

        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversedHalf = 0;

        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        return x == reversedHalf || x == reversedHalf / 10;
    }
}
```

---

# 📊 Dry Run

Input

```text
x = 1221
```

| Remaining (`x`) | Reversed Half |
| --------------: | ------------: |
|            1221 |             0 |
|             122 |             1 |
|              12 |            12 |

Since

```text
x == reversed_half
```

Return

```text
true
```

---

Input

```text
x = 12321
```

| Remaining (`x`) | Reversed Half |
| --------------: | ------------: |
|           12321 |             0 |
|            1232 |             1 |
|             123 |            12 |
|              12 |           123 |

Now ignore the middle digit:

```text
123 // 10 = 12
```

Compare

```text
12 == 12
```

Return

```text
true
```

---

# 📊 Complexity Analysis

| Metric | Complexity     |
| ------ | -------------- |
| Time   | **O(log₁₀ n)** |
| Space  | **O(1)**       |

---

# 🔑 Key Concepts

* Mathematics
* Integer Manipulation
* Digit Extraction
* Reverse Number
* Constant Space Optimization

---

# 🎯 Edge Cases

* ✅ Negative numbers
* ✅ Single-digit numbers
* ✅ Numbers ending in zero
* ✅ Even number of digits
* ✅ Odd number of digits
* ✅ Zero itself

---

# 📚 What I Learned

* A palindrome can be verified without converting the number into a string.
* Reversing only half of the digits avoids unnecessary work and prevents integer overflow in many languages.
* Careful handling of odd-length numbers allows the algorithm to remain both simple and efficient.

---

# 🔗 Related Problems

* 7. Reverse Integer
* 66. Plus One
* 67. Add Binary
* 415. Add Strings

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver
# 🔢 9. Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Topics](https://img.shields.io/badge/Topics-Math%20%7C%20Number%20Manipulation-blue)

## 📖 Problem Statement

Given an integer `x`, return **true** if `x` is a palindrome and **false** otherwise.

A palindrome is a number that reads the same forward and backward.

> **LeetCode:** https://leetcode.com/problems/palindrome-number/

---

# 📝 Examples

### Example 1

**Input**

```text
x = 121
```

**Output**

```text
true
```

**Explanation**

Reading the number from left to right and right to left gives the same result.

---

### Example 2

**Input**

```text
x = -121
```

**Output**

```text
false
```

**Explanation**

The negative sign appears only at the beginning, making it impossible for the number to be a palindrome.

---

### Example 3

**Input**

```text
x = 10
```

**Output**

```text
false
```

**Explanation**

Reversing the number gives `01`, which is `1`.

---

# 💡 Intuition

A straightforward solution is to convert the integer into a string and compare it with its reverse.

Although simple, this approach uses extra memory.

A more efficient solution reverses **only half of the number**.

### Key Observations

* Negative numbers are never palindromes.
* Numbers ending with `0` (except `0` itself) cannot be palindromes.
* We only need to reverse half of the digits because once the reversed half becomes greater than or equal to the remaining half, we've processed enough digits.

---

# 🚀 Optimal Approach — Reverse Half of the Number

Instead of reversing the entire number:

1. Reject invalid cases immediately.
2. Repeatedly move the last digit from the original number into a new reversed number.
3. Stop when the reversed half is greater than or equal to the remaining half.
4. Compare both halves.

For numbers with an odd number of digits, ignore the middle digit by dividing the reversed half by `10`.

---

# 🛠 Algorithm

1. If the number is negative, return `False`.
2. If the number ends with `0` but is not `0`, return `False`.
3. Initialize `reversed_half = 0`.
4. While `x > reversed_half`:

   * Remove the last digit from `x`.
   * Append it to `reversed_half`.
5. Return:

```text
x == reversed_half
```

or

```text
x == reversed_half // 10
```

to handle odd-length numbers.

---

# 🐍 Python Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
```

---

# ☕ Java Solution

```java
class Solution {

    public boolean isPalindrome(int x) {

        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversedHalf = 0;

        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        return x == reversedHalf || x == reversedHalf / 10;
    }
}
```

---

# 📊 Dry Run

Input

```text
x = 1221
```

| Remaining (`x`) | Reversed Half |
| --------------: | ------------: |
|            1221 |             0 |
|             122 |             1 |
|              12 |            12 |

Since

```text
x == reversed_half
```

Return

```text
true
```

---

Input

```text
x = 12321
```

| Remaining (`x`) | Reversed Half |
| --------------: | ------------: |
|           12321 |             0 |
|            1232 |             1 |
|             123 |            12 |
|              12 |           123 |

Now ignore the middle digit:

```text
123 // 10 = 12
```

Compare

```text
12 == 12
```

Return

```text
true
```

---

# 📊 Complexity Analysis

| Metric | Complexity     |
| ------ | -------------- |
| Time   | **O(log₁₀ n)** |
| Space  | **O(1)**       |

---

# 🔑 Key Concepts

* Mathematics
* Integer Manipulation
* Digit Extraction
* Reverse Number
* Constant Space Optimization

---

# 🎯 Edge Cases

* ✅ Negative numbers
* ✅ Single-digit numbers
* ✅ Numbers ending in zero
* ✅ Even number of digits
* ✅ Odd number of digits
* ✅ Zero itself

---

# 📚 What I Learned

* A palindrome can be verified without converting the number into a string.
* Reversing only half of the digits avoids unnecessary work and prevents integer overflow in many languages.
* Careful handling of odd-length numbers allows the algorithm to remain both simple and efficient.

---

# 🔗 Related Problems

* 7. Reverse Integer
* 66. Plus One
* 67. Add Binary
* 415. Add Strings

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver