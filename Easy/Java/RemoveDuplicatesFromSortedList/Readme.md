# 🔗 Remove Duplicates from Sorted List

![LeetCode](https://img.shields.io/badge/LeetCode-83-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Java-17%2B-red?style=flat-square\&logo=openjdk)
![Algorithm](https://img.shields.io/badge/Algorithm-Two%20Pointers-blue?style=flat-square)

## 📌 Overview

Given the head of a **sorted linked list**, remove all duplicate values so that every value appears only once.

The list must remain sorted.

### Example

```text
Input:
1 → 1 → 2 → 3 → 3

Output:
1 → 2 → 3
```

---

## 🧠 Approach

Because the linked list is already sorted, duplicate values will always appear next to each other.

Use a single pointer, `current`:

1. Start at the head.
2. Compare `current.val` with `current.next.val`.
3. If they are equal, skip the duplicate node.
4. Otherwise, move `current` forward.
5. Continue until the end of the list.

The duplicate is removed using:

```java
current.next = current.next.next;
```

This reuses the existing nodes instead of creating a new list.

---

## 💻 Implementation

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode current = head;

        while (current.next != null) {
            if (current.val == current.next.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}
```

---

## 🔍 Example Walkthrough

For:

```text
1 → 1 → 2 → 3 → 3
```

### Step 1

```text
1 → 1 → 2 → 3 → 3
↑   ↑
current
```

`1 == 1`, so skip the second `1`.

```text
1 → 2 → 3 → 3
```

### Step 2

`1 != 2`, so move forward.

```text
1 → 2 → 3 → 3
    ↑
  current
```

Continue until another duplicate is found.

```text
1 → 2 → 3 → 3
        ↑   ↑
```

`3 == 3`, so skip the second `3`.

Final result:

```text
1 → 2 → 3
```

---

## ⚠️ Edge Cases

| Case                      | Input           | Output    | Behavior                                    |
| ------------------------- | --------------- | --------- | ------------------------------------------- |
| Empty list                | `[]`            | `[]`      | Returns `null`                              |
| One node                  | `[1]`           | `[1]`     | No duplicate to remove                      |
| No duplicates             | `[1,2,3]`       | `[1,2,3]` | List remains unchanged                      |
| Two identical nodes       | `[1,1]`         | `[1]`     | Second node is removed                      |
| All duplicates            | `[2,2,2,2]`     | `[2]`     | All duplicates are removed                  |
| Duplicates at beginning   | `[1,1,2,3]`     | `[1,2,3]` | Consecutive duplicates are skipped          |
| Duplicates at end         | `[1,2,3,3]`     | `[1,2,3]` | Final duplicate is removed                  |
| Multiple duplicate groups | `[1,1,2,2,3,3]` | `[1,2,3]` | Each duplicate group is reduced to one node |

---

## ⏱️ Complexity

* **Time:** `O(n)` — each node is visited at most once.
* **Auxiliary Space:** `O(1)` — only one pointer is used.
* **Output Space:** `O(1)` — the existing linked list is modified in place.

---

## 💡 Key Takeaways

* A sorted list places duplicates next to each other.
* One pointer is enough to solve the problem.
* `current.next = current.next.next` removes a duplicate in place.
* No additional data structure is required.
* The original list nodes are reused.

---

## 🔗 Related Problems

* **#21 — Merge Two Sorted Lists** → Merge sorted linked lists
* **#82 — Remove Duplicates from Sorted List II** → Remove all values that appear more than once
* **#141 — Linked List Cycle** → Linked-list pointer traversal
* **#206 — Reverse Linked List** → Basic linked-list manipulation


## 📖 Reference

[LeetCode — Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

---

<div align="center">

⭐ **Sorted List + Pointer Traversal = O(n) Time, O(1) Space**

</div>
