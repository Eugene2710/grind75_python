class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        binary search w 2 pointers/sliding window to look for bad version
        if (l+r)//2 == n: return (l+r)//2
        elif (l+r)//2 < n: l = (l+r)//2 +1
        else: r = (l+r)//2 - 1

        time complexity: O(log N)
        space complexity: O(1)
        """
        l: int = 1
        r: int = n
        while l<r:
            mid: int = (l+r)//2
            # case: once bad version is found, everything to the right can be trimmed off
            if isBadVersion(mid) is True:
                r = mid
            else:
                l = mid +1
        return l

"""
[
l=4, r=5
mid = 9//2 = 4
r=4


n = 5, bad = 4
mid = (1+5)//2 = 3
l = 4 , line 20
]
"""