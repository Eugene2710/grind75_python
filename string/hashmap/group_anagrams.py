from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hashset to map list of character count as key, list of strings with the same anagram as value

        time complexity: O(M*N* 26), M: length of input strings given, N: avg length of strings given
        space complexity: O(26*M*N)
        """
        # map char count to list of anagrams
        res = defaultdict(list)

        for s in strs:
            # populate list of int of length 26 - num of alphabets possible
            count: list[int] = [0] * 26
            # increment value of alphabet number key according to occurrences
            for c in s:
                count[ord(c) - ord("a")] += 1
            # append str to list where key is the list containing occurrences of alphabet number keys
            # note: key cannot be list since lists are mutables in python, hence make it a tuple
            res[tuple(count)].append(s)
        # make res.values a list aas res.values is a lazy view object in latest versions of python
        return list(res.values())
