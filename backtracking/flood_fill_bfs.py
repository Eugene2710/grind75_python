from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Deque to store elements which same as og elem, if same add qo deque
        Check surrounding elem and add to deque

        time complexity: O(MN)
        space complexity: O(MN)
        """
        m: int = len(image)
        n: int = len(image[0])
        og: int = image[sr][sc]

        if og == color:
            return image
        dequeue: deque[tuple[int, int]] = deque()
        dequeue.append((sr, sc))

        while dequeue:
            r, c = dequeue.popleft()
            if image[r][c] != og:
                continue
            image[r][c] = color

            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and image[nr][nc]==og:
                    dequeue.append((nr, nc))

        return image

