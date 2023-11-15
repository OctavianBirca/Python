

# the list

people = ["Johnny", "Mary", "Francis", "Albert", "David"]

# print the list
print("INDEX | NAME")
print("="*20)

for p in range(len(people)):
    print (f"   {p}  | {people[p]}")
    print ("-"*20)

print()

# input first value and check if it's valid
while True:
    print()
    first_value  = int(input("Input the first value to be switched: "))
    if first_value > len(people):
        print("Error! The value is no valid")
    else: 
        break


# input second value and check if it's valid
while True:
    print()
    second_value = int(input("Input the second value to be switched: "))
    if second_value > len(people):
        print("Error! The value is no valid")   
    else: 
        break

# message for the same values
if second_value == first_value:
    print("You have input the same value")   


# switching the values
temp = people[first_value]
people[first_value] = people[second_value]
people[second_value] = temp


# print updated list
for p in range(len(people)):
    print (f"   {p}  | {people[p]}")
    print ("-"*20)
