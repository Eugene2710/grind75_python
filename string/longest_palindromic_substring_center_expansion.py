class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        approach 1(not the most efficient): center expansion (expand around center)
        using sliding window,
            expand around i for odd-length palindrome
            expand around i+1 for even-length palindrome

        time complexity: O(N^2)
        space complexity: O(1) not counint output string
        example
        "aaa"
        """
        if not s or len(s) < 2:
            return s

        start, max_length = 0, 1

        for i in range(len(s)):
            # 1) Check for odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

            # 2) Check for even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

        return s[start:start + max_length]
