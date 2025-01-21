class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        approach:
        using a SET to check if char was repeated, 
        a SLIDING WINDOW with right pointer traversing rightwards left pointer moving rightwards if there is a duplicate, 
        and check if after deleting char in the new position of left pointer from set, does the char on right pointer still exists in set
        once after deleting the char from left pointer in set and does not exist in set anymore, thr right pointer will then continue moving right
        
        time complexity: O(N)
        space complexity: O(N)
        """
        char_set: set[str] = set()
        l: int = 0
        res: int = 0

        for r in range(len(s)):
            # if right pointer points to duplicate in input list
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            res = max(res, r-l+1)

        return res