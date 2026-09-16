# 🔗 Merge Two Sorted Lists

[![LeetCode](https://img.shields.io/badge/LeetCode-21-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/merge-two-sorted-lists/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=flat-square)](https://leetcode.com/problems/merge-two-sorted-lists/)
[![Language](https://img.shields.io/badge/Language-Java-orange?style=flat-square\&logo=openjdk)](https://www.java.com/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Two%20Pointers-purple?style=flat-square)](https://leetcode.com/problems/merge-two-sorted-lists/)

## 📌 Overview

Given two sorted linked lists, merge them into one sorted linked list by reusing the existing nodes.

### Example

```text
Input:
list1 = 1 → 2 → 4
list2 = 1 → 3 → 4

Output:
1 → 1 → 2 → 3 → 4 → 4
```

---

## 💡 Approach

Use an **iterative two-pointer approach**.

A dummy node provides a fixed starting point while `current` tracks the end of the merged list.

At each step:

1. Compare the current nodes of both lists.
2. Attach the smaller node to `current`.
3. Advance that list and `current`.
4. When one list ends, attach the remaining nodes from the other list.

The existing nodes are reused, so no additional list needs to be created.

---

## 💻 Implementation

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }

            current = current.next;
        }

        current.next = (list1 != null) ? list1 : list2;

        return dummy.next;
    }
}
```

---

## 🔍 Example Walkthrough

```text
list1: 1 → 2 → 4
list2: 1 → 3 → 4
```

Compare the current nodes:

```text
1 ≤ 1 → take list1
1 < 3 → take list1
2 < 3 → take list1
3 < 4 → take list2
```

The remaining nodes are then attached:

```text
1 → 1 → 2 → 3 → 4 → 4
```

---

## ⚠️ Edge Cases

| Case                               | Input                | Behavior                                      |
| ---------------------------------- | -------------------- | --------------------------------------------- |
| Both lists empty                   | `[]`, `[]`           | Returns `null`                                |
| First list empty                   | `[]`, `[1,2,3]`      | Returns `list2` unchanged                     |
| Second list empty                  | `[1,2,3]`, `[]`      | Returns `list1` unchanged                     |
| Single-node lists                  | `[1]`, `[2]`         | Produces `1 → 2`                              |
| Equal values                       | `[1,2]`, `[1,3]`     | Keeps both values; `list1` is chosen first    |
| All values in one list are smaller | `[1,2]`, `[5,6]`     | Appends remaining `list2`                     |
| All values in one list are larger  | `[5,6]`, `[1,2]`     | Appends remaining `list1`                     |
| Duplicate values                   | `[1,1,2]`, `[1,2,2]` | Preserves all duplicate nodes in sorted order |

The final line:

```java
current.next = (list1 != null) ? list1 : list2;
```

handles the cases where one list becomes empty before the other.

---

## ⏱️ Complexity

Let `n` and `m` be the lengths of the two lists.

| Metric      | Complexity |
| ----------- | ---------- |
| Time        | `O(n + m)` |
| Extra Space | `O(1)`     |

Each node is visited at most once, and the existing nodes are reused.

---

## 🎯 Key Takeaways

* Use **two pointers** to traverse both sorted lists.
* A **dummy node** simplifies list construction.
* Reuse existing nodes instead of creating another linked list.
* Attach the remaining list once either pointer reaches `null`.
* Handle empty lists before assuming both contain nodes.

### Key Pattern

```text
Compare
   ↓
Attach smaller node
   ↓
Advance pointer
   ↓
Repeat
   ↓
Attach remaining nodes
```

---

## 🔗 Related Problems

| Problem                                | Difficulty | Concept                 |
| -------------------------------------- | ---------- | ----------------------- |
| Merge k Sorted Lists #23               | Hard       | Heap / Divide & Conquer |
| Intersection of Two Linked Lists #160  | Easy       | Two Pointers            |
| Remove Duplicates from Sorted List #83 | Easy       | Linked List             |
| Merge Sorted Array #88                 | Easy       | Two Pointers            |

---
---

## 📖 Reference

* [LeetCode — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
* [Java Documentation](https://docs.oracle.com/en/java/)

---

<p align="center">
  <b>LeetCode #21 • Merge Two Sorted Lists</b>
  <br>
  Two Pointers • Linked List • Java
</p>
