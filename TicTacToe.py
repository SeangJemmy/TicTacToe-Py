class TicTacToe:

    def __init__(self, p1, p2, xo, version):
        self.version = version
        self.p1 = p1
        self.p2 = p2
        self.xo = xo.lower()

        if self.xo == "x": 
            self.pxo = p1
        else:
            self.pxo = p2

        self.board = [[str(i*3 + (j + 1)) for j in range(3)] for i in range(3)]
        self.cloneboard = [[" " for j in range(3)] for i in range(3)]
        self.countinput = 0
        self.autonum = 0
        self.win = False

    def welcome(self):
        print(f"<< Welcome {self.p1}(x) and {self.p2}(o)! >>")

    def pBoard(self):
        hd = "-"*11
        ct = 2
        print()
        for i in range(3):
            print(f" {self.cloneboard[i][0]} | {self.cloneboard[i][1]} | {self.cloneboard[i][2]} ")
            if ct != 0:
                print(hd)
                ct -= 1
        print()

    def switchPlayer(self):
        if self.xo == "o":
            self.xo = "x"
            self.pxo = self.p1
        else:
            self.xo = "o"
            self.pxo = self.p2
        
    def drawBoard(self, n):
        ni = (n-1) // 3
        nj = (n-1) % 3
        self.board[ni][nj] = self.cloneboard[ni][nj] = self.xo
    
    def isValid(self, n):
        ni = (n-1) // 3
        nj = (n-1) % 3
        if (self.board[ni][nj] == "o" or self.board[ni][nj] == "x"):
            return False
        else:
            return True

    def checkWin(self):
        # Check Row
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                self.win = True
        
        # Check Column
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                self.win = True

        # Check Diagonal
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            self.win = True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            self.win = True

    def autoInput(self):
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] == "o" or self.board[i][j] == "x") is False:
                    self.autonum = i*3 + (j + 1)
                    self.cloneboard[i][j] = self.board[i][j] = self.xo