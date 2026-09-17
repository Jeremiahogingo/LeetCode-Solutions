# 🔤 Length of Last Word

[![LeetCode](https://img.shields.io/badge/LeetCode-58-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/length-of-last-word/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=flat-square)](https://leetcode.com/problems/length-of-last-word/)
[![Language](https://img.shields.io/badge/Language-Java-orange?style=flat-square\&logo=openjdk)](https://www.java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-String%20Traversal-purple?style=flat-square)](https://leetcode.com/problems/length-of-last-word/)

## 📌 Overview

Given a string containing words separated by spaces, return the length of the **last word**.

A word is a maximal sequence of non-space characters.

### Example

```text
Input:
s = "Hello World"

Output:
5
```

---

## 💡 Approach

Scan the string **from right to left**.

1. Skip any trailing spaces.
2. Count characters until the next space or the beginning of the string.
3. Return the count.

This avoids creating arrays or additional strings with methods such as `split()`.

---

## 💻 Implementation

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int i = s.length() - 1;

        // Skip trailing spaces
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        int length = 0;

        // Count the last word
        while (i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }

        return length;
    }
}
```

---

## 🔍 Example Walkthrough

```text
Input:
"   fly me   to   the moon  "
```

Start from the end:

```text
"   fly me   to   the moon  "
                          ↑
                    skip spaces
                          ↓
"   fly me   to   the moon"
                         ↑
                    count backward
                         ↓
                       moon
```

```text
Length = 4
```

---

## ⚠️ Edge Cases

| Case                   | Input              | Output | Behavior                              |
| ---------------------- | ------------------ | -----: | ------------------------------------- |
| Empty string           | `""`               |    `0` | No characters to process; returns `0` |
| Trailing spaces        | `"Hello World  "`  |    `5` | Skips trailing spaces                 |
| Leading spaces         | `"  Hello"`        |    `5` | Counts the only word                  |
| Multiple spaces        | `"Hello   World"`  |    `5` | Stops at the space before `World`     |
| Single word            | `"LeetCode"`       |    `8` | Counts the entire string              |
| Single character       | `"a"`              |    `1` | Returns `1`                           |
| Word followed by space | `"a "`             |    `1` | Skips the trailing space              |
| Multiple words         | `"Today is great"` |    `5` | Counts `great`                        |

> **Note:** An empty string is outside LeetCode's stated constraints, but the implementation safely returns `0` for it.

---

## ⏱️ Complexity

Let `n` be the length of the string.

| Metric      | Complexity |
| ----------- | ---------- |
| Time        | `O(n)`     |
| Extra Space | `O(1)`     |

Each character is examined at most once, with no additional data structures.

---

## 🎯 Key Takeaways

* Traverse from **right to left**.
* Ignore trailing spaces first.
* Count until the next space.
* Avoid unnecessary `split()` and array creation.
* Achieve **linear time with constant extra space**.

### Key Pattern

```text
Start at the end
      ↓
Skip spaces
      ↓
Count characters
      ↓
Hit space / beginning
      ↓
Return count
```

---

## 🔗 Related Problems

| Problem                        | Difficulty | Concept             |
| ------------------------------ | ---------- | ------------------- |
| Reverse String #344            | Easy       | Two Pointers        |
| Valid Palindrome #125          | Easy       | String Traversal    |
| Reverse Words in a String #151 | Medium     | String Manipulation |
| String to Integer (atoi) #8    | Medium     | String Parsing      |

---
---

## 📖 Reference

* [LeetCode — Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
* [Java Documentation](https://docs.oracle.com/en/java/)

---

<p align="center">
  <b>LeetCode #58 • Length of Last Word</b>
  <br>
  String Traversal • Two Pointers • Java
</p>
