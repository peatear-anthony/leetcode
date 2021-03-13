# https://leetcode.com/problems/available-captures-for-rook/


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # step one find the rook
        for index, row in enumerate(board):
            if 'R' not in row:
                continue
            col_index = row.index('R')
            row_index = index
            break

        rook_row = [piece for piece in board[row_index] if piece != '.' ]
        rook_col = [row[col_index] for row in board]
        rook_col = [piece for piece in rook_col if piece != '.' ]

        simple_board = [rook_row, rook_col]
        simple_board = [line for line in simple_board if len(line) >= 2]
        count = 0

        for line in simple_board:
            rook_index = line.index('R')
            if rook_index == 0: # Left edge case ['R', '*',...]
                if line[rook_index + 1] == 'p':
                    count += 1 
            elif rook_index == len(line) - 1: # Right edge case ['...', '*','R']
                if line[rook_index - 1] == 'p':
                    count += 1 
            else: # Normal case ['*', 'R','*']
                if line[rook_index + 1] == 'p':
                    count += 1
                if line[rook_index - 1] == 'p':
                    count += 1   
        return count
