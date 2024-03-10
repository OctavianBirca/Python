import psycopg2
from function import *
from Product import * 
import os



                                              
while True:
    print("Menu:")
    print("1: Show all products")
    print("2: Add a new product")
    print("3: Update a product")
    print("4: Delete a product")
    print("5: Find a product")
    print("6: Exit")

    option = input("Enter your choice: ")

    if option == '1':
        os.system('cls')
        showProductAll()

    elif option == '2':
            p1 = Product()
            product_id = getID('products') + 1
            price_id = getID('price') + 1
            stock_id = getID('stock') + 1

            product_name = input("Product Name: ")
            product_price = int(input("Product Price: ")) *100
            product_stock = int(input("Stock Quantity: "))
                                
            p1.add(product_id, product_name, price_id, product_price, stock_id, product_stock )

            showProductAll()

    elif option == '3':
            product_id = int(input("Product's id: "))
            product_name = input("Product's new Name: ")
            p1 = Product()
            p1.update(product_id, product_name)
            showProductAll()

    elif option == '4':
            product_id = int(input("Product's id: "))
            p1 = Product()
            p1.delete(product_id)
            showProductAll()

    elif option == '5':
            product_id = int(input("Product's id: "))
            p1 = Product()
            p1.find(product_id)
            
    
    elif option == '6':
            print("Exiting program.")
            break




