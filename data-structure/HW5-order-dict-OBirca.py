from os import system

system("clear")

print()
print("===============ORDER===============\n")

order = {
    "name" : "", 
    "pizza": "", 
    "price": "",
 "quantity": "",
    "total": "",
"discount" : 0.1,
"delivery" : 30,
    }

discount_view = order["discount"] * 100 

order["name"] = input("Client's name: ")

print("\n 1. Pizza Royal - 30.00 \n 2. Pizza 4 Fromages - 35.00 \n 3. Pizza Vegan - 43.00 \n")



while True:
    pizza = input("Please select a pizza: ")


    if pizza == "1":
        order["pizza"] = "Royal"
        order["price"] = 30.00
        break
        

    elif pizza == "2":
        order["pizza"] = "4 Fromages"
        order["price"] = 35.00
        break
        

    elif pizza == "3":
        order["pizza"] = "4 Fromages"
        order["price"] = 43.00
        break
        
    else:
        print ("Wrong input")
        continue    
    
    
print ("   Pizza:", order["pizza"], "selected")

order["quantity"] = int(input("How many? "))

order["total"] = order["price"] * order["quantity"]

discount = input ("Do you have a discount card y/n: ")


if discount == "y":
    order["total"] = order["price"] * order["quantity"] * order["discount"]
elif discount == "n": 
    order["total"] = order["price"] * order["quantity"]

if order["total"] > 300:
    order["delivery"] = 0

else: 
    
    order["total"] = order["price"] * order["quantity"] * order["discount"] + order["delivery"]


system("clear")

print ("=========TOTAL ORDER=========\n")
print ("  Client:", order["name"])
print ("   Pizza:", order["pizza"])
print ("   Price:", order["price"], )
print ("      x :", order["quantity"], "pcs")

order["total"] = order["price"] * order["quantity"]

print ("   Total:", order["total"])


if discount == "y":
    order["total"] = order["total"] - (order["total"] * order["discount"])
elif discount == "n":
    order["discount"] = 0 
    discount_view = 0
    

print ("Discount:", discount_view,"%")

if order["total"] > 300:
    order["delivery"] = 0
    order["total"] = order["total"] + order["delivery"]
    
else: 
    order["total"] =  order["total"] + order["delivery"]
    

print ("Delivery:", order["delivery"])
print ("   TOTAL:", order["total"])
print ()

