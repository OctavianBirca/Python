from map import *
from ui import *

message = "ok"

while True:
    clear()
    print(message)
    printMap(gameMap)
    key = controls()

    if key == "x":
        break

    gameMap[rr][rc] = 0

    
    if key == "d" and rc < len(gameMap[0]) -1 and gameMap[rr][rc+1] != 1 :
        rc += 1
        

    if key == "a" and rc > 0 and gameMap[rr][rc-1] != 1: 
        rc -= 1


    if key == "s" and rr < len(gameMap)-1 and gameMap[rr+1][rc] != 1:
        rr += 1
        

    if key == "w" and rr > 0 and gameMap[rr-1][rc] != 1:
        rr -= 1

    
    
    

    if gameMap[rr][rc+2] == 3 :
        message = "Warning! Danger on the left!!!"
        if gameMap[rr][rc+2] == 3:
            gameMap[rr][rc+2] = 4
    
    elif gameMap[rr][rc+3] == 4 and gameMap[rr][rc+3] != 1:
        message = "ok!"
        gameMap[rr][rc+3] = 3
    

    elif gameMap[rr][rc-2] == 3:
       message = "Waring danger on the right!"
       if gameMap[rr][rc-2] == 3:
            gameMap[rr][rc-2] = 4

    elif gameMap[rr][rc-3] == 4 and gameMap[rr][rc-3] != 1:
        message = "ok!"
        gameMap[rr][rc-3] = 3

    elif gameMap[rr+2][rc] == 3:
        message = "Waring danged!"
        if gameMap[rr+2][rc] == 3:
            gameMap[rr+2][rc] = 4 
    
    elif gameMap[rr+3][rc] == 4 and gameMap[rr+3][rc] != 1:
        message = "ok!"
        gameMap[rr+3][rc] = 3
    
    elif gameMap[rr-2][rc] == 3:
        message = "Waring danger on front!"
        if gameMap[rr-2][rc] == 3:
            gameMap[rr-2][rc] = 4 
    
    elif gameMap[rr-3][rc] == 4 and gameMap[rr-3][rc] != 1:
        message = "ok!"
        gameMap[rr-3][rc] = 3


    else:
        message = "ok"


    gameMap[rr][rc] = 2

