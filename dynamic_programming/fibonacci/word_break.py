class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        bottom up DP:
        iterate through each char of input string s, nested iteration through each word in wordDict,
        check if LENGTHS of index+word < len(s) AND for exact same characters between char in s and word

        time complexity: O(S * W) , W: num of words in wordDict
        space complexity: O(S)
        """
        s_len: int = len(s)
        # initialize list of False bools by default and of length s+1 (s+1 so that last index is True as base case)
        # turn indexed position to true if word match the chars in dp
        dp: list[bool] = [False] * (s_len + 1)
        dp[s_len] = True

        for i in range(s_len-1, -1, -1):
            for word in wordDict:
                word_len: int = len(word)
                if i+word_len <= s_len and s[i: i+word_len] == word:
                    dp[i] = dp[i+word_len]
                # if dp[i] is True, there is no need to check for other word in wordDict
                if dp[i]:
                    break
        return dp[0]