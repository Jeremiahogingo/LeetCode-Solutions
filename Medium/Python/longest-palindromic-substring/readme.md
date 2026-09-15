# 🔄 Longest Palindromic Substring

[![LeetCode](https://img.shields.io/badge/LeetCode-5-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/longest-palindromic-substring/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)](https://leetcode.com/problems/longest-palindromic-substring/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square\&logo=python)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Expand%20Around%20Center-purple?style=flat-square)](https://leetcode.com/problems/longest-palindromic-substring/)

## 📌 Overview

**Longest Palindromic Substring** is a classic string-processing problem that requires finding the longest contiguous substring that reads identically from left to right and right to left.

A string is considered a **palindrome** when:

```text
s == reverse(s)
```

For example:

```text
"racecar" → Palindrome
"abba"    → Palindrome
"hello"   → Not a palindrome
```

The solution uses the **Expand Around Center** technique. Instead of generating every possible substring, we treat each character and each gap between characters as a possible palindrome center and expand outward while the characters match.

---

## 🧠 Core Idea

Every palindrome has a center.

There are two possible palindrome structures:

### Odd-Length Palindrome

Example:

```text
b a b
  ↑
center
```

The center is a single character.

We expand using:

```python
expand(i, i)
```

---

### Even-Length Palindrome

Example:

```text
a b b a
  ↑ ↑
center
```

The center lies between two characters.

We expand using:

```python
expand(i, i + 1)
```

Therefore, for every index `i`, we check both:

```text
Odd-length  → (i, i)
Even-length → (i, i + 1)
```

The longest palindrome found during the process becomes the answer.

---

## ⚙️ Algorithm

1. Handle strings containing fewer than two characters.
2. Maintain `start` and `end` to represent the longest palindrome found.
3. Define an `expand()` function that receives two pointers.
4. Expand outward while:

   * `left` remains inside the string.
   * `right` remains inside the string.
   * `s[left] == s[right]`.
5. Calculate the palindrome length after expansion.
6. For every character:

   * Check the odd-length palindrome.
   * Check the even-length palindrome.
7. Update the longest palindrome boundaries when a longer palindrome is found.
8. Return the substring between `start` and `end`.

---

## 💻 Implementation

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left: int, right: int) -> int:
            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            # Odd-length palindrome
            odd_length = expand(i, i)

            # Even-length palindrome
            even_length = expand(i, i + 1)

            max_length = max(odd_length, even_length)

            if max_length > end - start:
                start = i - (max_length - 1) // 2
                end = i + max_length // 2

        return s[start:end + 1]
```

---

## 🔍 Example Walkthrough

### Example 1

```text
Input:
s = "babad"
```

Consider `a` as the center:

```text
b a b
  ↑
```

Expanding outward:

```text
b == b
```

produces:

```text
"bab"
```

The algorithm continues checking the remaining centers and discovers another palindrome of the same maximum length:

```text
"aba"
```

Therefore, a valid output is:

```text
"bab"
```

or:

```text
"aba"
```

Both are accepted.

---

### Example 2

```text
Input:
s = "cbbd"
```

The longest palindrome is:

```text
c b b d
  ↑ ↑
```

The center lies between the two `b` characters.

Expanding outward produces:

```text
"bb"
```

Therefore:

```text
Output: "bb"
```

---

## 🔄 Expand Around Center

The main operation is:

```python
while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1
```

Consider:

```text
s = "racecar"
```

Starting from the middle:

```text
r a c e c a r
      ↑
```

Expansion proceeds as:

```text
e
```

then:

```text
c e c
```

then:

```text
a c e c a
```

then:

```text
r a c e c a r
```

The entire string is identified as a palindrome without generating any intermediate substrings.

---

## ⏱️ Complexity Analysis

| Metric          | Complexity |
| --------------- | ---------: |
| Time            |  **O(N²)** |
| Auxiliary Space |   **O(1)** |

### Time Complexity

There are `O(N)` possible centers.

For each center, expansion can take up to `O(N)` time.

Therefore:

```text
O(N) × O(N) = O(N²)
```

### Space Complexity

The algorithm only maintains a few integer variables and two pointers.

Therefore:

```text
O(1)
```

auxiliary space is used.

---

## 🚀 Why This Approach?

There are several possible approaches to this problem.

| Approach             |        Time |      Space | Notes                                          |
| -------------------- | ----------: | ---------: | ---------------------------------------------- |
| Brute Force          |     `O(N³)` |     `O(1)` | Generate and check every substring             |
| Dynamic Programming  |     `O(N²)` |    `O(N²)` | Efficient but uses significant memory          |
| Expand Around Center | **`O(N²)`** | **`O(1)`** | Excellent balance of simplicity and efficiency |
| Manacher's Algorithm |      `O(N)` |     `O(N)` | Optimal but considerably more complex          |

**Expand Around Center** is the preferred practical solution because it provides strong performance while remaining easy to understand and implement.

Manacher's algorithm is theoretically faster, but its complexity is unnecessary for the problem's constraints and makes the solution considerably harder to maintain.

---

## 💡 Implementation Highlights

### 1. Two Types of Centers

Checking only:

```python
expand(i, i)
```

would miss even-length palindromes such as:

```text
"abba"
```

Therefore, we also check:

```python
expand(i, i + 1)
```

---

### 2. No Substrings During Search

The algorithm doesn't repeatedly create strings while searching.

Instead, it stores only:

```python
start
end
```

and creates the final substring once:

```python
return s[start:end + 1]
```

---

### 3. Two-Pointer Expansion

The helper function uses two pointers:

```text
left ← center → right
```

When characters match, both pointers move outward.

```python
left -= 1
right += 1
```

The expansion stops as soon as the palindrome condition fails.

---

### 4. Tracking the Longest Result

After checking both palindrome types:

```python
max_length = max(odd_length, even_length)
```

the current palindrome is compared with the best result found so far.

---

## 📚 Lessons Learned

* Every palindrome can be analyzed around a center.
* Palindromes can have either one center character or a two-character center.
* Two-pointer expansion can eliminate the need for explicitly generating substrings.
* `O(N²)` time with `O(1)` auxiliary space is an excellent trade-off for this problem.
* Avoiding unnecessary substring creation improves both clarity and memory usage.
* The same center-expansion technique can be applied to other palindrome-related problems.
* Algorithm selection should consider not only theoretical performance but also implementation complexity.

---

## 🔑 Key Pattern

### Expand Around Center

```text
           Center
              ↓
        L ←   C   → R
              ↓
       Compare S[L] and S[R]
              ↓
          If equal
              ↓
       Expand both pointers
```

General implementation:

```python
def expand(left, right):
    while (
        left >= 0
        and right < len(s)
        and s[left] == s[right]
    ):
        left -= 1
        right += 1

    return right - left - 1
```

This pattern is particularly useful for:

* Palindrome detection
* Longest palindromic substring
* Counting palindromic substrings
* Center-based string problems

---

## 🧠 Related Concepts

* String Processing
* Two Pointers
* Expand Around Center
* Palindrome Detection
* Substrings
* Search Space Reduction
* Character Comparison
* Algorithm Optimization

---

## 🔗 Related LeetCode Problems

* [Palindrome Number — #9](https://leetcode.com/problems/palindrome-number/)
* [Valid Palindrome — #125](https://leetcode.com/problems/valid-palindrome/)
* [Palindromic Substrings — #647](https://leetcode.com/problems/palindromic-substrings/)
* [Palindrome Partitioning — #131](https://leetcode.com/problems/palindrome-partitioning/)
* [Longest Palindromic Subsequence — #516](https://leetcode.com/problems/longest-palindromic-subsequence/)

---

## 📝 Notes

* The problem asks for a **substring**, so the characters must be contiguous.
* A subsequence is different because its characters do not need to be adjacent.
* Both odd- and even-length palindromes must be checked.
* The `expand()` function performs the palindrome validation.
* `start` and `end` store the boundaries of the longest palindrome.
* If multiple palindromes have the same maximum length, any valid one may be returned.
* The solution uses **O(1) auxiliary space**.
* **Python** is the recommended language because it expresses the center-expansion technique clearly and concisely.

---

## 📖 Reference

* [LeetCode — Longest Palindromic Substring #5](https://leetcode.com/problems/longest-palindromic-substring/)
* [Python Documentation](https://docs.python.org/3/)

---
---

<div align="center">

### 🔄 Mastering Strings Through Symmetry

**LeetCode #5 • Medium • Python • Expand Around Center**

</div>
