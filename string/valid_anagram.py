class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        create a dict with char as key, count as value and add s into the dict
        remove count of char from t, if key of char does not exist in dict, return False

        time complexity: O(2N) = O(N)
        space complexity: O(N)
        """
        char_dict: dict[str, int] = {}
        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1

        for c in t:
            if c not in char_dict:
                return False
            else:
                char_dict[c] -= 1
                if char_dict[c] == 0:
                    del char_dict[c]

        return len(char_dict) == 0

