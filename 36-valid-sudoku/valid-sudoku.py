from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Arrays for hashing
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        # Traverse the board
        for r in range(9):
            for c in range(9):

                # Ignore empty cells
                if board[r][c] == ".":
                    continue

                # Convert number string to index
                # "1" -> 0
                # "2" -> 1
                # ...
                # "9" -> 8
                num = int(board[r][c]) - 1

                # Find 3x3 box index
                box = (r // 3) * 3 + (c // 3)

                # Check duplicate in row
                if rows[r][num] == 1:
                    return False

                # Check duplicate in column
                if cols[c][num] == 1:
                    return False

                # Check duplicate in box
                if boxes[box][num] == 1:
                    return False

                # Mark number as visited
                rows[r][num] = 1
                cols[c][num] = 1
                boxes[box][num] = 1

        return True