#TicTacToe

class Canvas:
    #attributes
    def __init__(self):
        #[ : ASCII 91
        #] : ASCII 93
        self.EMPTY = chr(91) +" " + chr(93)

        #any empty mat[3][3]
        self.mat =[[self.EMPTY]*3, [self.EMPTY]*3, [self.EMPTY]*3]


    def updateCanvas(self, r, c, symbol):
        #validate
        if r >= 3 or r < 0:
            return False
        if c >= 3 or c < 0:
            return False
        if self.mat[r][c] != self.EMPTY:
            return False
        #update
        self.mat[r][c] = chr(91)+ symbol + chr(93)
        return True

    def displayCanvas(self):
        i = 0
        while i < 3:
            print()
            j =0
            while j < 3:
                print(self.mat[i][j], end=" ")
                j+=1
            i+=1

        print()

    def eraseCanvas(self):
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                self.mat[i][j] = self.EMPTY
                j += 1
            i += 1

    def isFullCanvas(self):
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                if self.mat[i][j] == self.EMPTY:
                    return False
                j += 1
            i += 1
        return True

    def matchRow(self, r, symbol):
        compare = chr(91) + symbol + chr(93)
        return self.mat[r][0] == compare and self.mat[r][1] == compare and self.mat[r][2] == compare

    def matchCol(self, c, symbol):
        compare = chr(91) + symbol + chr(93)
        return self.mat[0][c] == compare and self.mat[1][c] == compare and self.mat[2][c] == compare

    def matchDiagonal(self, symbol):
        compare = chr(91) + symbol + chr(93)
        return self.mat[0][0] == compare and self.mat[1][1] == compare and self.mat[2][2] == compare

    def matchReverseDiagonal(self, symbol):
        compare = chr(91) + symbol + chr(93)
        return self.mat[0][2] == compare and self.mat[1][1] == compare and self.mat[2][0] == compare


class TicTacToe:
    def __init__(self):
        self.players = []
        self.symbol = ['x', 'o']
        self.c = Canvas()

    def checkWins(self, symbol):

        i =0
        while i < 3:
            if self.c.matchRow(i, symbol):
                return True
            i+=1

        i = 0
        while i < 3:
            if self.c.matchCol(i, symbol):
                return True
            i += 1

        if self.c.matchDiagonal(symbol):
            return True

        if self.c.matchReverseDiagonal(symbol):
            return True

        return False


    def play(self):
        #whose playing
        temp = input("Name of player 1 ")
        self.players.append(temp)
        temp = input("Name of player 2 ")
        self.players.append(temp)

        print("Symbol for ", self.players[0], " is ", self.symbol[0])
        print("Symbol for ", self.players[1], " is ", self.symbol[1])

        self.c.displayCanvas()
        
        flag = 0
        current = 0
        while not self.c.isFullCanvas():
            print(self.players[current] + " (" + self.symbol[current] + ") plays ")
            r = int(input("Enter row coordinate "))
            c = int(input("Enter col coordinate "))

            if self.c.updateCanvas(r,c, self.symbol[current]):
                self.c.displayCanvas()
                if self.checkWins(self.symbol[current]):
                    print(self.players[current] + " wins")
                    flag = 1
                    break

                current = (current + 1) % 2
            else:
                print("Wrong move by ", self.players[current])
                print("play again")

        if flag == 0:
            print("Game Draw")

        self.c.eraseCanvas()

def main():
    ttt = TicTacToe()
    ch = "y"
    while ch == 'y':
        ttt.play()
        ch = input("Play Again (y/n) ")


main()