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
        if not s:
            return ""
        # 1) Transform s into T with a boundary char (e.g., '|')
        #    T will have length = 2 * len(s) + 1
        T = "|".join("^{}$".format(s))  # Another pattern: "^|" + "|".join(s) + "|$"
        n = len(T)

        P = [0] * n
        center = right = 0

        # 2) Main Manacher loop
        for i in range(1, n - 1):
            mirror = 2 * center - i # bc center is always equal to (mirror+i)/2

            # If i is within the right boundary, mirror's info can help initialize P[i]
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Attempt to expand around i
            while i + 1 + P[i] < n and i - 1 - P[i] >= 0 and T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If we've expanded past 'right', update center, right
            if i + P[i] > right:
                center, right = i, i + P[i]

        # 3) Find the maximum element in P
        max_len = 0
        center_index = 0
        for i in range(1, n - 1):
            if P[i] > max_len:
                max_len = P[i]
                center_index = i

        # 4) Determine the start in the original string
        # The transformation was ^ + s_0 + | + s_1 + | ... + s_{n-1} + $
        # center_index corresponds to position in T, which we map back to s.
        # If we used "^{}".format(s), then for a P[i], the substring in s
        # starts at (center_index - max_len) // 2 in the original s.
        start = (center_index - max_len) // 2

        return s[start: start + max_len]