class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        2 pointers: left - from start, right - from end
        vol: min(height[left], height[right]) * (right-left)
        move pointer which is smaller towards center and replace max vol if vol>max
        """
        l: int = 0
        r: int = len(height)-1
        most: int = 0

        while l<r:
            curr: int = min(height[l], height[r]) * (r-l)
            most = max(most, curr)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1

        return most