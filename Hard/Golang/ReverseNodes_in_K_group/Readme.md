# 25. Reverse Nodes in k-Group

<div align="center">

[![LeetCode](https://img.shields.io/badge/LeetCode-25-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/reverse-nodes-in-k-group/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problems/reverse-nodes-in-k-group/)
[![Go](https://img.shields.io/badge/Language-Go-00ADD8?style=for-the-badge\&logo=go\&logoColor=white)](https://go.dev/)
[![Technique](https://img.shields.io/badge/Technique-Linked%20List%20Manipulation-blue?style=for-the-badge)]
[![Space](https://img.shields.io/badge/Extra%20Space-O\(1\)-green?style=for-the-badge)]

### Reversing linked list nodes in fixed-size groups using iterative pointer manipulation.

</div>

---

## 📖 Overview

This problem is an advanced linked-list manipulation challenge.

Given a singly linked list and an integer `k`, the list must be processed in consecutive groups of exactly `k` nodes. Every complete group is reversed, while any remaining nodes that do not form a complete group are left unchanged.

The main challenge is not the reversal itself. The difficult part is safely managing pointers while:

* Detecting whether a complete group of `k` nodes exists.
* Reversing nodes without losing access to the rest of the list.
* Reconnecting the reversed group to the previous and next sections.
* Preserving incomplete groups.

The optimal solution performs all operations **in place** using constant extra space.

---

# 💡 Core Idea

The algorithm repeatedly processes the list using four important steps:

```text
Find a group of k nodes
        ↓
Is the group complete?
     ↙        ↘
   No          Yes
   ↓            ↓
 Stop        Reverse group
                 ↓
           Reconnect nodes
                 ↓
           Move to next group
```

For example:

```text
Input:

1 → 2 → 3 → 4 → 5

k = 2
```

The list is divided into:

```text
[1 → 2] [3 → 4] [5]
```

Reverse only the complete groups:

```text
2 → 1 → 4 → 3 → 5
```

The last node remains unchanged because it does not form a complete group of size `2`.

---

# 🧠 Key Insight

Before reversing a group, we must first verify that at least `k` nodes remain.

Consider:

```text
1 → 2 → 3 → 4 → 5
```

with:

```text
k = 3
```

The first group:

```text
1 → 2 → 3
```

contains exactly `3` nodes and can be reversed.

The remaining nodes:

```text
4 → 5
```

contain fewer than `3` nodes.

Therefore, they must remain unchanged:

```text
3 → 2 → 1 → 4 → 5
```

This check prevents accidentally reversing incomplete groups.

---

# 🧩 Pointer Strategy

The solution uses several pointers to safely manipulate the list.

## 1. Dummy Node

A dummy node is placed before the original head.

```text
dummy → 1 → 2 → 3 → 4 → 5
```

This simplifies reconnection, especially when the first group is reversed.

```go
dummy := &ListNode{Next: head}
```

---

## 2. `groupPrev`

This pointer represents the node immediately before the current group.

Initially:

```text
groupPrev
    ↓
dummy → 1 → 2 → 3 → 4 → 5
```

After reversing the first group, it moves to the end of that reversed group.

---

## 3. `kth`

The `kth` pointer identifies the last node of the current group.

For:

```text
1 → 2 → 3 → 4 → 5
```

and:

```text
k = 3
```

we find:

```text
1 → 2 → 3
        ↑
       kth
```

If no `kth` node exists, fewer than `k` nodes remain and the algorithm stops.

---

## 4. `groupNext`

Before reversing the group, we save the node immediately after it.

```text
1 → 2 → 3 → 4 → 5
        ↑   ↑
       kth groupNext
```

This pointer is important because it allows the reversed group to reconnect to the rest of the list.

---

# ⚙️ Algorithm

### Step 1 — Create a Dummy Node

The dummy node simplifies head manipulation.

```text
dummy → head
```

---

### Step 2 — Find the `k`th Node

Starting from `groupPrev`, move forward `k` positions.

```text
groupPrev → 1 → 2 → 3
                    ↑
                   kth
```

If the `k`th node does not exist:

```text
Fewer than k nodes remain
        ↓
Stop processing
```

---

### Step 3 — Save the Next Group

Store:

```go
groupNext := kth.Next
```

This preserves access to the remaining linked list.

---

### Step 4 — Reverse the Current Group

Use the standard iterative linked-list reversal technique.

Before:

```text
1 → 2 → 3 → 4
```

Reverse:

```text
3 → 2 → 1 → 4
```

The pointer reversal continues until the current pointer reaches `groupNext`.

---

### Step 5 — Reconnect the Group

After reversal:

```text
groupPrev → 1 → 2 → 3 → groupNext
```

becomes:

```text
groupPrev → 3 → 2 → 1 → groupNext
```

The old first node becomes the last node of the reversed group.

---

### Step 6 — Move to the Next Group

The old first node is now the tail of the reversed group.

Therefore:

```go
groupPrev = temp
```

The algorithm repeats until fewer than `k` nodes remain.

---

# 🧑‍💻 Go Solution

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseKGroup(head *ListNode, k int) *ListNode {
    // Dummy node simplifies handling changes to the head.
    dummy := &ListNode{
        Next: head,
    }

    // Points to the node before the current group.
    groupPrev := dummy

    for {
        // Find the kth node in the current group.
        kth := getKthNode(groupPrev, k)

        // If fewer than k nodes remain, leave them unchanged.
        if kth == nil {
            break
        }

        // Save the node after the current group.
        groupNext := kth.Next

        // Reverse the current group.
        prev := groupNext
        current := groupPrev.Next

        for current != groupNext {
            next := current.Next
            current.Next = prev
            prev = current
            current = next
        }

        // Reconnect the previous part of the list
        // to the reversed group.
        temp := groupPrev.Next
        groupPrev.Next = kth

        // Move groupPrev to the end of the reversed group.
        groupPrev = temp
    }

    return dummy.Next
}

// Returns the kth node after current.
// Returns nil if fewer than k nodes remain.
func getKthNode(current *ListNode, k int) *ListNode {
    for current != nil && k > 0 {
        current = current.Next
        k--
    }

    return current
}
```

---

# 🔍 Example Walkthrough

## Input

```text
head = [1, 2, 3, 4, 5]
k = 2
```

Initial list:

```text
1 → 2 → 3 → 4 → 5
```

---

### First Group

```text
[1 → 2]
```

Reverse:

```text
2 → 1
```

List:

```text
2 → 1 → 3 → 4 → 5
```

---

### Second Group

```text
[3 → 4]
```

Reverse:

```text
4 → 3
```

List:

```text
2 → 1 → 4 → 3 → 5
```

---

### Remaining Nodes

```text
[5]
```

Since:

```text
1 < k
```

the node remains unchanged.

### Output

```text
[2, 1, 4, 3, 5]
```

---

# 📊 Complexity Analysis

Let `n` be the number of nodes in the linked list.

| Complexity           | Value  |
| -------------------- | ------ |
| **Time Complexity**  | `O(n)` |
| **Space Complexity** | `O(1)` |

### Why `O(n)`?

Each node is processed a constant number of times:

* Once while checking groups.
* Once during reversal.

Therefore, the overall time complexity is linear.

### Why `O(1)` Space?

The algorithm uses only a fixed number of pointers:

```text
dummy
groupPrev
kth
groupNext
prev
current
next
```

No additional array, stack, or linked list proportional to the input size is created.

---

# 🔄 Approach Comparison

| Approach                       |   Time |    Extra Space | Notes                        |
| ------------------------------ | -----: | -------------: | ---------------------------- |
| Store nodes in an array        | `O(n)` |         `O(n)` | Easier but uses extra memory |
| Recursive reversal             | `O(n)` | `O(n/k)` stack | Elegant but uses call stack  |
| Iterative pointer manipulation | `O(n)` |         `O(1)` | **Optimal**                  |

The iterative solution is preferred because it satisfies the constant auxiliary-space requirement.

---

# ⚠️ Common Mistakes

## 1. Reversing an Incomplete Group

For:

```text
1 → 2 → 3 → 4 → 5
k = 3
```

Incorrect:

```text
3 → 2 → 1 → 5 → 4
```

Correct:

```text
3 → 2 → 1 → 4 → 5
```

Always verify that `k` nodes exist before reversing.

---

## 2. Losing the Remaining List

Before changing pointers, save:

```go
groupNext := kth.Next
```

Without this reference, the rest of the linked list may become disconnected.

---

## 3. Forgetting to Reconnect the Reversed Group

After reversing:

```text
groupPrev → reversed group
```

must be restored using:

```go
groupPrev.Next = kth
```

Otherwise, the reversed section will not connect correctly to the previous part of the list.

---

## 4. Moving `groupPrev` Incorrectly

After reversal, the original first node becomes the last node:

```text
Before:
1 → 2 → 3

After:
3 → 2 → 1
          ↑
      groupPrev
```

Therefore, `groupPrev` must move to that node before processing the next group.

---

# 🚀 Implementation Highlights

| Feature             | Description                    |
| ------------------- | ------------------------------ |
| **Language**        | Go                             |
| **Difficulty**      | Hard                           |
| **Category**        | Linked List                    |
| **Technique**       | Iterative Pointer Manipulation |
| **Pattern**         | Reverse in Fixed-Size Groups   |
| **Time Complexity** | `O(n)`                         |
| **Extra Space**     | `O(1)`                         |

---

# 🧠 Lessons Learned

## 1. Dummy Nodes Simplify Linked List Problems

A dummy node removes special cases involving changes to the head.

Instead of handling:

```text
What if the first node changes?
```

we always work with:

```text
dummy → head
```

This makes reconnection logic much simpler.

---

## 2. Always Preserve Important Pointers

Before modifying a linked list, identify the pointers that must be preserved.

In this problem:

```text
Current Group
      ↓
[1 → 2 → 3] → Remaining List
                 ↑
             groupNext
```

Saving `groupNext` prevents the remaining list from being lost.

---

## 3. Linked List Reversal Is a Reusable Pattern

The core reversal operation:

```go
next := current.Next
current.Next = prev
prev = current
current = next
```

appears in many linked-list problems.

Mastering this pattern makes it easier to solve problems involving:

* Full list reversal
* Partial reversal
* Group reversal
* Reversing sublists
* Palindrome linked lists
* Rotating linked lists

---

## 4. Verify Conditions Before Modifying Data

The algorithm follows an important principle:

```text
Validate
   ↓
Modify
   ↓
Reconnect
```

Before reversing, we first verify that a complete group exists.

This pattern is useful in many in-place algorithms where premature modification can corrupt the data structure.

---

# 🎯 Key Pattern

```text
       ┌─────────────────┐
       │ Find k Nodes    │
       └────────┬────────┘
                ↓
        ┌───────────────┐
        │ k Nodes Exist?│
        └───────┬───────┘
            No  │  Yes
                │
         ┌──────┴──────┐
         ↓             ↓
       Stop      Reverse Group
                      ↓
                Reconnect Nodes
                      ↓
                 Move Forward
                      ↓
                    Repeat
```

---

# 🔗 Related Concepts

* Linked Lists
* Pointer Manipulation
* In-Place Algorithms
* Dummy Nodes
* Iterative Reversal
* Recursive Reversal
* Fixed-Size Group Processing
* Constant Space Algorithms

---

# 🔗 Related LeetCode Problems

| #      | Problem                      | Difficulty | Main Concept       |
| ------ | ---------------------------- | ---------- | ------------------ |
| 206    | Reverse Linked List          | 🟢 Easy    | Basic Reversal     |
| 92     | Reverse Linked List II       | 🟡 Medium  | Partial Reversal   |
| 24     | Swap Nodes in Pairs          | 🟡 Medium  | Group Manipulation |
| 143    | Reorder List                 | 🟡 Medium  | Split + Reverse    |
| 234    | Palindrome Linked List       | 🟢 Easy    | Reverse Half       |
| **25** | **Reverse Nodes in k-Group** | 🔴 Hard    | **Group Reversal** |

---


---

# 📝 Notes

### Pattern: **Reverse a Linked List in Groups**

The key reusable strategy is:

```text
Locate the group
        ↓
Validate its size
        ↓
Preserve the next connection
        ↓
Reverse the group
        ↓
Reconnect
        ↓
Continue
```

A useful rule for linked-list problems is:

> **Never modify a pointer until you know which connections you still need to preserve.**

---

## 📚 Reference

[LeetCode 25 — Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/?utm_source=chatgpt.com)

---

<div align="center">

### 🧩 Problem #25

**Difficulty:** Hard 🔴
**Language:** Go
**Time Complexity:** `O(n)`
**Space Complexity:** `O(1)`

### 🔑 Pattern

**Find k Nodes → Reverse → Reconnect → Repeat**

⭐ *Keep solving. Keep learning. Keep improving.*

</div> 
