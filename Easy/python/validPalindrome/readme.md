# LeetCode 125: Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic](https://img.shields.io/badge/Topic-Two%20Pointers-orange)

## Problem Description

Given a string `s`, determine whether it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

A palindrome reads the same forward and backward.

**Problem link:** [LeetCode 125 — Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

## Approach: Two Pointers

Use two pointers to compare characters from opposite ends of the string without creating a separate cleaned string.

1. Initialize `left` at the beginning and `right` at the end.
2. Skip non-alphanumeric characters from both ends.
3. Compare the remaining characters without considering case.
4. If the characters differ, return `False`.
5. Move both pointers inward and continue until they meet.

If all comparisons match, return `True`.

## Python Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

## Examples

**Example 1**

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `true`
- Explanation: Ignoring spaces, punctuation, and case produces `"amanaplanacanalpanama"`, which is a palindrome.

**Example 2**

- Input: `s = "race a car"`
- Output: `false`
- Explanation: After ignoring spaces and case, the string is `"raceacar"`, which is not a palindrome.

**Example 3**

- Input: `s = " "`
- Output: `true`
- Explanation: Removing non-alphanumeric characters produces an empty string, which is considered a palindrome.

## Complexity Analysis

Let \(n\) be the length of the input string.

- **Time Complexity:** \(O(n)\) — each character is examined at most a constant number of times.
- **Auxiliary Space Complexity:** \(O(1)\) — the algorithm uses two pointers and does not construct a filtered string.

## Key Takeaways

- Two pointers can compare elements from opposite ends efficiently.
- Python's `isalnum()` identifies alphanumeric characters.
- Python's `lower()` enables case-insensitive comparisons.
- Skipping irrelevant characters in place avoids allocating additional storage.

## References

- [LeetCode Problem 125](https://leetcode.com/problems/valid-palindrome/description/)
- [Python `str.isalnum()` Documentation](https://docs.python.org/3/library/stdtypes.html#str.isalnum)
- [Python `str.lower()` Documentation](https://docs.python.org/3/library/stdtypes.html#str.lower)
