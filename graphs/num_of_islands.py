class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        mark-in-place recursive dfs approach:
        if surrounding elem is 1 and within bounds: change elem to 0 and add to recursive dfs call stack

        time complexity: O(m*n)
        space complexity: O(1)

        note:
        - It does not matter where you start - if it is an island it will be interconnected so no island will be double counted
        - for checking of outer bound, use >= instead of > since it is comparison against length of list
        """
        rows: int = len(grid)
        cols: int = len(grid[0])
        islands: int = 0

        def dfs(r: int, c: int) -> None:
            # case 1: if out of bounds or elem == 0: return
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0":
                return
            # case 2: if within bounds AND elem==1: change elem to 0 and add elem to recursion call stack
            grid[r][c] = 0
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)

        return islands