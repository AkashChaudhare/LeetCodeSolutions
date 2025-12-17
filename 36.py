class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sq = defaultdict(set)


        for r in range(9):
            for c in range(9):
                val = board[r][c] 
                if val == ".":
                    continue
                if (val in cols[c]) or (val in rows[r]) or (val in sq[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sq[(r // 3, c // 3)].add(board[r][c])
        print(sq)
        return True
