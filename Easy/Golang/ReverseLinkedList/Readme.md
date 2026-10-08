# 🔄 Reverse Linked List

![LeetCode](https://img.shields.io/badge/LeetCode-206-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?style=flat-square\&logo=go)

## Overview

Given the head of a singly linked list, reverse the list and return its new head.

**Example:**

```text
Input:  1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1
```

## Approach

Use three pointers:

* `prev` — stores the previous node.
* `current` — stores the current node.
* `next` — temporarily stores the next node.

For each node, reverse its `Next` pointer and move forward.

```text
current.Next = prev
```

Continue until `current` becomes `nil`.

## Implementation

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    current := head

    for current != nil {
        next := current.Next
        current.Next = prev
        prev = current
        current = next
    }

    return prev
}
```

## Edge Cases

| Case           | Input       | Output      |
| -------------- | ----------- | ----------- |
| Empty list     | `[]`        | `[]`        |
| One node       | `[1]`       | `[1]`       |
| Two nodes      | `[1,2]`     | `[2,1]`     |
| Multiple nodes | `[1,2,3,4]` | `[4,3,2,1]` |

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

Each node is visited once, and the list is reversed in place.

## Key Takeaway

The iterative three-pointer technique reverses a linked list efficiently without creating additional nodes.

```

## Reference

[LeetCode — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
