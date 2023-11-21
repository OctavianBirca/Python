
from os import system

# LEGEND:
# 0 - Free
# 1 - Reserved
# 2 - Bought

seats = [ 0, 0, 0, 0, 0, 0, 0, 0]

option = -1
place = -1
exit = -1

while option != 0:

    # free and bought seats counter
    free_seats = 0
    bought_seats = 0
    for s in range(len(seats)):
        if seats[s] == 0: # free seats
            free_seats += 1
        
        elif seats[s] == 2: # bought seats
            bought_seats += 1

    ####### View #######

    system ("Cls")
    print()
    
    ### seats numerotation
    for s in range(len(seats)):
        print ("", s+1, "", end = "  ")
    print()


    ### seats booking view
    for s in range(len(seats)): 
        if seats[s] == 1:
            print ("|-|", end = "  ")
        
        elif seats[s] == 2:
            print ("|X|", end = "  ")
        
        else :
            print ("| |", end = "  ")
    
    print("\n\nFree seats  : ", free_seats, end=" | ")
    print("Bought seats: ", bought_seats)
    

    print("\n")
    
    #### MENU ######
    print ("MENU")
    print ("1. Book")
    print ("2. Buy")
    print ("3. Cancel")
    print ("0. Exit")
    
    

    while option != 0:
        
        option = int(input("MENU: "))

        if option < 0 or option > 3:
            print("Wrong Menu option, please try again!")
            continue
        
        # booking
        elif option == 1:
            place = int(input("Select a place to book: "))
            if place-1 <= 0 or place-1 >= len(seats): 
                print("Wrong place, please try again!")
                continue
            else: 
                seats[place-1] = 1
                break
                    
        
        # buy
        elif option == 2:
            place = int(input("Select a place to buy: "))

            if place-1 <= 0 or place-1 >= len(seats): 
                print("Wrong place, please try again!") 
                continue
            else: 
                seats[place-1] = 2
                break

            
        # cancel        
        elif option == 3:
            
            place = int(input("Select a place do cancel: "))
            

            if place <= 0 or place-1 >= len(seats): 
                print("Wrong place, please try again!") 
                continue

            elif seats[place-1] == 2: 
                print("Sorry the place can't be canceled")
                continue

            elif seats[place-1] == 0: 
                print("You have selected an empty seat! ")
                continue

            else:
                seats[place-1] = 0
                break
                

            

                
                
               
                    

                    
                    

        

