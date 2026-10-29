package rotateimage

func rotate(matrix [][]int) {
	n := len(matrix)

	// Step 1: Transpose the matrix.
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			matrix[i][j], matrix[j][i] =
				matrix[j][i], matrix[i][j]
		}
	}

	// Step 2: Reverse each row.
	for i := 0; i < n; i++ {
		for left, right := 0, n-1; left < right; left, right = left+1, right-1 {
			matrix[i][left], matrix[i][right] =
				matrix[i][right], matrix[i][left]
		}
	}
}
