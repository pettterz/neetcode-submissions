class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                digit = board[i][j]
                if digit != ".":
                    block = (i // 3) * 3 + (j // 3)
                    if digit in rows[i] or digit in cols[j] or digit in squares[block]:
                        return False
                    else:
                        rows[i].add(digit)
                        cols[j].add(digit)
                        squares[block].add(digit)

        return True

                    

        