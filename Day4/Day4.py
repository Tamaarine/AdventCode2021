class Board():
    def __init__(self, row=5, col=5):
        self.row = row
        self.col = col
        self.board = [[-1 for _ in range(col)] for _ in range(row)] # make a row x col matrix with -1 values
        self.current_row_inserted = 0 # keeps track of how many rows has been inserted by insert_row
        # insert values later
        
    def check_winning(self):
        # check all row and all column for winning
        # return True if any row/col wins
        for row in self.board:
            won = True
            for pair in row:
                if not pair[1]:
                    won = False
                    break
            # Go through every row, if one single row has all of the elements marked, then we return True
            if won:
                return True 
        
        # If none of the rows has a winning we check all the column, must use index. Column major order
        for c in range(len(self.board)):
            won = True
            for r in range(len(self.board[0])):
                if not self.board[r][c][1]:
                    won = False
                    break
            if won:
                return True
        
        # If we reach here that means none of the row/col has a win return false
        return False
    
    def insert_row(self, line):
        line = line.strip('\n')
        splitted = line.split()
        if self.current_row_inserted < self.row:
            self.board[self.current_row_inserted] = [(int(str_num), False) for str_num in splitted] # num, boolean pair
            self.current_row_inserted += 1
            return 0
        else:
            return 1
            
    def mark_num(self, num):
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if self.board[r][c][0] == num:
                    self.board[r][c] = (num, True)
                    break
    
    def retrieve_unmarked_sum(self):
        sum = 0
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                if not self.board[r][c][1]:
                    sum += self.board[r][c][0]
        return sum
    
    def __str__(self):
        ret = ""
        for row in self.board:
            ret += str(row) + '\n'
        return ret             
        
def day4p1(filename, row=5):
    file = open(filename, 'r')
    
    moves = [int(num) for num in file.readline().split(',')]
    boards : list[Board] = []
    
    file = [line for line in file if len(line) != 1]
    max = len(file) // row
    
    for i in range(max):
        to_insert = Board()
        for j in range(5):
            to_insert.insert_row(file[5 * i + j])
        boards.append(to_insert)
    
    for move in moves:
        for board in boards:
            board.mark_num(move)
            
            if board.check_winning():
                # if this board wins after inserting the number
                # retrieve the sum
                return board.retrieve_unmarked_sum() * move
    
    
def day4p2(filename, row=5):
    file = open(filename, 'r')
    
    moves = [int(num) for num in file.readline().split(',')]
    boards : list[Board] = []
    
    file = [line for line in file if len(line) != 1]
    max = len(file) // row
    
    for i in range(max):
        to_insert = Board()
        for j in range(5):
            to_insert.insert_row(file[5 * i + j])
        boards.append(to_insert)
    
    winning_board = [False for i in range(len(boards))]
    count = len(winning_board)
    
    for move in moves:
        for i, board in enumerate(boards):
            board.mark_num(move)
            
            if board.check_winning() and not winning_board[i]:
                if count > 1:
                    # if this board wins after inserting the number
                    # retrieve the sum
                    if not winning_board[i]:
                        count -= 1
                        winning_board[i] = True
                else:
                    print(move, board)
                    return board.retrieve_unmarked_sum() * move
                     
if __name__ == "__main__":
    print(day4p1('input.txt'))
    print(day4p2('input.txt'))