/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseKGroup(head *ListNode, k int) *ListNode {
    // Dummy node helps handle changes to the head.
    dummy := &ListNode{
        Next: head,
    }

    // groupPrev points to the node before the current group.
    groupPrev := dummy

    for {
        // Step 1: Find the kth node from groupPrev.
        kth := getKthNode(groupPrev, k)

        // Fewer than k nodes remain, so leave them unchanged.
        if kth == nil {
            break
        }

        // The node immediately after the current group.
        groupNext := kth.Next

        // Step 2: Reverse the current group.
        prev := groupNext
        current := groupPrev.Next

        for current != groupNext {
            next := current.Next
            current.Next = prev
            prev = current
            current = next
        }

        // Step 3: Reconnect the reversed group.
        temp := groupPrev.Next
        groupPrev.Next = kth

        // Move to the end of the reversed group.
        groupPrev = temp
    }

    return dummy.Next
}

// Returns the kth node after the given node.
// Returns nil if fewer than k nodes remain.
func getKthNode(current *ListNode, k int) *ListNode {
    for current != nil && k > 0 {
        current = current.Next
        k--
    }

    return current
}