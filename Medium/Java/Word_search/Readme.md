🔍 Problem Summary
You're given:

A 2D grid of characters board.

A string word.


Goal: Determine if word exists in the grid.


Rules:

You can move horizontally or vertically to adjacent cells.

You cannot use the same cell more than once in a word.


🧠 Approach: Depth-First Search (DFS) with Backtracking
The idea is to explore all possible paths in the grid that could form the given word.

Steps:

Iterate through each cell in the grid.

If a cell matches the first character of word, initiate a DFS from that cell.

In DFS:

Check boundaries and if the current cell matches the corresponding character in word.

Mark the cell as visited to avoid revisiting.

Recursively explore adjacent cells (up, down, left, right).

Backtrack by unmarking the cell after exploration