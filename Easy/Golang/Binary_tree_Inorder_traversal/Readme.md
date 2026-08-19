# 94. Binary Tree Inorder Traversal

<div align="center">

[![LeetCode](https://img.shields.io/badge/LeetCode-94-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/binary-tree-inorder-traversal/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/binary-tree-inorder-traversal/)
[![Go](https://img.shields.io/badge/Language-Go-00ADD8?style=for-the-badge\&logo=go\&logoColor=white)](https://go.dev/)
[![Technique](https://img.shields.io/badge/Technique-Iterative%20DFS-blue?style=for-the-badge)]
[![Data Structure](https://img.shields.io/badge/Data%20Structure-Stack-purple?style=for-the-badge)]

### Iterative inorder traversal using an explicit stack.

</div>

---

## 📖 Overview

Binary tree traversal is a fundamental concept in data structures and algorithms. This problem focuses on **inorder traversal**, where nodes must be visited in the following order:

```text
Left → Root → Right
```

The main challenge is maintaining the correct traversal order without using recursion.

While recursion provides a simple solution, this implementation uses an **explicit stack** to simulate the behavior of the recursive call stack.

The algorithm repeatedly:

1. Moves as far left as possible.
2. Stores nodes that still need to be processed.
3. Visits the most recently stored node.
4. Moves to its right subtree.
5. Repeats the process until every node has been visited.

---

# 💡 Core Idea

Inorder traversal follows this pattern:

```text
        Root
       /    \
     Left   Right
```

The correct visiting order is:

```text
Left
 ↓
Root
 ↓
Right
```

For example:

```text
        1
         \
          2
         /
        3
```

The inorder traversal is:

```text
[1, 3, 2]
```

The traversal sequence is:

```text
1 → move right
      ↓
      2
     /
    3

Visit order:

1 → 3 → 2
```

---

# 🧠 Why Use a Stack?

A recursive solution automatically uses the **function call stack** to remember nodes.

Conceptually, recursive inorder traversal looks like this:

```text
Traverse Left
      ↓
Visit Root
      ↓
Traverse Right
```

When implementing the traversal iteratively, we must manually remember the nodes that we need to return to.

A stack is ideal because it follows:

```text
Last In → First Out
```

The general pattern becomes:

```text
Move Left
    ↓
Push Nodes
    ↓
Reach nil
    ↓
Pop Node
    ↓
Visit Node
    ↓
Move Right
    ↓
Repeat
```

---

# ⚙️ Algorithm

## Step 1 — Initialize the Result and Stack

Create:

* `result` to store the traversal order.
* `stack` to store nodes that need to be processed.
* `current` to track the current node.

```go
result := []int{}
stack := []*TreeNode{}
current := root
```

---

## Step 2 — Move Left

Continue moving left until there are no more left children.

Each node is pushed onto the stack.

```go
for current != nil {
    stack = append(stack, current)
    current = current.Left
}
```

For this tree:

```text
        4
       /
      2
     /
    1
```

The stack becomes:

```text
[4, 2, 1]
```

---

## Step 3 — Pop and Visit

Once there are no more left nodes, the top node of the stack is the next node to visit.

```go
current = stack[len(stack)-1]
stack = stack[:len(stack)-1]

result = append(result, current.Val)
```

This ensures that all nodes in the left subtree are processed before the root.

---

## Step 4 — Move Right

After visiting a node, move to its right subtree.

```go
current = current.Right
```

The algorithm then repeats the same process.

---

# 🔄 Complete Traversal Pattern

```text
┌───────────────────────┐
│ current or stack exists│
└───────────┬───────────┘
            ↓
     Move Left as far
       as possible
            ↓
      Push each node
            ↓
       Reach nil?
            ↓
         Pop node
            ↓
        Visit node
            ↓
       Move Right
            ↓
          Repeat
```

---

# 🧑‍💻 Go Solution

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorderTraversal(root *TreeNode) []int {
    result := []int{}
    stack := []*TreeNode{}

    current := root

    for current != nil || len(stack) > 0 {

        // Move as far left as possible,
        // storing nodes we need to return to.
        for current != nil {
            stack = append(stack, current)
            current = current.Left
        }

        // Pop the next node to visit.
        current = stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        // Visit the node.
        result = append(result, current.Val)

        // Traverse the right subtree.
        current = current.Right
    }

    return result
}
```

---

# 🔍 Example Walkthrough

Consider:

```text
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

### Initial State

```text
current = 4
stack = []
result = []
```

### Move Left

```text
Push 4
Push 2
Push 1
```

Stack:

```text
[4, 2, 1]
```

### Pop and Visit

```text
Visit 1
```

Result:

```text
[1]
```

### Return to Parent

```text
Pop 2
Visit 2
```

Result:

```text
[1, 2]
```

### Traverse the Right Subtree

Move to:

```text
3
```

Visit:

```text
3
```

Result:

```text
[1, 2, 3]
```

The same process continues for the remaining nodes:

```text
4 → 5 → 6 → 7
```

Final result:

```text
[1, 2, 3, 4, 5, 6, 7]
```

---

# 📊 Complexity Analysis

Let `n` be the number of nodes and `h` be the height of the tree.

| Complexity           | Value  |
| -------------------- | ------ |
| **Time Complexity**  | `O(n)` |
| **Space Complexity** | `O(h)` |

### Why `O(n)` Time?

Each node is:

* Pushed onto the stack once.
* Popped from the stack once.
* Added to the result once.

Therefore, every node is processed a constant number of times.

```text
O(n)
```

### Why `O(h)` Space?

The stack stores nodes along the current path from the root toward a leaf.

In the worst case of a completely skewed tree:

```text
1
 \
  2
   \
    3
     \
      4
```

the stack can contain up to `n` nodes.

Therefore:

```text
Worst case: O(n)
Balanced tree: O(log n)
```

Generally, this is expressed as:

```text
O(h)
```

where `h` is the height of the tree.

> Note: The returned `result` array is typically not counted as auxiliary space.

---

# 🔄 Approach Comparison

| Approach         |   Time | Extra Space | Notes                                      |
| ---------------- | -----: | ----------: | ------------------------------------------ |
| Recursive DFS    | `O(n)` |      `O(h)` | Simple and readable                        |
| Iterative Stack  | `O(n)` |      `O(h)` | Explicit traversal control                 |
| Morris Traversal | `O(n)` |      `O(1)` | Advanced and temporarily modifies the tree |

The iterative stack approach provides a good balance between readability, control, and efficiency.

---

# ⚠️ Common Mistakes

## 1. Visiting the Root Too Early

This is **preorder** behavior:

```text
Root → Left → Right
```

Inorder traversal must be:

```text
Left → Root → Right
```

Always move left before visiting the current node.

---

## 2. Forgetting to Process the Right Subtree

After visiting a node:

```go
current = current.Right
```

Without this step, the right subtree would never be processed.

---

## 3. Incorrect Stack Pop

The correct way to remove the last element in Go is:

```go
current = stack[len(stack)-1]
stack = stack[:len(stack)-1]
```

The stack behaves as a **LIFO** data structure.

---

## 4. Stopping When `current == nil`

The traversal should continue as long as either:

```text
current != nil
```

or:

```text
the stack is not empty
```

Therefore:

```go
for current != nil || len(stack) > 0 {
    // traversal
}
```

Even when `current` becomes `nil`, there may still be nodes waiting in the stack.

---

# 🚀 Implementation Highlights

| Feature             | Description   |
| ------------------- | ------------- |
| **Language**        | Go            |
| **Difficulty**      | Easy          |
| **Category**        | Binary Tree   |
| **Technique**       | Iterative DFS |
| **Data Structure**  | Stack         |
| **Traversal**       | Inorder       |
| **Time Complexity** | `O(n)`        |
| **Extra Space**     | `O(h)`        |

---

# 🧠 Lessons Learned

## 1. Recursion Can Be Simulated With a Stack

Recursive tree traversal relies on the call stack.

The iterative approach makes that process explicit:

```text
Recursive Call Stack
        ↓
Explicit Stack
```

This technique is useful when recursion depth could become a problem or when more control over traversal is needed.

---

## 2. Tree Traversals Follow Reusable Patterns

The three major depth-first traversals differ mainly in **when the node is visited**.

### Preorder

```text
Root → Left → Right
```

### Inorder

```text
Left → Root → Right
```

### Postorder

```text
Left → Right → Root
```

Understanding these patterns makes it easier to solve more advanced tree problems.

---

## 3. The Stack Represents the Path Back

When moving down the left side of a tree, parent nodes are stored in the stack.

For example:

```text
        5
       /
      3
     /
    1
```

The stack remembers:

```text
[5, 3, 1]
```

After visiting `1`, the algorithm can return to `3`, and then eventually to `5`.

---

## 4. Iterative Traversal Provides More Control

Using an explicit stack allows you to:

* Pause traversal.
* Modify traversal behavior.
* Track additional node information.
* Avoid recursion depth limitations.
* Adapt the technique for more complex DFS problems.

---

# 🎯 Key Pattern

```text
Move Left
    ↓
Push Nodes
    ↓
Pop Node
    ↓
Visit Node
    ↓
Move Right
    ↓
Repeat
```

This is one of the most important iterative tree traversal patterns.

---

# 🔗 Related Concepts

* Binary Trees
* Depth-First Search
* Inorder Traversal
* Tree Traversal
* Stack
* Iterative Algorithms
* Recursive Algorithms
* Tree Height
* DFS Simulation

---

# 🔗 Related LeetCode Problems

| #      | Problem                           | Difficulty | Main Concept            |
| ------ | --------------------------------- | ---------- | ----------------------- |
| 144    | Binary Tree Preorder Traversal    | 🟢 Easy    | Root → Left → Right     |
| **94** | **Binary Tree Inorder Traversal** | 🟢 Easy    | **Left → Root → Right** |
| 145    | Binary Tree Postorder Traversal   | 🟢 Easy    | Left → Right → Root     |
| 102    | Binary Tree Level Order Traversal | 🟡 Medium  | BFS + Queue             |
| 104    | Maximum Depth of Binary Tree      | 🟢 Easy    | Tree DFS                |
| 226    | Invert Binary Tree                | 🟢 Easy    | Tree Traversal          |



# 📝 Notes

### Pattern: **Iterative Inorder Traversal**

The reusable pattern is:

```text
Go Left
   ↓
Push Nodes
   ↓
Reach nil
   ↓
Pop and Visit
   ↓
Go Right
   ↓
Repeat
```

A useful rule to remember is:

> **Push nodes while moving left. Pop a node only when there is no further left child to explore.**

This pattern can be adapted to many tree traversal and depth-first search problems.

---

## 📚 Reference

[LeetCode 94 — Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/?utm_source=chatgpt.com)

---

<div align="center">

### 🌳 Problem #94

**Difficulty:** Easy 🟢
**Language:** Go
**Time Complexity:** `O(n)`
**Space Complexity:** `O(h)`

### 🔑 Pattern

**Go Left → Push → Pop → Visit → Go Right**

⭐ *Keep solving. Keep learning. Keep improving.*

</div>
