class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Using dfs recursion, if elem is same as og color, change it to the new color
        In that event, check for surrounding elements and boundaries

        Time complexity: O(M*N)
        Space complaexity: O(M*N)
        """
        m: int = len(image)
        n: int = len(image[0])
        og: int = image[sr][sc]
        if og == color:
            return image

        def dfs(r: int, c: int) -> None:
            if image[r][c] == og:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1, c)
                if r+1 < m:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c+1 < n:
                    dfs(r, c+1)
        dfs(r=sr, c=sc)
        return image