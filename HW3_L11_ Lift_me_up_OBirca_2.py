#HW1 Lesson 11 - Lift me up - Octavian Birca

from os import system

DIR_UP = -1
DIR_STOPPED = 0
DIR_DOWN = 1



building_roof = True
building_floors = 9
building_parking = True

lift_floor = 10
lift_open = False
lift_dir = DIR_STOPPED

human_floor = 5
human_in_lift = False 




############### Screen ################
system ('clear')
print('\n')

#---|-----|----
# R | < > |    
#---||---||----
# 9 || H ||     
#---||---||----
# 8 |     |     
#---|-----|----
# 7 |     |     
#---|-----|----
# 6 |     |     
#---|-----|----
# 5 |     |     
#---|-----|----
# 4 |     |     
#---|-----|----
# 3 |     |     
#---|-----|----
# 2 |     |  
#     {a}  
#---||---||----
# 1 || {} ||     
#---||---||----
# P |     |    
#---|-----|----
u = "=---="
h = ""






if building_roof:
    if lift_floor == 10:
             
        print (      f' R |     |    ')

    else:
        print (       '---|-----|----')      
        print (      f' R |     |    ')

    print (       f;)
    print (       f'---|{u}|----')
    print (f'{floor:^3}|{i}|{h} ')

for floor in range(9,0,-1): #floors
    
    
    
    #if floor == human_floor:
    #    h = ' H  '
    #else:
    #    h = '    '

    #if floor == human_in_lift:
    #    h = ' H  '
    #else:
     #   h = '    '
    
    if human_floor == lift_floor:
        human_in_lift = True
        human_floor = False
        lift_open = True
    
    
    if floor == human_floor:
        h = " H "
    else: 
        h = "   "

    

    if floor == lift_floor and human_in_lift == True:
        i = "| H |"
        u = "|---|" 

    elif floor == lift_floor and human_in_lift == False:
        i = "| x |"
        u = "|---|" 


    
    elif floor == lift_floor+1:
        if lift_open:
            i = " < > "
        elif lift_open == False:
            i = " > < "
        
    elif floor == lift_floor-1:
        i = "     "
    
        u = "|-=-|" 
    
    elif floor != lift_floor:
        
        i = "     "
        u = "-----"


    else:
        i = "     "

    

        
        
    
    print (       f'---|{u}|----')
    print (f'{floor:^3}|{i}|{h} ')
    

   
   

if building_parking:
    print (       '---|-----|----')      
    print (       ' P |     |    ')
    print (       '---|-----|----\n')   