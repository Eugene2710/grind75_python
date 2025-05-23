from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        3 hashsets:
        cols to check if value exists across that column,
        rows to check if val exists in that row
        squares to check if val exists in that square
        iterate through each cell and check if value exists or not, return if not exists, skip if empty cell

        time complexity: O(3*9^2)
        space complexity: O(3*9^2)
        """
        cols: dict[int, set[int]] = defaultdict(set)
        rows: dict[int, set[int]] = defaultdict(set)
        squares: dict[tuple[int], set[int]] = defaultdict(set)

        for i in range(9):
            for j in range(9):
                # case if no int is around, skip
                if board[i][j] == ".":
                    continue
                # case if elem exists in either hashset, return False
                if (
                    board[i][j] in cols[i] or
                    board[i][j] in rows[j] or
                    board[i][j] in squares[(i//3, j//3)]
                ):
                    return False
                # else, append elem into the hashsets
                cols[i].add(board[i][j])
                rows[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])

        return True