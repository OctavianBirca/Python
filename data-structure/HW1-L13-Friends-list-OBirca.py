

friends = []

while len (friends) < 100:
    name = input ('Add friend name: ')
  # exit if enter
    if name == '': 
        break
  # check if the input name exists in the list
    if name in friends:
        print("The name exists")
        continue
    friends.append (name)


print ("You have", len (friends), "friends")
for i in range (len(friends)):
    print(f"  {i}.  {friends[i]}")
