class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validate_block(col_start, col_end, row_start, row_end, board):
            arr1=[]
            for i in range(col_start,col_end+1):
                for j in range(row_start,row_end+1):
                    if board[j][i] != '.':
                        if board[j][i] in arr1:
                            return False
                        else:
                            arr1.append(board[j][i])
            return True

            # validate a row
        
        for row in board:
            row_numbers = []
            for i in range(0, 9):
                if row[i] != '.':
                    if row[i] in row_numbers:
                        return False
                    else: 
                        row_numbers.append(row[i])

        # validate a column
        for i in range(0, 9):
            column_numbers = []
            for j in range(0,9):
                if board[j][i] != '.':
                    if board[j][i] in column_numbers:
                        return False
                    else:
                        column_numbers.append(board[j][i])


        # validate 3*3 block column wise (0-2)
        # 0-2
        if not validate_block(0, 2, 0 , 2, board):
            return False
        # 3-5
        if not validate_block(0, 2, 3, 5, board):
            return False
        # 6-8
        if not validate_block(0, 2, 6, 8, board):
            return False
        
        # validate 3*3 block column wise (3-5)
        # 0-2
        if not validate_block(3, 5, 0 , 2, board):
            return False
        # 3-5
        if not validate_block(3, 5, 3, 5, board):
            return False
        # 6-8
        if not validate_block(3, 5, 6, 8, board):
            return False
        
        # validate 3*3 block column wise (6-8)
        # 0-2
        if not validate_block(6, 8, 0 , 2, board):
            return False
        # 3-5
        if not validate_block(6, 8, 3, 5, board):
            return False
        # 6-8
        if not validate_block(6, 8, 6, 8, board):
            return False

        

        return True
        