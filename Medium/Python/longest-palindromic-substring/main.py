class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0

        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            # Odd-length palindrome
            odd_length = expand(i, i)

            # Even-length palindrome
            even_length = expand(i, i + 1)

            max_length = max(odd_length, even_length)

            if max_length > end - start:
                start = i - (max_length - 1) // 2
                end = i + max_length // 2

        return s[start:end + 1]