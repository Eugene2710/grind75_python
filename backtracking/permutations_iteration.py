class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        """
        perms: list[list[int]] = [[]]
        for n in nums:
            new_perms: list[list[int]] = [[]]
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms

        return perms

    """
    e.g. nums = [1,2,3]
    n=1 -> perms = [[]] -> p = [] -> new_perms = [[],[1]] -> perms = [[],[1]]
    n=2 -> new_perms = [[],[1]] -> p=[] -> p_copy = [2] -> new_perms = [[],[1],[2]] -> perms = [[],[1],[2]]
                                p=[1] -> i=1 -> p_copy = [1,2] -> new_perms = [[],[1],[2],[1,2]]
    """
