# 🔀 Reorder List

![LeetCode](https://img.shields.io/badge/LeetCode-143-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?style=flat-square\&logo=go)
![Complexity](https://img.shields.io/badge/Time-O\(n\)-blue?style=flat-square)
![Space](https://img.shields.io/badge/Space-O\(1\)-blue?style=flat-square)

## Overview

Given a singly linked list:

```text
L₀ → L₁ → L₂ → ... → Lₙ
```

Reorder it in the following form:

```text
L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → ...
```

The nodes must be rearranged **in place** without changing their values.

### Example

```text
Input:
1 → 2 → 3 → 4 → 5

Output:
1 → 5 → 2 → 4 → 3
```

---

## Approach

The solution consists of three steps:

### 1. Find the middle

Use the **slow and fast pointer** technique.

```text
1 → 2 → 3 → 4 → 5
        ↑
       slow
```

The `slow` pointer reaches the middle of the list.

### 2. Reverse the second half

Split the list at the middle and reverse the second half.

```text
First:   1 → 2 → 3

Second:  4 → 5
         ↓
         5 → 4
```

### 3. Merge the two halves

Take nodes alternately from each half:

```text
1 → 5 → 2 → 4 → 3
```

This produces the required ordering without creating another data structure.

---

## Implementation

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    if head == nil || head.Next == nil {
        return
    }

    // Find the middle of the list
    slow, fast := head, head

    for fast.Next != nil && fast.Next.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    // Split the list
    second := slow.Next
    slow.Next = nil

    // Reverse the second half
    var prev *ListNode

    for second != nil {
        next := second.Next
        second.Next = prev
        prev = second
        second = next
    }

    // Merge the two halves
    first := head
    second = prev

    for second != nil {
        firstNext := first.Next
        secondNext := second.Next

        first.Next = second
        second.Next = firstNext

        first = firstNext
        second = secondNext
    }
}
```

---

## Example Walkthrough

Consider:

```text
1 → 2 → 3 → 4 → 5 → 6
```

### Split

```text
First half:
1 → 2 → 3

Second half:
4 → 5 → 6
```

### Reverse second half

```text
First:   1 → 2 → 3
Second:  6 → 5 → 4
```

### Merge

Take one node from each half:

```text
1 → 6 → 2 → 5 → 3 → 4
```

The list is now reordered.

---

## Edge Cases

| Case        | Input           | Result          |
| ----------- | --------------- | --------------- |
| Empty list  | `[]`            | No change       |
| One node    | `[1]`           | `[1]`           |
| Two nodes   | `[1,2]`         | `[1,2]`         |
| Odd length  | `[1,2,3,4,5]`   | `[1,5,2,4,3]`   |
| Even length | `[1,2,3,4,5,6]` | `[1,6,2,5,3,4]` |

---

## Complexity

| Metric      | Complexity |
| ----------- | ---------- |
| Time        | **O(n)**   |
| Extra Space | **O(1)**   |

Each node is visited a constant number of times, and the list is modified directly without using an array or another linked list.

---

## Key Takeaways

* **Slow/fast pointers** find the midpoint.
* The second half is **reversed in place**.
* The two halves are **merged alternately**.
* The entire operation requires **O(n) time and O(1) extra space**.

---

## Related Problems

* **#206 — Reverse Linked List** — Reverse a linked list using pointers.
* **#21 — Merge Two Sorted Lists** — Merge linked lists using pointer manipulation.
* **#92 — Reverse Linked List II** — Reverse part of a linked list.
* **#876 — Middle of the Linked List** — Find the middle using slow/fast pointers.

## Reference

[LeetCode — Reorder List](https://leetcode.com/problems/reorder-list/)

---

<div align="center">

**Find Middle → Reverse → Merge**

</div>
