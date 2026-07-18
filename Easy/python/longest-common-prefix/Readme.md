# 📝 14. Longest Common Prefix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Topics](https://img.shields.io/badge/Topics-Strings%20%7C%20Trie-blue)

## 📖 Problem Statement

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

> **LeetCode:** https://leetcode.com/problems/longest-common-prefix/

---

# 📝 Examples

## Example 1

### Input

```text
strs = ["flower","flow","flight"]
```

### Output

```text
"fl"
```

### Explanation

All strings begin with **"fl"**, making it the longest common prefix.

---

## Example 2

### Input

```text
strs = ["dog","racecar","car"]
```

### Output

```text
""
```

### Explanation

There is no common prefix shared by all strings.

---

# 💡 Intuition

The common prefix can only be as long as the shortest string.

Instead of comparing every pair of strings, compare characters **column by column**.

For each character position:

* Compare the character in the first string with the corresponding character in every other string.
* If any string differs or ends, return everything before that position.

This method is known as **Vertical Scanning**.

---

# 🚀 Approach — Vertical Scanning

Assume the first string is the reference.

```
flower
flow
flight
```

Compare one column at a time.

```
f == f == f ✅

l == l == l ✅

o == o == i ❌
```

Stop immediately.

Return

```
fl
```

Since the mismatch occurs at index `2`.

---

# 🛠 Algorithm

1. If the array is empty, return an empty string.
2. Traverse every character in the first string.
3. Compare that character with the same position in every other string.
4. If:

   * a string ends, or
   * characters differ,
     return the prefix found so far.
5. If every character matches, return the first string.

---

# 🐍 Python Solution

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        for i in range(len(strs[0])):

            current = strs[0][i]

            for word in strs[1:]:

                if i == len(word) or word[i] != current:
                    return strs[0][:i]

        return strs[0]
```

---

# ☕ Java Solution

```java
class Solution {

    public String longestCommonPrefix(String[] strs) {

        if (strs == null || strs.length == 0)
            return "";

        for (int i = 0; i < strs[0].length(); i++) {

            char current = strs[0].charAt(i);

            for (int j = 1; j < strs.length; j++) {

                if (i == strs[j].length() ||
                    strs[j].charAt(i) != current) {

                    return strs[0].substring(0, i);
                }
            }
        }

        return strs[0];
    }
}
```

---

# 📊 Dry Run

Input

```text
["flower","flow","flight"]
```

### Step 1

Compare index **0**

```
f
f
f
```

Match ✅

---

### Step 2

Compare index **1**

```
l
l
l
```

Match ✅

---

### Step 3

Compare index **2**

```
o
o
i
```

Mismatch ❌

Return

```
"fl"
```

---

# 📊 Complexity Analysis

| Metric | Complexity   |
| ------ | ------------ |
| Time   | **O(n × m)** |
| Space  | **O(1)**     |

Where:

* **n** = Number of strings
* **m** = Length of the shortest string

---

# 🔑 Key Concepts

* Strings
* Vertical Scanning
* Character Comparison
* Prefix Matching
* Early Termination

---

# 🎯 Edge Cases

* ✅ Empty array
* ✅ Single string
* ✅ No common prefix
* ✅ One string is a prefix of another
* ✅ All strings are identical

---

# 📚 Alternative Approaches

| Approach            | Time                | Space               |
| ------------------- | ------------------- | ------------------- |
| Vertical Scanning   | **O(n × m)**        | **O(1)**            |
| Horizontal Scanning | O(n × m)            | O(1)                |
| Divide & Conquer    | O(n × m)            | O(log n)            |
| Binary Search       | O(n × m × log m)    | O(1)                |
| Trie                | O(total characters) | O(total characters) |

The **Vertical Scanning** approach is generally preferred for interviews because it is simple, efficient, and uses constant extra space.

---

# 📚 What I Learned

* Comparing characters column by column avoids unnecessary string operations.
* Early termination makes the algorithm efficient in practice.
* The longest common prefix cannot exceed the length of the shortest string.

---

# 🔗 Related Problems

* 28. Find the Index of the First Occurrence in a String
* 58. Length of Last Word
* 125. Valid Palindrome
* 211. Design Add and Search Words Data Structure

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver
