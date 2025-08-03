from typing import Optional


class TrieNode:
    def __init__(self, val: str, is_end: bool = False) -> None:
        self.val: str = val
        self.child: list[Optional["TrieNode"]] = [None] * 26
        self.is_end = is_end


class WordDictionary:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode("*")

    @staticmethod
    def _get_char_idx(char: str) -> int:
        return ord(char) - ord("a")

    def addWord(self, word: str) -> None:
        """
        iterate through input str, if child[idx] is None: create new Node
        -> traverse to child Node -> add is_end to end of word

        time complexity: O(N)
        space complexity: O(1)
        """
        curr: TrieNode = self.root
        for char in word:
            char_idx: int = WordDictionary._get_char_idx(char)
            if curr.child[char_idx] is None:
                curr.child[char_idx] = TrieNode(char)
            curr = curr.child[char_idx]
        curr.is_end = True

    def _dfs(self, idx: int, node: TrieNode, word: str) -> bool:
        # termination condition: when length of word==idx
        if idx == len(word):
            return node.is_end
        # case 1: when char == ".": iterate through its child and check if child == char
        char: str = word[idx]
        if char == ".":
            for child in node.child:
                if child and self._dfs(idx+1, child, word):
                    return True
                return False
        # case 2: when node.val == an alphabet
        # case 3: when node.val is None
        else:
            char_index = WordDictionary._get_char_idx(char)
            if node.child[char_index] is None:
                return False
            return self._dfs(idx+1, node.child[char_index], word)

    def search(self, word: str) -> bool:
        """
        DFS approach: search for node and return False if node does not exist
        termination condition: if length of word == idx
        """
        return self._dfs(0, self.root, word)

"""
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
                                      #
Output
[null,null,null,null,false,true,true,true]

self._dfs(0, *, bad)

[
self._dfs(
self._dfs(0, *, bad) , line 49
]

"""