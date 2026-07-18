class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        for i in range(len(strs[0])):

            char = strs[0][i]

            for word in strs[1:]:

                if i == len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]