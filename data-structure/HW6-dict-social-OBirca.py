

user = {

    "username" : "Octavian",
    "online"   : False,
    "email"    : "octav@birca.com",
    "rating"   : 165465321,
    "friends"  : [
        "Jean", 
        "Fred",
        "Pierre",
    ]
    
}


####### Add new friends #######
new_friend = None

while True:
    print("To finish press ENTER")
    new_friend = input("Add a new friend's name: ")
    user["friends"].append(new_friend)

    if new_friend == "":
        user["friends"].remove(new_friend)

        break  # Exit the loop if input is empty


####### show user status ######
print()
print("== USER STATUS ==")

if user["online"] == True:
    print ("🤨", user["username"], "✅")
else:
    print ("🤨", user["username"], "⛔")
    
print ("🖄 ", user["email"] )

likes = None

if user["rating"] == 0 or user["rating"] < 1000:
    print ("💙", user["rating"] )

elif user["rating"] == 1000 or user["rating"] < 1000000:
    likes = user["rating"] // 1000
    print ("💙", str(likes) + "M" )

elif user["rating"] >= 1000000 :
    likes = user["rating"] // 1000000
    print ("💙", str(likes) + "T" )


###### friends list
print("\n Friends:")

for f in range(len(user["friends"])):
    print ("👫", user["friends"][f])

print()

