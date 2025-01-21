class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Method 1: use 2 pointers and a dict of alphanumeric char, traverse to to center from left and right ends
        while left pointer not in dict, traverse right,
        while right pointer not in dict, traverse left
        if left!=right, return False
        else, traverse right for left pointer and traverse left right pointer
        time complexity: O(N), space complexity: O(1)
        Method 2: traverse from left to right of given list and return True using == [::-1]
        time complexity: O(N), space complexity: O(1)
        use isalnum() and lower()

        use the isalnum() built in lib bc this was written in C and thus, is sped up
        """
        new_s: str = ""

        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1] # this is as good as traversing from end to start backwards