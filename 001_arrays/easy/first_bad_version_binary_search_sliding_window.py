# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        """
        Approach: Binary search through n; sliding window
        Time Complexity: O(log n)
        Space complexity: O(1)

        """

        left: int = 1
        right: int = n

        while right > left:
            mid: int = (right + left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                # +1 to make sure there is no TLE
                # use left=mid+! instead of right=mid-1 bc you want the latest version bad version which of a higher value
                left = mid + 1
        return left