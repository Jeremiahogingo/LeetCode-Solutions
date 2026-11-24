
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
