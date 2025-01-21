class Solution:
    def longestPallindrome(self, s: str) -> int:
        """
        approach 1:
        using a hashmap/dict to store the char as keys and counts and values, 
        iterate through input string and add 2 to res ONLY IF the count for the char is even num (%2 == 0)
        iterate through values of hashmap/dict and if there is any value which count is odd, add 1 to res

        time complexity: O(2N) = O(N)
        space complexity: O(N)
        """
        count: dict[int] = defaultdict(int) # defaultdict helps to deal w valueerrors
        res: int = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 2:
                res += 2
        for cnt in count.values(): # note that .values is a method within the defaultdict lib, so remb to include brackets
            if cnt % 2 = 1:
                res += 1
                break # include break bc there is no need to find any other odd values - they cannot contribute to res

        return res