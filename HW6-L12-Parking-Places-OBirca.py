#HW6-L12 - PARKING PLACES  - Octavian Birca

PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*5*PARKING_PLACES) # for a better reading i've changed from "#" * PARKING_PLACES * 5

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE:
        print("|   |", end="")
    
    else:
        print("| X |", end="")

print("\n","#"*5*PARKING_PLACES, sep="")  #as i can understand, the sep="" atribute is used to make a null space after "\n", which makes a new roow after end="" from if/else function