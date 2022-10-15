from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach: Create hashmap with alphabet as key, number of occurences as value of array 1. Iterate through array 2, if
        note: import of defaultdicts contianer from collections dictionary

        Time complexity: O(2S+T)
        Space Complexity: O(S)
        """
        # if lengths of string are not the same, it is not an anagram - fastest way to determine a non-anagram
        if len(s) != len(t):
            return False

        # create a dictionary where default value will be zero for that key instead of an error thrown
        hash_map = defaultdict(lambda: 0)

        for char in s:
            hash_map[char] += 1
        for char in t:
            if hash_map[char] == 0:
                return False
            hash_map[char] -= 1

        for char in hash_map.values():
            if char != 0:
                return False

        return True