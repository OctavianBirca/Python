
def drawLine( length, direction ):
    
    if direction == "v":
        for i in range (length): 
            print("|")
    
    elif direction == "h":
        for i in range(length):
            print("-", end="")
        

line_lenght = int(input("Type line's lenght: "))
line_orientation = input("Type h for horizontal of v for vertical: ")


drawLine(line_lenght, line_orientation)
        
