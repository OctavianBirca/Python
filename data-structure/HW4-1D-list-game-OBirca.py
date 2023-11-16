from os import system

option = '' 
over = False
robo_x = 5 # robot start position
gmap = [' ', ' ', ' ', 'x', ' ', 'o', ' ', 'x', ' ', ' ',] 
#index   0    1    2    3    4    5    6    7    8    9
hp = 100
health = ["▀", "▀", "▀", "▀",]
h_draw = 4

while option != "x" :
    ############## print the map #################
    system ("clear")
    if hp == 0:
        print("Game Over")
        break


    print ("❤", hp, end=" ")

    for h in range(h_draw):
        print (health[h], end ="")
    

    print("\n")
    print ("-"*20)
    
    for i in range(len(gmap)):
        print (gmap[i], end=" ")

    print()
    print ("-"*20)

    
    print ("\n\n\t a - left | x - exit | d - left")

     ############## end print the map #################


    ############## CONTROLS #################

    option =  input ('>>')
    
    if option == 'a' and robo_x > 0:
        gmap[robo_x] = ' '
        robo_x -= 1
        if gmap[robo_x] == "x":
            gmap[robo_x] = "X"
            over = True
            hp -= 50
            h_draw -= 2


            

        else: 
            gmap[robo_x] = "o"

    
    elif option == 'd' and robo_x < len(gmap)-1: 
        gmap[robo_x] = ' '
        robo_x += 1
        if gmap[robo_x] == "x":
            gmap[robo_x] = "X"
            over = True
            hp -= 50
            h_draw -= 2

            
            

        else: 
            gmap[robo_x] = "o"

    elif option == 'x':
        print ("GAME OVER")