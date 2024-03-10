import psycopg2


def getID(table):
    conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX(id) FROM {table}")
    last_id = cursor.fetchone()[0]

    if last_id == None:
        last_id = int(0)
    
    else:
        pass
        

    cursor.close()
    conn.close()

    return last_id

def showTable(table):
    conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    table_string = "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*12 + "+\n"
    table_string += "|  id  | price      |  quantity  |\n"
    table_string += "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*12 + "+\n"

    for row in rows:
        table_string += f"| {row[0]:^4} | {row[1]:^10} | {row[2]:^10} |\n"

    table_string += "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*12 + "+\n"

    print(table_string)




def showProductAll():
    conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
    cursor = conn.cursor()
    cursor.execute(f"""
                   SELECT products.ID, products.name, products.price_id, price.product_price, stock.id, stock.quantity 
                   FROM products
                   JOIN price ON products.price_id = price.id  
                   JOIN stock ON stock.product_id = products.id ; 
                   
""")
    rows = cursor.fetchall()
    print(f"Found {len(rows)} rows.")
    cursor.close()
    conn.close()

    table_string = "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*7 + "+" + "-"*8 + "+" + "-"*7 + "+" + "-"*11 +"+\n"
    table_string += "|  ID  | Prod Name  | pr ID |  price | st ID |  quantity |\n"
    table_string += "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*7 + "+" + "-"*8 + "+" + "-"*7 + "+" + "-"*11 +"+\n"

    for row in rows:
        table_string += f"| {row[0]:^4} | {row[1]:^10} | {row[2]:^5} | {row[3]/100:.2f} | {row[4]:^5} |  {row[5]:^6}  |\n"

    table_string += "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*7 + "+" + "-"*8 + "+" + "-"*7 + "+" + "-"*11 +"+\n"

    print(table_string)


def delete_rec(id, table):
    conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
    cursor = conn.cursor()
    cursor.execute(f"""
                  DELETE FROM {table}
                    WHERE 
                  id = {id};
                  
                   
""")
    conn.commit()
      
    cursor.close()
    conn.close()

    print ("Record deleted")

def showRecord(id, table):
    conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
    cursor = conn.cursor()
    cursor.execute(f"""
                   SELECT products.ID, products.name, products.price_id, price.product_price, stock.id, stock.quantity 
                   FROM products
                   JOIN price ON products.price_id = price.id  
                   JOIN stock ON stock.product_id = products.id  
                   WHERE {table}.id = {id};
                   
                """)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if row:
        table_string = "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*7 + "+" + "-"*8 + "+" + "-"*7 + "+" + "-"*11 +"+\n"
        table_string += "|  ID  | Prod Name  | pr ID |  price | st ID |  quantity |\n"
        table_string += "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*7 + "+" + "-"*8 + "+" + "-"*7 + "+" + "-"*11 +"+\n"

        table_string += f"| {row[0]:^4} | {row[1]:^10} | {row[2]:^5} | {row[3]:^6} | {row[4]:^5} |  {row[5]:^6}  |\n"

        table_string += "+" + "-"*6 + "+" + "-"*12 + "+" + "-"*7 + "+" + "-"*8 + "+" + "-"*7 + "+" + "-"*11 +"+\n"  

        print(table_string)
    
    else:
         print("The record with the ID: ", id, "in the table", table , "was not Found")

def updateRecord(id, name, table, new_name):

    conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
    cursor = conn.cursor()
    cursor.execute(f"""
                   UPDATE {table}
                   SET {name} = '{new_name}'
                   WHERE id = {id};
                   
                """)
    
    conn.commit()
    
    cursor.close()
    conn.close()





