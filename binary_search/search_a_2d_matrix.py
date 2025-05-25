class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search: flatten matrix, floor and mod the row and column by their lengths
        time complexity: O(N)
        space complexity: O(1)
        """
        m: int = len(matrix)
        n: int = len(matrix)

        bot: int = 0
        top: int = m*n-1

        while top>=bot:
            mid: int = (top+bot)//2
            r, c = divmod(mid, n)
            val: int = matrix[r][c]
            if val==target:
                return True
            elif val>target:
                top = mid-1
            else:
                bot = mid+1
        return False