# 🌳 Convert Sorted List to Binary Search Tree

![LeetCode](https://img.shields.io/badge/LeetCode-109-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Java-17%2B-red?style=flat-square\&logo=openjdk)
![Algorithm](https://img.shields.io/badge/Algorithm-Recursion-blue?style=flat-square)

## 📌 Overview

Given the head of a **sorted singly linked list**, convert it into a **height-balanced Binary Search Tree (BST)**.

A height-balanced BST keeps the heights of the left and right subtrees as close as possible.

### Example

```text
Input:
-10 → -3 → 0 → 5 → 9

Output:

        0
       / \
     -3   9
     /   /
   -10  5
```

---

## 🧠 Approach

The sorted order of the linked list allows us to construct the BST recursively.

1. Find the middle node using **slow and fast pointers**.
2. Use the middle node as the root.
3. Disconnect the left half from the middle.
4. Recursively convert the left half into the left subtree.
5. Recursively convert the right half into the right subtree.
6. Repeat until the list is empty.

The key idea is:

```text
Left half → Root → Right half
```

---

## 💻 Implementation

```java
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }

        if (head.next == null) {
            return new TreeNode(head.val);
        }

        ListNode prev = null;
        ListNode slow = head;
        ListNode fast = head;

        // Find the middle node
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // Disconnect the left half
        prev.next = null;

        // Create root from the middle node
        TreeNode root = new TreeNode(slow.val);

        root.left = sortedListToBST(head);
        root.right = sortedListToBST(slow.next);

        return root;
    }
}
```

---

## 🔍 Example Walkthrough

For:

```text
-10 → -3 → 0 → 5 → 9
```

The middle node is `0`.

```text
Left half:   -10 → -3
Root:        0
Right half:  5 → 9
```

Create `0` as the root and recursively process both halves.

```text
        0
       / \
     -3   9
     /   /
   -10  5
```

Each recursive call chooses the middle element of its current list segment.

---

## ⚠️ Edge Cases

| Case            | Input            | Output             | Behavior                             |
| --------------- | ---------------- | ------------------ | ------------------------------------ |
| Empty list      | `[]`             | `null`             | No tree is created                   |
| One node        | `[1]`            | `1`                | The only node becomes the root       |
| Two nodes       | `[1,3]`          | Root `3`, left `1` | Middle node is selected as root      |
| Three nodes     | `[1,2,3]`        | Root `2`           | Perfectly balanced tree              |
| Negative values | `[-3,-1,0]`      | Valid BST          | Negative values are handled normally |
| Mixed values    | `[-10,-3,0,5,9]` | Balanced BST       | Values remain in sorted BST order    |

---

## ⏱️ Complexity

* **Time:** `O(n log n)` for a balanced recursion tree.
* **Auxiliary Space:** `O(log n)` for the recursion stack.
* **Output Space:** `O(n)` for the created BST nodes.

Finding the middle requires traversing the current list segment, while recursion divides the list into smaller halves.

---

## 💡 Key Takeaways

* The middle element of a sorted sequence is a natural BST root.
* Slow/fast pointers efficiently locate the linked-list middle.
* Recursion converts the left and right halves independently.
* The resulting tree is height-balanced.
* No array conversion is required.

---

## 🔗 Related Problems

* **#108 — Convert Sorted Array to Binary Search Tree** → Similar problem using an array
* **#98 — Validate Binary Search Tree** → Validate BST properties
* **#100 — Same Tree** → Compare two binary trees
* **#104 — Maximum Depth of Binary Tree** → Analyze tree height
* **#206 — Reverse Linked List** → Linked-list pointer manipulation


## 📖 Reference

[LeetCode — Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

---

<div align="center">

⭐ **Sorted List → Middle Element → Balanced BST**

</div>
