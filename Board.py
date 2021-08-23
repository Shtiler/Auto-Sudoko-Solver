
class Board:
    def __init__(self):
        self.board =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def Print(self):
        for i in range(len(self.board)): 
            if i % 3 == 0 and i != 0: print("- - - - - - - - - - - -")
            
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0: print(" | ", end="")
                
                if j == 8: print(self.board[i][j])
                else: print(self.board[i][j], end=" ")
        print("\n")
    
    # Input option by X,Y
    def Input(self):
        try:
            while True:
                print("Enter a X to input or any string to exit")
                x = int(input())
                print("Enter a Y to input or any string to exit")
                y = int(input())
                print("Enter a Value to input or any string to exit")
                value = int(input())
                if value > 9:
                    raise Exception
                self.board[x][y] = value
                print("Update:  \n ")
                self.Print()
        except:
            print("Error")
        finally:
            print("Board Looks Like This \n :")
            self.Print()
    
    # Input by 9 digits that represents a row
    def InputRow(self):
        for i in range(9):
            lst = []
            print(f"Enter 9 digits that represent line {i+1}")
            string = input()
            lst = [int(d) for d in str(string)]
            self.board[i] = lst
            print("Board Looks Like This: \n")
            self.Print()
            
    
    def FindEmpty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i,j
        return None,None

    def Valid(self,guess, row, col):
        row_vals = self.board[row]
        if guess in row_vals:
            return False 
        col_vals = [self.board[i][col] for i in range(9)]
        if guess in col_vals:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == guess:
                    return False

        return True

    
    def Solve(self):
        row, col = self.FindEmpty()

        if row is None: 
            self.Print()
            return True,self.board
        
        for guess in range(1, 10): 
            if self.Valid(guess, row, col):
                self.board[row][col] = guess
                if self.Solve()[0]:
                    return True,self.board
            self.board[row][col] = 0
        return False,self.board
                
        

        



