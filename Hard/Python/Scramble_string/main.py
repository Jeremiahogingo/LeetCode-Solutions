from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        @cache
        def dfs(i: int, j: int, length: int) -> bool:
            # Same substring means it is already a valid scramble.
            if s1[i:i + length] == s2[j:j + length]:
                return True

            # Quick pruning: both substrings must contain
            # exactly the same characters.
            if sorted(s1[i:i + length]) != sorted(s2[j:j + length]):
                return False

            # Try every possible split.
            for split in range(1, length):
                # Case 1: Do not swap.
                if (
                    dfs(i, j, split)
                    and dfs(
                        i + split,
                        j + split,
                        length - split
                    )
                ):
                    return True

                # Case 2: Swap the two parts.
                if (
                    dfs(
                        i,
                        j + length - split,
                        split
                    )
                    and dfs(
                        i + split,
                        j,
                        length - split
                    )
                ):
                    return True

            return False

        return dfs(0, 0, n)