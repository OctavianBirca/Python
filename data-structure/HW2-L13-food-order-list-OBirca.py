
# order info 

order_food_names =    [ "Pizza", "Salad", "Soup" ]
order_food_price =    [  75.00 ,  45.00,   15.00 ]
order_food_quantity = [   2.00 ,   1.00,    2.00 ]
total_amount = 0


# iterative print

for i in range (len (order_food_names)):
        print (i+1, order_food_names[i], order_food_price[i], order_food_quantity[i])
        
        total_amount = total_amount+(order_food_price[i]*order_food_quantity[i])
        print (total_amount)
        
print ("TOTAL: ", total_amount)
