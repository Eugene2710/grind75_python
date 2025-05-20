class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        dfs recursion backtracking:
        iterate through 2d list and if elem==word[0], recurse dfs on the surrounding elem
        dfs checks if the elem in board == indexed elem in word, if not return False
        else return True and recurse dfs on surrounding elem
        if index of word == len(word), return True

        time complexity: O(M*N* 2^W), W: word length
        sapce complexity: O(W)
        """
        m: int = len(board)
        n: int = len(board[0])
        path: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, i: int) -> bool:
            # once index is length of word, word is found in board -> return True
            if i == len(word):
                return True
            # check for false conditions
            if (r<0 or r>=m or c<0 or c>=n or word[i]!=board[r][c] or (r,c) in path):
                return False
            # add (r,c) in path
            path.add((r,c))
            # check for surrounding elements
            res = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            # backtrack and check for other permutations
            path.remove((r, c))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(r, c, 0):
                    return True

        return False
