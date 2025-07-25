from typing import Optional


class TrieNode:
    def __init__(self, val: str, is_end: bool = False) -> None:
        self.val = val
        self.child: list[Optional["TrieNode"]] = [None] * 26
        self.is_end: bool = is_end


class Trie:

    def __init__(self) -> None:
        self.head: TrieNode = TrieNode("*")

    @staticmethod
    def _get_char_index(char: str) -> int:
        """
        given a char, return its asci value
        """
        return ord(char) - ord("a")

    def insert(self, word: str) -> None:
        """
        iterate through word and input each char into Trie while checking if child exists for each TrieNode:
        a. if child w that TrieNode exists, move on to next TrieNode
        b. if child w that TrieNode does not exist, create that TrieNode
        """
        curr: TrieNode = self.head
        for char in word:
            char_index: int = Trie._get_char_index(char)
            if curr.child[char_index] is None:
                to_insert: TrieNode = TrieNode(char)
                curr.child[char_index] = to_insert
            curr = curr.child[char_index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """
        dfs recursion to recurse through child nodes to search for characters
        -> if last char of word .is_end is False: return False

        Possible cases
        1. node.child[char_index] is not None -> recurse to next node
        2. node.child[char_index] is None -> return False

        """
        curr: TrieNode = self.head
        for char in word:
            char_index: int = Trie._get_char_index(char)
            if curr.child[char_index] is None:
                return False
            curr = curr.child[char_index]
        if curr.is_end is False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        similar to search method above, but without the check for .is_end
        """
        curr: TrieNode = self.head
        for char in prefix:
            char_index: int = Trie._get_char_index(char)
            if curr.child[char_index] is None:
                return False
            curr = curr.child[char_index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)