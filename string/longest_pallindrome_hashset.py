class Solution:
    def longestPallindrome(self, s: str) -> int:
        """
        approach 2: (slightly faster as it iterates through the input string only once and does not iterate through the hashmap again for approach 1)
        using a hashset to add characters if that char appears
        if char alr exists, remove it and add 2 to res
        add 1 to res if there is still a value in hashset - this means that there is still an odd value

        time complexity: O(N)
        space complexity: O(N)
        """
        seen: set[int] = set()
        res: int = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                res+=2
            else:
                seen.add(c)
        
        return res+1 if seen else res