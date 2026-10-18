
func canJump(nums []int) bool {
	farthest := 0

	for i, jump := range nums {
		// Current position cannot be reached
		if i > farthest {
			return false
		}

		// Update the farthest reachable index
		if i+jump > farthest {
			farthest = i + jump
		}

		// The last index is reachable
		if farthest >= len(nums)-1 {
			return true
		}
	}

	return true
}
