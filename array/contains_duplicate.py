class Solution: 
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        approach: use a set, if value exists in set: return True, else: add value to set
        """
        nums_set: set[int] = set()
        for elem in nums:
            if elem in nums_set:
                return True
            else:
                nums_set.add(elem)
        return False