<div align="center">

# 🌳 Longest Common Suffix Queries

[![LeetCode](https://img.shields.io/badge/LeetCode-3093-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/longest-common-suffix-queries/)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)
![Language](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Data Structure](https://img.shields.io/badge/Data%20Structure-Trie-blue?style=for-the-badge)
![Algorithm](https://img.shields.io/badge/Algorithm-String%20Processing-success?style=for-the-badge)

**A Trie-based solution for efficiently answering longest common suffix queries.**

</div>

---

# 📖 Overview

This project demonstrates an efficient solution to a challenging string-processing problem using a **Trie (Prefix Tree)**.

Rather than comparing every query against every candidate string, the solution preprocesses the input into a searchable data structure that allows each query to be answered in linear time with respect to its own length.

The implementation also incorporates custom tie-breaking rules by maintaining metadata within each Trie node, eliminating the need for additional processing during queries.

---

# 💡 Core Idea

A Trie is naturally designed for **prefix matching**, not suffix matching.

The key observation is that reversing every string transforms:

```text
Common Suffix
```

into

```text
Common Prefix
```

For example,

```text
Original

container : abcd
query     : cd
```

After reversing,

```text
dcba
dc
```

The problem becomes finding the **longest common prefix**, which can be solved efficiently using a Trie.

---

# 🌳 Data Structure

Each Trie node stores two pieces of information:

* **Children**

  * References to the next characters.

* **Best Candidate**

  * The index of the optimal string passing through that node according to the required tie-breaking criteria.

By storing this information during construction, each query can immediately retrieve the correct answer without revisiting previously inserted words.

---

# ⚙️ Algorithm

### 1. Preprocessing

* Reverse every string.
* Insert each reversed string into the Trie.
* Update the "best candidate" stored at every visited node.

### 2. Query Processing

* Reverse the query string.
* Traverse the Trie character by character.
* Stop when no further match exists.
* Return the candidate stored at the deepest matched node.

This strategy avoids repeatedly comparing every query against every stored string.

---

# 📊 Complexity Analysis

Let:

* **N** = Total number of characters in all container strings
* **M** = Total number of characters in all query strings

| Operation       | Complexity   |
| --------------- | ------------ |
| Build Trie      | **O(N)**     |
| Process Queries | **O(M)**     |
| Overall         | **O(N + M)** |

### Space Complexity

```text
O(N)
```

The Trie contains at most one node for every inserted character.

---

# 🚀 Implementation Highlights

* Reverse-string transformation simplifies suffix matching.
* Trie enables efficient prefix traversal.
* Metadata stored at every node removes the need for post-processing.
* Constant-time tie-breaking during insertion.
* Linear overall complexity with respect to the total input size.

---

# 📚 Lessons Learned

This solution highlights several important algorithmic techniques:

* Transforming a difficult problem into a familiar one.
* Choosing the appropriate data structure for efficient lookup.
* Storing auxiliary information to reduce query-time work.
* Designing algorithms that satisfy multiple ordering constraints without additional sorting.

It also demonstrates how preprocessing can dramatically reduce the cost of repeated queries.

---

# 🧠 Related Concepts

* Trie (Prefix Tree)
* String Manipulation
* Prefix Matching
* Suffix Matching
* Reverse String Technique
* Offline Query Processing
* Metadata Propagation
* Greedy Tie-Breaking
* Time-Space Tradeoffs

---

# 🔗 References

* **LeetCode Problem:** https://leetcode.com/problems/longest-common-suffix-queries/
* **Trie Data Structure:** https://en.wikipedia.org/wiki/Trie
* **Python Documentation:** https://docs.python.org/3/

---

<div align="center">

### ⭐ If you found this implementation helpful, consider starring the repository.

*"The best algorithm isn't always the most complex—it's often the one that transforms the problem into something you've already solved."*

</div>
