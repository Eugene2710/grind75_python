class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Approach: 2 pointers - 1 from left, 1 from right. If left pointer != right pointer, not palindrome. Stop when index of left pointer >= right pointer.
        Note: to resolve the issue of non-alphanumeric characters, write a function using ord() method

        Time Complexity: O(N)
        Space Complexity: O(N)

        """
        l: int = 0
        r: int = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c: str) -> bool:
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9'))
                )
