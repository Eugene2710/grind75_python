class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        DFS: Using a stack to store tuples of row and column index, iterate through stack.
        For each element in stack, check if surrounding elements are same as color, if they are add to stack.
        Check surrounding using four connectivity approach

        time complexity: O(M*N)
        space complexity: O(M*N)
        """
        m: int = len(image)
        n: int = len(image[0])
        og: int = image[sr][sc]
        # in event where og==color, return image to prevent further checks
        if og==color:
            return image
        stack: list[tuple[int, int]] = [(sr, sc)]

        while stack:
            r, c = stack.pop()
            if image[r][c] != og:
                continue

            image[r][c] = color

            # push neighbors
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and image[nr][nc]==og:
                    stack.append((nr, nc))

        return image
