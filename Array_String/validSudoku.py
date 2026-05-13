from collections import defaultdict

def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y == ".":
                    continue
                pair = (i//3, j//3)
                if y in cols[j] or y in rows[i] or y in squares[pair]:
                    return False
                cols[j].add(y)
                rows[i].add(y)
                squares[pair].add(y)
        return True