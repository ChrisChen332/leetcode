from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check row
        for i in range(len(board)):
            dup = set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dup:
                    return False
                dup.add(board[i][j])

        #Check Column
        for i in range(len(board)):
            dup = set()
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in dup:
                    return False
                dup.add(board[j][i])
        for square in range(9):
            dup = set()
            for i in range(3):
                for j in range(3):
                    col = (square % 3) * 3 + i
                    row = (square // 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in dup:
                        return False
                    dup.add(board[row][col])
        return True