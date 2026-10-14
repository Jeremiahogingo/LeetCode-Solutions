# 🔗 Reverse Linked List II

![LeetCode](https://img.shields.io/badge/LeetCode-92-orange?style=flat-square&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?style=flat-square&logo=go)
![Time](https://img.shields.io/badge/Time-O(n)-blue?style=flat-square)
![Space](https://img.shields.io/badge/Space-O(1)-blue?style=flat-square)

## Overview

Given the head of a singly linked list and two positions, `left` and `right`, reverse the nodes between those positions, inclusive.

The remaining nodes must retain their original relative order. The list should be modified in place.

### Example

```text
Input:
head = [1,2,3,4,5], left = 2, right = 4

Output:
[1,4,3,2,5]
```

## Approach

Use **in-place pointer manipulation** with a dummy node and head insertion.

1. **Create a dummy node:** Simplifies reversing a section that starts at the head.
2. **Find the preceding node:** Move `prev` to the node immediately before position `left`.
3. **Reverse the section:** Repeatedly move `current.Next` to the front of the selected section.
4. **Return the head:** Return `dummy.Next`, which points to the updated list.

The `prev` pointer stays fixed while nodes are moved to the front of the reversal section.

## Implementation

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val  int
 *     Next *ListNode
 * }
 */

func reverseBetween(head *ListNode, left int, right int) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy

    // Find the node before position left
    for i := 1; i < left; i++ {
        prev = prev.Next
    }

    current := prev.Next

    // Move each next node to the front of the section
    for i := 0; i < right-left; i++ {
        next := current.Next

        current.Next = next.Next
        next.Next = prev.Next
        prev.Next = next
    }

    return dummy.Next
}
```

## Example Walkthrough

For `head = [1,2,3,4,5]`, `left = 2`, and `right = 4`:

**Initial list**

```text
1 → 2 → 3 → 4 → 5
    ↑
  current
```

**Move node 3 before node 2**

```text
1 → 3 → 2 → 4 → 5
```

**Move node 4 before node 3**

```text
1 → 4 → 3 → 2 → 5
```

The selected section is reversed, while the rest of the list remains in order.

## Edge Cases

| Case | Input | Output |
|---|---|---|
| Single node | `[5]`, `left = 1`, `right = 1` | `[5]` |
| No reversal needed | `[1,2,3]`, `left = 2`, `right = 2` | `[1,2,3]` |
| Reverse entire list | `[1,2,3]`, `left = 1`, `right = 3` | `[3,2,1]` |
| Reverse from beginning | `[1,2,3,4]`, `left = 1`, `right = 2` | `[2,1,3,4]` |
| Reverse at the end | `[1,2,3,4]`, `left = 3`, `right = 4` | `[1,2,4,3]` |

## Complexity

Let \(n\) be the number of nodes in the list.

| Metric | Complexity |
|---|---|
| Time | **O(n)** |
| Auxiliary space | **O(1)** |

Each pointer moves through the list a bounded number of times, and no additional list or array is created.

## Visual Pointer-State Diagram

Example: `head = [1,2,3,4,5]`, `left = 2`, `right = 4`.

The goal is to reverse `2 → 3 → 4` while keeping `1` and `5` in their original relative positions.

### Initial pointer positions

```text
dummy → 1 → 2 → 3 → 4 → 5 → nil
         ↑   ↑
        prev current
```

- `prev` points to node `1`, immediately before the section being reversed.
- `current` points to node `2`, the first node in the section.
- `next` will point to the node moved to the front in each iteration.

### Iteration 1 — Move node 3 before node 2

Initially, `next = current.Next`, so `next` points to node `3`.

```text
Before:

dummy → 1 → 2 → 3 → 4 → 5 → nil
         ↑   ↑   ↑
        prev current next
```

Apply the pointer updates:

```go
current.Next = next.Next
next.Next = prev.Next
prev.Next = next
```

Result:

```text
dummy → 1 → 3 → 2 → 4 → 5 → nil
         ↑       ↑
        prev    current
```

**What changed?**

- `2.Next` now points to `4`.
- `3.Next` now points to `2`.
- `1.Next` now points to `3`.

Notice that `prev` and `current` stay where they are.

### Iteration 2 — Move node 4 before node 3

Now `next = current.Next`, so `next` points to node `4`.

```text
Before:

dummy → 1 → 3 → 2 → 4 → 5 → nil
         ↑       ↑   ↑
        prev    current next
```

Apply the same pointer updates:

```go
current.Next = next.Next
next.Next = prev.Next
prev.Next = next
```

Result:

```text
dummy → 1 → 4 → 3 → 2 → 5 → nil
         ↑           ↑
        prev        current
```

The selected section is now reversed.

### Final pointer state

```text
dummy → 1 → 4 → 3 → 2 → 5 → nil
```

The function returns `dummy.Next`, which points to node `1`, the head of the updated list.

## Pointer Update Summary

| Pointer update | Purpose |
|---|---|
| `next := current.Next` | Save the node to move |
| `current.Next = next.Next` | Remove `next` from its current position |
| `next.Next = prev.Next` | Insert `next` at the front of the section |
| `prev.Next = next` | Connect the preceding node to the moved node |

**Key insight:** `prev` and `current` remain fixed during the reversal loop. Each iteration moves the node after `current` to the front of the section, reversing the selected nodes one by one.

## Key Takeaways

- A dummy node simplifies edge cases at the head.
- Head insertion reverses a section without reversing the entire list.
- The original nodes are reused.
- The solution achieves linear time and constant auxiliary space.

## Related Problems

- [#206 — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [#25 — Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [#24 — Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [#143 — Reorder List](https://leetcode.com/problems/reorder-list/)

## Reference

[LeetCode — Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

---

<div align="center">

**Locate → Detach by Pointer Updates → Reverse In Place**

</div>