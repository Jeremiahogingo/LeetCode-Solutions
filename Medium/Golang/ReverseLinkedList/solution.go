
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

	// Move prev to the node before position left
	for i := 1; i < left; i++ {
		prev = prev.Next
	}

	// First node of the section being reversed
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
