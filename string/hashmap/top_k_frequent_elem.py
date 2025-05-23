class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        iterate through nums and append to dict with num of elem as key, elem as value
        iterate through dict (use dict.items()), assign elem of list as nums elem, index of list as nums freq
        iterate from end of list to start of list and if there is value in list, append elems to result

        time complexity: O(N)
        space complexity: O(N)
        """
        count: dict[int, int] = {}
        n: int = len(k)
        # populate list of n+1
        freq: list[list[int]] = [[] for i in range(n+1)]

        # assign elem of num as key of dict, frequency of num elem as value of dict
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        # assign freq as index of list, elem of num as elem of list
        for num, c in count.values():
            freq[c].append(num)

        res: list[int] = []
        # iterate through list backwards, if elems exits in that index, append to res
        # return if length of res == k
        for i in range(n, 0, -1):
            if freq[i]:
                res.extend(freq[i])
                if len(res) == k:
                    return res
