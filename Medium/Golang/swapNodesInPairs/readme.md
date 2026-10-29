# LeetCode 24: Swap Nodes in Pairs

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?logo=go&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Linked%20List-blue)

## Problem Description

Given the head of a singly linked list, swap every two adjacent nodes and return the new head.

You must swap the actual nodes by changing their links, **not by modifying their values**.

**Problem link:** [LeetCode 24 — Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

## Approach: Iterative Pointer Manipulation

Use a dummy node and three pointers to swap adjacent nodes in place.

1. Create a dummy node pointing to the original head.
2. Use `prev` to track the node immediately before the current pair.
3. Identify the first and second nodes in the pair.
4. Update their `Next` pointers to reverse their order.
5. Connect `prev` to the second node and advance to the next pair.
6. Return `dummy.Next`, which points to the new head.

If fewer than two nodes remain, the loop stops and any remaining node stays in its original position.

## Go Solution

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val  int
 *     Next *ListNode
 * }
 */

func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy

    for prev.Next != nil && prev.Next.Next != nil {
        first := prev.Next
        second := first.Next

        first.Next = second.Next
        second.Next = first
        prev.Next = second

        prev = first
    }

    return dummy.Next
}
```

## Examples

**Example 1**

- Input: `head = [1,2,3,4]`
- Output: `[2,1,4,3]`
- Explanation: The pairs `(1,2)` and `(3,4)` are swapped.

**Example 2**

- Input: `head = []`
- Output: `[]`
- Explanation: An empty list requires no changes.

**Example 3**

- Input: `head = [1]`
- Output: `[1]`
- Explanation: There is no adjacent pair to swap.

**Example 4**

- Input: `head = [1,2,3]`
- Output: `[2,1,3]`
- Explanation: The first two nodes are swapped, and the final node remains unchanged.

## Complexity Analysis

Let \(n\) be the number of nodes in the linked list.

- **Time Complexity:** \(O(n)\) — each pair is processed once.
- **Auxiliary Space Complexity:** \(O(1)\) — only a constant number of pointers are used.

## Key Takeaways

- Use pointer manipulation to rearrange nodes without changing their values.
- A dummy node simplifies handling cases where the head changes.
- Save the relevant node references before updating links to avoid losing the rest of the list.
- Iterative swapping achieves constant auxiliary space.

## Related Problems

These problems build on linked-list pointer manipulation and node reordering.

| Problem | Difficulty | Connection |
|---|---|---|
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Reverse a linked list by changing pointers. |
| [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | Reverse a selected portion of a linked list. |
| [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Rearrange nodes in a specified order. |
| [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Reverse nodes in groups of a specified size. |

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── Golang/
        └── 24_Swap_Nodes_in_Pairs.go
```

## References

- [LeetCode Problem 24](https://leetcode.com/problems/swap-nodes-in-pairs/description/)
- [Go Documentation](https://go.dev/doc/)
