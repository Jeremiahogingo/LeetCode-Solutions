# 🌳 100. Same Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Topics](https://img.shields.io/badge/Topics-Trees%20%7C%20DFS%20%7C%20Recursion-blue)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow?logo=javascript)

## 📖 Overview

This problem asks us to determine whether two binary trees are **identical**.

Two trees are considered the same if:

* They have the same structure.
* Every corresponding node contains the same value.

The solution performs a simultaneous traversal of both trees, comparing nodes one pair at a time.

---

# 💡 Core Idea

Instead of comparing the trees level by level or converting them into arrays, we recursively compare corresponding nodes.

For every pair of nodes:

* If both are `null`, they match.
* If only one is `null`, the trees differ.
* If their values differ, the trees differ.
* Otherwise, recursively compare both left children and both right children.

The trees are identical only if **every recursive comparison succeeds**.

---

# 🌲 Data Structure

The solution operates on a **Binary Tree**.

Each node contains:

```text
TreeNode
├── val
├── left
└── right
```

The recursive algorithm naturally follows the tree's structure.

---

# ⚙️ Algorithm

1. If both nodes are `null`, return `true`.
2. If only one node is `null`, return `false`.
3. If the node values differ, return `false`.
4. Recursively compare:

   * Left subtree
   * Right subtree
5. Return `true` only if both recursive calls return `true`.

---

# 🟨 JavaScript Solution

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val)
 *     this.left = (left === undefined ? null : left)
 *     this.right = (right === undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {

    if (p === null && q === null) {
        return true;
    }

    if (p === null || q === null || p.val !== q.val) {
        return false;
    }

    return isSameTree(p.left, q.left) &&
           isSameTree(p.right, q.right);
};
```

---

# 📊 Example Walkthrough

Tree **P**

```text
    1
   / \
  2   3
```

Tree **Q**

```text
    1
   / \
  2   3
```

Comparison:

```text
1 == 1 ✅
│
├── 2 == 2 ✅
│
└── 3 == 3 ✅
```

Both trees have identical structure and values.

Result:

```text
true
```

---

Second Example

Tree **P**

```text
    1
   /
  2
```

Tree **Q**

```text
    1
     \
      2
```

Comparison:

```text
Left child exists only in P ❌
```

Result:

```text
false
```

---

# 📊 Complexity Analysis

| Metric | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(h)**   |

Where:

* **n** = Number of nodes
* **h** = Height of the tree

In the worst case (a skewed tree), the recursive call stack requires **O(n)** space.

---

# 🚀 Why This Solution Is Optimal

* Each node is visited exactly once.
* No additional data structures are required.
* The recursion stops immediately when a mismatch is found.
* The implementation is simple, readable, and commonly expected in coding interviews.

---

# 🎯 Key Concepts

* Binary Trees
* Depth-First Search (DFS)
* Recursion
* Tree Traversal
* Divide and Conquer

---

# 📚 Lessons Learned

* Comparing trees recursively mirrors their hierarchical structure.
* Base cases are essential for handling `null` nodes correctly.
* Recursive DFS often provides the cleanest solution for binary tree comparison problems.

---

# 🔗 Related Problems

* 101. Symmetric Tree
* 104. Maximum Depth of Binary Tree
* 226. Invert Binary Tree
* 572. Subtree of Another Tree
* 543. Diameter of Binary Tree

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver
