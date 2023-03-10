import subprocess


""" this is our gameboard

         X | O | X 
     X | O | X 
         X | O | X 
     X | O | X 
         X | O | X 
        ---+---+---
         X | O | X 
     X | O | X 
         X | O | X 
     X | O | X 
         X | O | X 
        ---+---+---
         O | O | X      
     O | O | X      
         O | O | X      
     O | O | X      
         O | O | X      


 todo:
   a cell can not marked twice
   1 player vs computer.
   error when input invalid letter   

"""

class Cell:
    def __init__(self, mark):
        self.mark = mark
        self.empty = True
    
    def __str__(self):
        markStr = "" 
        return f' {self.mark} '
    
    def setMark(self, mark):
        self.mark = mark
        self.empty = False
    
    def isEmpty(self):
        return self.empty
    
    def isNotEmpty(self):
        return not self.empty


class Row:
    def __init__(self, rowNum):
        self.rowNum = rowNum
        self.cell1 = Cell(" ")
        self.cell2 = Cell(" ")
        self.cell3 = Cell(" ")
    
    def __str__(self): 
        return f'{self.cell1}|{self.cell2}|{self.cell3}\n'
    

    def setMark(self, cellNum, markValue):
        if(cellNum == 1):
            self.cell1.setMark(markValue)
        elif(cellNum == 2):
            self.cell2.setMark(markValue)
        else:
            self.cell3.setMark(markValue)

    
    def win(self):
        isSomeBodyWin = (self.cell1.isNotEmpty()) and (self.cell1.mark == self.cell2.mark) and (self.cell2.mark == self.cell3.mark)
        return isSomeBodyWin


class RowSeparator:
    def __str__(self): 
        return "---+---+---\n"

class Gameboard:

    def __init__(self):
        self.row1 = Row(1)
        self.row2 = Row(2)
        self.row3 = Row(3)
        self.turn = "X"
        self.rowSeparator = RowSeparator()
    

    def __str__(self):
        return f'\n{self.row1}{self.rowSeparator}{self.row2}{self.rowSeparator}{self.row3}'
    
    def putMark(self, position, mark):
        if(position < 4): 
            self.row1.setMark(position, mark)
        elif(position < 7):
            self.row2.setMark(position - 3,mark)
        else:
            self.row3.setMark(position - 6,mark)
        
        self.switch()

    
    def checkIfAnybodyWin(self):
        return self.row1.win() or self.row2.win() or self.row3.win() or self.sameC1() or self.sameC2() or self.sameC3() or self.diagonalWin() or self.diagonalWin2()
    
    def sameC1(self) :
        return (self.row1.cell1.isNotEmpty()) and (self.row1.cell1.mark == self.row2.cell1.mark) and (self.row2.cell1.mark == self.row3.cell1.mark)

    def sameC2(self) :
        return (self.row1.cell2.isNotEmpty()) and (self.row1.cell2.mark == self.row2.cell2.mark) and (self.row2.cell2.mark == self.row3.cell2.mark)
        
    def sameC3(self) :
        return (self.row1.cell3.isNotEmpty()) and (self.row1.cell3.mark == self.row2.cell3.mark) and (self.row2.cell3.mark == self.row3.cell3.mark)
    

    #  .is marked  
    # r1.c1 == r2.c2 
    # r2.c2 == r3.c3

    def diagonalWin(self):
        return (self.row1.cell1.isNotEmpty()) and (self.row1.cell1.mark == self.row2.cell2.mark) and (self.row2.cell2.mark == self.row3.cell3.mark)
    
    
    # conditions?
    # r1.c3 == r2.c2 == r3.c1 is marked
    # all is marked 
    # r1.c3 == r2.c2
    # r2.c2 == r3.c1
    #
    def diagonalWin2(self):
        return (self.row1.cell3.isNotEmpty()) and (self.row1.cell3.mark == self.row2.cell2.mark) and (self.row2.cell2.mark == self.row3.cell1.mark)
        

    def setPlayers(number):
        pass

    def play(self): 
        position = input(f'It is {self.turn} which position you want to mark: ')
        position = int(position)
        self.putMark(position, self.turn)
        self.clean()
        print(self)
        
    def start(self) :
        self.clean()
        print(self)
        while(True):
            self.play()
            if(self.checkIfAnybodyWin()):
                print(f'{self.lastTurn()}, U WIN!!!')
                break


    def clean(self):
        subprocess.call("clear")

    
    def switch(self):
        if(self.turn == "X"):
            self.turn = "O"
        else:
            self.turn = "X"

    def lastTurn(self):
        if(self.turn == 'X'):
            return 'O'
        else:
            return 'X'

    


game = Gameboard()
game.setPlayers()
game.start()