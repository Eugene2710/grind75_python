class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        """
        Approach: Recursive DFS - start from image[sr][sc], store value. If image[sr][sc-1] == stored value, change else, terminate. Recurse as long as not out of bound.

        Time Complexity: O(RC)
        Space Complexity: O(RC)
        """

        # helper function to check if cell is not out of bound
        def valid_cell(row: int, col: int) -> bool:
            return row >= 0 and row < len(image) and col >= 0 and col < len(image[row])

        def dfs(start: int, row: int, col: int) -> None:
            # return/remove dfs stack if cell == color
            if image[row][col] == color:
                return
            # else change approved cell to same value as color
            image[row][col] = color

            # a 2D list to help move around the surrounding cells more easier
            row_col_directional_list: List[Tuple[int, int]] = [
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]

            # loop through surrounding cell - if it is within bound and == to starting cell, add that cell to the dfs call stack
            for d_row, d_col in row_col_directional_list:
                new_row: int = row + d_row
                new_col: int = col + d_col
                if valid_cell(new_row, new_col) and image[new_row][new_col] == start:
                    dfs(start, new_row, new_col)

        dfs(image[sr][sc], sr, sc)
        return image
