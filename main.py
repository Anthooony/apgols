from random import randint

class Board:
    def __init__(self, size, num):
        self.l = [["."  for i in range(size)] for i in range(size)]
        for i in range(num):
            self.l[randint(0,size-1)][randint(0,size-1)] = "O"
            
    def run():
        while True:
            self.update()
            
    def update():
        for x in len(self.l):
            for y in len(self.l[x]):
                cell = self.l[x][y]
                nbn = self.nb_of_neighbours(x, y)
                if cell == ".":   #x and y are the coordinates of the cell
                    if nbn == 3:
                        cell = 1
                if cell == "O":
                    if nbn < 2:
                        cell = 0
                    if nbn > 3:
                        cell = 0
                        
    def nb_of_neighbours(self, x, y):
        n=0
        #code :D
        return n