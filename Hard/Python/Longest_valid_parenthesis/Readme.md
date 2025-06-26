🔍 Problem Description

You are given a string s composed solely of the characters '(' and ')'. Your task is to find the length of the longest substring that forms a valid (well-formed) parentheses sequence.

A valid parentheses substring must:

Consist of properly matched pairs of parentheses: every '(' has a corresponding ')',

And maintain correct nesting order (e.g., "(( ))" is valid, but "())(" is not).

📌 Example Cases

Example 1

Input: s = "(()"
Output: 2
Explanation: The longest valid substring is "()".

Example 2

Input: s = ")()())"
Output: 4
Explanation: The longest valid substring is "()()" 


🛠 Why It’s Challenging

Unlike simpler problems (e.g., checking if a string is valid), this one asks for the longest contiguous portion that’s valid. You can have parts that are unmatched and break up otherwise valid segments.

🚀 Common Approaches

Stack-Based Solution (O(n) time, O(n) space)

Use a stack to store indices.

Push -1 initially as a sentinel/base.

Traverse the string:

On '(': push its index.

On ')': pop from the stack.

If stack is empty after popping, push current index as new base.

Otherwise, compute current valid length = current index - top of stack, update max 


Dynamic Programming (O(n) time, O(n) space)

Use dp[i] to store the length of the longest valid substring ending at i.

For each ')' at i, check:

If s[i-1] == '(', then dp[i] = dp[i-2] + 2

Else, if the character before the last valid substring is '(', extend accordingly Q[i – dp[i – 1] – 1] == '('

Update max as you go