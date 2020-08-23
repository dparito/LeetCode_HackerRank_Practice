from challenge_header import printHeader


class Solution:
    def isRowValid(self, row) -> bool:
        row_num_list = [i for i in row if i is not '.']
        row_num_set = set(row_num_list)
        return True if len(row_num_list) == len(row_num_set) else False


    def isColValid(self, col) -> bool:
        col_num_list = [i for i in col if i is not '.']
        col_num_set = set(col_num_list)
        return True if len(col_num_list) == len(col_num_set) else False


    def isSubBoxValid(self, sub_box) -> bool:
        sub_box_num_list = [i for i in sub_box if i is not '.']
        sub_box_num_set = set(sub_box_num_list)
        return True if len(sub_box_num_list) == len(sub_box_num_set) else False

    
    def isValidSudoku(self, board) -> bool:
        row_validity_check = True
        col_validity_check = True
        sub_box_validity_check = True

        for row in board:
            row_validity_check = row_validity_check and self.isRowValid(row)

        for col in range(9):
            column = []
            for row in range(9):
                column.append(board[row][col])
            col_validity_check = col_validity_check and self.isColValid(column)

        col = 0
        while col < 9:
            row = 0
            while row < 9:
                sub_box = [board[row][col],board[row][col+1],board[row][col+2],
                            board[row+1][col],board[row+1][col+1],board[row+1][col+2],
                            board[row+2][col],board[row+2][col+1],board[row+2][col+2]]
                sub_box_validity_check = sub_box_validity_check and self.isSubBoxValid(sub_box)
                row += 3
            col += 3

        return row_validity_check and col_validity_check and sub_box_validity_check
        

if __name__ == "__main__":
    printHeader("Valid Sudoku")

    board = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    
    my_solution = Solution()
    
    print(my_solution.isValidSudoku(board))
