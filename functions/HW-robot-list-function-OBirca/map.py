rc = 0
rr = 0

gameMap = [
    [0,0,0,3,0,0,0,0,0,0], 
    [0,0,1,0,0,0,0,3,0,0], 
    [0,0,0,1,0,0,0,0,0,0], 
    [0,0,0,0,1,0,0,0,0,0], 
    [0,0,0,0,0,1,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,3,0,0,0], 
    [0,3,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,3,0,1]

]

gameMap [rr][rc] = 2

def p (c):
    print (c + " ", end = "")


def printMap ( list ):
    for ri in range(len(list)):
        for ci in range(len(list[ri])):
            
            if list [ri][ci] == 1:
                p("#")

            elif list [ri][ci] == 3:
                p("+")

            elif list [ri][ci] == 4:
                p("X")

            elif list [ri][ci] == 2:
                p("R")
            
            elif list[ri][ci] == 0:
                p(".")
            
                

        print()

printMap(gameMap)