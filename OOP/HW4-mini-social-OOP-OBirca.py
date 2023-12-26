class User:
    def __init__ (self, nickname, rating = 0, rating_points = 0, total_notes = 0, comments = None ):
        self.nickname = nickname
        self.rating = rating
        self.rating_points = rating_points
        self.total_notes = total_notes
        self.comments = comments if comments is not None else []


    def __str__ (self):
        return f"{self.nickname:>12} | {self.rating:6.1f} | {self.rating_points:4} | {self.total_notes:>5} | {len(self.comments)}"
    

    def totalPoints(self, points):
        self.points = points
        self.rating_points += self.points
        self.total_notes += 1
        self.ratingCalc()

   
    def ratingCalc (self):
        self.rating = self.rating_points / self.total_notes       
        return self.rating
        
    def notes (self, note):
        self.note = note()
        self.total_notes = self.notes + self.note 
        return self.total_notes
    
    #def commentsCounter (self, comment):
    #    self.comments += 1
    #    self.comment = comment
    #    return self.comments, self.comment
    
    def add_comment(self, comment):
        self.comments.append(comment)
         



######
        
def showList(list):
    print (f" ID |    Nickname | Rating |  Pts | Notes | Cmts ")

    print (f"----+-------------+--------+------+-------+------ ")
    for index, l in enumerate(list):
        print(f"{index+1:>3} |{l}")


def showMenu():
    print ()
    print ("== MENU==")
    print ("1. Add new User")
    print ("2. Rate a User")
    print ("3. Delete a User")
    print ("4. Add a comment:")
    print ("0. Exit")

def showUsersComments(list, id):
    user = list[id]
    print(user.comments)
        



users = []

users.append ( User("Marry", 0.0, 0, 0))
users.append ( User("John", 0.0, 0, 0))
users.append ( User("Kate", 0.0, 0, 0))
users.append ( User("Alex", 0.0, 0, 0))

select = -1

while select != 0:
    
    showList(users)
    showMenu()

    #users[1].totalPoints(5)

    select = int(input("Select: ") )

    if select == 1:
        new_user = input("User's Nickname: ")
        users.append ( User (new_user) )
        
    elif select == 2:
        sel_user = int (input("User's ID: "))
        new_points = int (input("Rate from 0 to 5: "))
        if new_points > 5:
            new_points = 5
        elif new_points < 0:
            new_points = 0

        users[sel_user-1].totalPoints(new_points)

    elif select == 3:
        sel_user = int (input("User's ID: "))
        users.pop (sel_user-1)

    elif select == 4:
        sel_user = int (input("User's ID: "))
        new_comment = input("Write the comment:")
        users[sel_user-1].add_comment(new_comment)
        

    elif select == 5:
        sel_user = int (input("User's ID: "))
        for c in users[sel_user-1].comments:
            print()
            print("-", c, "\n")
            
        
        c= input("press enter to continuue")

    elif select == 0:
        break

