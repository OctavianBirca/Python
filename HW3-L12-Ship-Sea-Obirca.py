


big_ship = int(input('Enter the ship coordonates: '))

grand_ship = 5



for x in range(1,11):
        
    if x == big_ship and x != grand_ship: #big ship
      print( "W", end="" )
    
#### the grand ship draw - start ####
    elif x == grand_ship and x == big_ship:
      print( "W", end="" )
    elif x == grand_ship-1 and x == big_ship-1:
        print( "w", end="" )  

    elif x == grand_ship+1 and x == big_ship+1:
        print( "w", end="" )  

#### the grand ship draw - end ####
    
    else:
      print( "~", end="" ) #the sea 
