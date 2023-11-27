from os import system


people = ["Marry", 20, "John", 21, "Peter", 22, "Mihai", 25]
n = 0
a = 0
alt_counter = 0
people_names = []
people_ages = []
option = -1

system ("Cls")

### Separation of the main list on 2 lists
def separateList(item, list, str_list, int_list):
    for item in range(len(list)):

        if  type(list[item]) == str:
        
            str_list.append(list[item])

        elif type(list[item]) == int:
        
            int_list.append(list[item])


separateList(n, people, people_names, people_ages)


### Show 2 lists in a table
def showListFrom2Lists(item, str_name_list, int_list):
    for item in range(len( str_name_list)):
        print(f" {item} - { str_name_list[item]:12} - {int_list[item]} years")
        
showListFrom2Lists(n, people_names, people_ages)

### count main list by strig types
def countListByString(item, list, counter):
    for item in range(len(list)):

        if  type(list[item]) == str:
        
            counter += 1
        
    print(counter, "people in the list")


### count main list by int

def countListByIndex(item, list, counter):
    counter = 0
    for item in range(len(list)):
        if (item + 2) %2 == 0:
            counter += 1
    
        
    print(counter, "people in the list")

countListByIndex(n, people, a)


### Menu
def showMenu ():
    print()

    print("Menu")
    print("1. Find a person by his index")
    print("2. Find person a person")
    print("3. Change person's age")
    print("4. Delete a person from the list")
    print("5. Add a person")
    print("6. Inser a new a person")
    

    select = int(input("Select: "))

    return select


# select a item by its index
def selectByIndex(index, list, list2):
    
    if index < 0 or index > len(list):
        print("Sorry, this index does not exist")  

    else: 
        print (index, "|", list[index], "|", list2[index] )

    print()


# search a person by his name

def searchByName(name, list, list2):
    for item in range(len(list)):
        item_found = list[item] == name
        
        if item_found:  
            list_index = list.index(name) 

            break

    if item_found:
        print (name, "age", list2[list_index])
    
    else: 
        print (name, "not found!") 


# change person's age

def changeAge(name, list, list2):
    for item in range(len(list)):
        item_found = list[item] == name
        
        if item_found:

            print (list[item])
            break

    if item_found:
        new_age = input ("Person's age: ")

        list2[list.index(name)] = new_age

        print (list[list.index(name)], "age", list2[list.index(name)], "changed" )
        return new_age

    else: 
        print (name, "not found!") 


# delete item from a list1 and list 2 

def deletePerson(name, list, list2):
    for item in range(len(list)):
        item_found = list[item] == name
        
        if item_found:
            
            print (list[item], list2[item])
            print( list.index(name))
            break

    if item_found:
            person_index = list.index(name)
            print(person_index)
            list.pop(person_index)
            list2.pop(person_index) 
                       

    else: 
        print (name, "not found!") 


# add a new item in a list

def append_in_list(input_text, list):
    item = input(input_text)
    list.append(item)

# insert a new item in a list

def insert_in_list(input_text, list, position):
    item = input(input_text)
    list.insert(position, item)

 
    

while option != 0:

    system ("Cls")
    countListByString(n, people_names, a)
    showListFrom2Lists(n, people_names, people_ages)
    
    option = showMenu()


    if option == 1:
        s1 = int(input("Type the index: "))
        selectByIndex(s1, people_names, people_ages)
        out = input("Type enter to continue ")
        if out == "":
            continue
        

    elif option == 2:
        s2 = input("Select a person by his name: ")
        searchByName(s2, people_names, people_ages)
        out = input("Type enter to continue ")
        if out == "":
            continue
        
    elif option == 3:
        s3 = input("Input the person's name: ")
        changeAge(s3, people_names, people_ages)
        out = input("Type enter to continue ")
        if out == "":
            continue
        
    elif option == 4:
        s4 = input("Input the person's name to delete: ")
        deletePerson(s4, people_names, people_ages)
        out = input("Type enter to continue ")
        if out == "":
            continue

    elif option == 5:
        append_in_list("Person's Name: ", people_names)
        append_in_list("Person's Age: ", people_ages)
        out = input("Type enter to continue ")
        if out == "":
            continue    

    elif option == 6:
        pos = int(input("Input the position: "))
        insert_in_list("Person's Name: ", people_names, pos)
        insert_in_list("Person's Age: ", people_ages, pos)
        out = input("Type enter to continue ")
        if out == "":
            continue

    elif option == 0:
        break


    else:
        print("Sorry, wrong value ")
        continue
        







