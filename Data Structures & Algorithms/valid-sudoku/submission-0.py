class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        cln = [set()for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                b = (r // 3)*3+ (c // 3)
                num = board[r][c]
                if num in row[r] or num in cln[c] or num in box[b]:
                    return False
                row[r].add(num)
                cln[c].add(num)
                box[b].add(num)

        return True