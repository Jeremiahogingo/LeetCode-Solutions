class TrieNode:
    def __init__(self):
        self.children = {}
        self.best = -1


class Solution:

    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        def better(i, j):
            if j == -1:
                return True
            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return True
            if len(wordsContainer[i]) == len(wordsContainer[j]):
                return i < j
            return False

        for i, word in enumerate(wordsContainer):

            if better(i, root.best):
                root.best = i

            node = root

            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if better(i, node.best):
                    node.best = i

        ans = []

        for word in wordsQuery:

            node = root

            for ch in reversed(word):

                if ch not in node.children:
                    break

                node = node.children[ch]

            ans.append(node.best)

        return ans