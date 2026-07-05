from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r, x in enumerate(board):
            for c, y in enumerate(x):
                if y == ".":
                    continue
                else:
                    square_identifier = (r//3, c//3)
                    if y in rows[r]:
                        return False
                    if y in columns[c]:
                        return False
                    if y in squares[square_identifier]:
                        return False

                    rows[r].add(y)
                    columns[c].add(y)
                    squares[square_identifier].add(y)

        print(rows)
        print(columns)
        print(squares)
        return True


