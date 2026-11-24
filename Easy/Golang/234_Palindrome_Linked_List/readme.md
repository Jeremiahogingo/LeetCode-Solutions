# 234. Palindrome Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-Go-00ADD8)
![Topic](https://img.shields.io/badge/Topic-Linked%20List%20%7C%20Two%20Pointers-blue)

## Problem

**LeetCode:** [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Given the head of a singly linked list, determine whether the linked list is a palindrome.

A palindrome is a sequence that reads the same forward and backward.

Return `true` if the linked list is a palindrome; otherwise, return `false`.

## Approach: Fast and Slow Pointers + Reversing the Second Half

The optimal solution uses two pointers to locate the middle of the linked list, reverses the second half, and compares corresponding node values.

The original linked list is restored after the comparison.

### Algorithm

1. Handle edge cases: an empty list or a single-node list is automatically a palindrome.
2. Use slow and fast pointers to locate the middle of the linked list.
   - Slow moves one node at a time.
   - Fast moves two nodes at a time.
3. If the list has an odd number of nodes, skip the middle node.
4. Reverse the second half of the linked list.
5. Compare the first half with the reversed second half.
6. If any corresponding values differ, the list is not a palindrome.
7. Restore the original linked list by reversing the second half again.
8. Return the comparison result.

## Go Solution

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val  int
 *     Next *ListNode
 * }
 */

// Reverse a linked list in place.
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    current := head

    for current != nil {
        nextNode := current.Next
        current.Next = prev
        prev = current
        current = nextNode
    }

    return prev
}

func isPalindrome(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return true
    }

    // Step 1: Find the middle using slow and fast pointers.
    slow, fast := head, head

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    // For an odd-length list, skip the middle node.
    secondHalf := slow
    if fast != nil {
        secondHalf = slow.Next
    }

    // Step 2: Reverse the second half.
    reversed := reverseList(secondHalf)

    // Step 3: Compare both halves.
    left := head
    right := reversed
    isPal := true

    for right != nil {
        if left.Val != right.Val {
            isPal = false
            break
        }

        left = left.Next
        right = right.Next
    }

    // Step 4: Restore the original linked list.
    reverseList(reversed)

    return isPal
}
```

## Example Walkthrough

**Input:**

```text
head = [1, 2, 3, 2, 1]
```

### Step 1: Find the middle

The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time.

```text
1 → 2 → 3 → 2 → 1
        ↑
       slow
```

### Step 2: Separate and reverse the second half

Since the list has an odd number of nodes, the middle node (`3`) is skipped.

```text
First half:   1 → 2 → 3

Second half:  1 → 2
```

After reversing the second half:

```text
First half:   1 → 2 → 3
Second half:  1 → 2
```

### Step 3: Compare corresponding values

```text
First half:   1 → 2
              ↓   ↓
Second half:  1 → 2
```

All corresponding values match.

**Output:**

```text
true
```

## Complexity Analysis

Let `n` represent the number of nodes in the linked list.

| Complexity | Cost | Explanation |
|---|---|---|
| Time | O(n) | Finding the middle, reversing, comparing, and restoring |
| Auxiliary Space | O(1) | Uses a fixed number of pointers and variables |

The solution modifies the linked list temporarily but restores its original structure before returning.

## Alternative Approach: Using a Slice

Another approach is to copy all node values into a Go slice and compare values from opposite ends.

- Time Complexity: O(n)
- Space Complexity: O(n)

Although straightforward, this approach requires additional memory. Reversing the second half is more space-efficient.

## Key Concepts

- **Fast and Slow Pointers:** Efficiently locate the middle of a linked list.
- **Linked List Reversal:** Reverse node connections without allocating another list.
- **Two Pointers:** Compare corresponding values from two halves.
- **In-place Operations:** Modify a data structure using constant auxiliary space.
- **Pointer Restoration:** Restore the original structure after temporary modifications.

## Important Takeaways

1. Fast and slow pointers are useful for finding the middle of linked lists.
2. Reversing a linked list requires careful pointer manipulation.
3. An odd-length list requires skipping its middle node during comparison.
4. In-place algorithms can reduce auxiliary memory from O(n) to O(1).
5. Always consider whether the input structure should be restored after an operation.

## Repository Structure

```text
LeetCode-Solutions/
└── Easy/
    └── Go/
        └── 234_Palindrome_Linked_List.go
```

## References

- [LeetCode Problem 234](https://leetcode.com/problems/palindrome-linked-list/)
- [Go Documentation](https://go.dev/doc/)
- [Linked List Data Structure](https://en.wikipedia.org/wiki/Linked_list)

---

**Problem:** 234 — Palindrome Linked List  
**Difficulty:** Easy  
**Language:** Go  
**Topics:** Linked List, Two Pointers, Fast and Slow Pointers

**Author:** [Jeremiah Ogingo](https://github.com/Jeremiahogingo)