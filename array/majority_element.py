class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        approach: use Boyer-Moore Voting algo - count the frequency of ONLY the top candidate AND the top cadidate
        """
        candidate: int = nums[0]
        freq: int = 1
        for i in nums[1:]:
            if freq == 0:
                candidate = i
            if nums[i] == candidate:
                freq+=1
            if nums[i] != candidate:
                freq -= 1

        return candidate