

SCALE  = 10

hX = 5
hY = 4

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY: #Helicopter
            map += "🚁"
        #Danger Area
        elif x == hX-1 and y == hY-1:
            map += "🔸"
        elif x == hX and y == hY-1:
            map += "🔸"
        elif x == hX+1 and y == hY-1:
            map += "🔸"    

        elif x == hX-1 and y == hY:
            map += "🔸"
        elif x == hX+1 and y == hY:
            map += "🔸"

        elif x == hX-1 and y == hY+1:
            map += "🔸"    
        elif x == hX and y == hY+1:
            map += "🔸"    
        elif x == hX+1 and y == hY+1:
            map += "🔸"    

         #Wind Area
        
        elif x == hX-2 and y == hY-2:
            map += "⤳ "
        elif x == hX-1 and y == hY-2:
            map += "⤳ "    
        elif x == hX and y == hY-2:
            map += "⤳ "    
        elif x == hX+1 and y == hY-2:
            map += "⤳ "
        elif x == hX+2 and y == hY-2:
            map += "⤳ "
        

        elif x == hX-2 and y == hY-1:
            map += "⤳ "
        elif x == hX+2 and y == hY-1:
            map += "⤳ "   

        elif x == hX-2 and y == hY:
            map += "⤳ "
        elif x == hX+2 and y == hY:
            map += "⤳ "   

        elif x == hX-2 and y == hY+1:
            map += "⤳ "
        elif x == hX+2 and y == hY+1:
            map += "⤳ "   


        elif x == hX-2 and y == hY+2:
            map += "⤳ "
        elif x == hX-1 and y == hY+2:
            map += "⤳ "    
        elif x == hX and y == hY+2:
            map += "⤳ "    
        elif x == hX+1 and y == hY+2:
            map += "⤳ "
        elif x == hX+2 and y == hY+2:
            map += "⤳ " 
    
        else:
            map += "  "

    map += "\n"                

print(map)