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

		// Go as far left as possible
		for current != nil {
			stack = append(stack, current)
			current = current.Left
		}

		// Visit the node
		current = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		result = append(result, current.Val)

		// Move to the right subtree
		current = current.Right
	}

	return result
}