package reorderlist

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	// 1. Find the middle of the list
	slow, fast := head, head

	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// 2. Reverse the second half
	second := slow.Next
	slow.Next = nil

	var prev *ListNode

	for second != nil {
		next := second.Next
		second.Next = prev
		prev = second
		second = next
	}

	// 3. Merge the two halves
	first := head
	second = prev

	for second != nil {
		firstNext := first.Next
		secondNext := second.Next

		first.Next = second
		second.Next = firstNext

		first = firstNext
		second = secondNext
	}
}
