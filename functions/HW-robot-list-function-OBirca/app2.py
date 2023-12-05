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

    
    
    

    if gameMap[rr][rc+2] == 3 or gameMap[rr][rc-2] == 3 or gameMap[rr+2][rc] == 3 or gameMap[rr-2][rc] == 3:
        message = "Warning! Danger!"
        if gameMap[rr][rc+2] == 3:
            gameMap[rr][rc+2] = 4
        elif gameMap[rr][rc-2] == 3:
            gameMap[rr][rc-2] = 4
        elif gameMap[rr+2][rc] == 3:
            gameMap[rr+2][rc] = 4 
        elif gameMap[rr-2][rc] == 3:
            gameMap[rr-2][rc] = 4 

     
    elif gameMap[rr][rc+3] == 4 or gameMap[rr][rc-3] == 4 or gameMap[rr+3][rc] == 4 or gameMap[rr-3][rc] == 4:
        message = "ok"
        if gameMap[rr][rc+3] == 4:
            gameMap[rr][rc+3] = 3
        elif gameMap[rr][rc-3] == 4:
            gameMap[rr][rc-3] = 3
        elif gameMap[rr+3][rc] == 4:
            gameMap[rr+3][rc] = 3 
        elif gameMap[rr-3][rc] == 4:
            gameMap[rr-3][rc] = 3 
    
    else: 
        if gameMap[rr][rr] == 4:
            gameMap[rr][rr] = 3
        
            


    gameMap[rr][rc] = 2

