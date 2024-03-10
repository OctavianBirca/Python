import psycopg2

class Product:
    def __init__(self):
        self.id = None
        self.name = None
        self.price_id = None  
        self.price = None
        self.stock_id = None 
        self.quantity = None     

    def add(self, id, name, price_id, price, stock_id, quantity):
        self.id = id
        self.name = name
        self.price_id = price_id  
        self.price = price
        self.stock_id = stock_id 
        self.quantity = quantity    

        conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
        cursor = conn.cursor()

        
        sql = f"""

                BEGIN;
                INSERT INTO "price" VALUES ({price_id}, {self.price}, 'EUR');
                INSERT INTO "products" VALUES ({id}, '{self.name}', {self.price_id});
                INSERT INTO "stock" VALUES ({self.stock_id}, {self.id}, {self.quantity});                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                COMMIT;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
              
        """

        cursor = conn.cursor()
        cursor.execute(sql)

        cursor.close()
        conn.close()




    def delete(self, id):
        self.id = id
         
        conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
        cursor = conn.cursor()

        try:
            cursor.execute("""
                BEGIN;
                DELETE FROM "stock" WHERE id = %s;
                DELETE FROM "products" WHERE id = %s;         
                DELETE FROM "price" WHERE id = %s;
                
                 
                COMMIT;
            """, (self.id, self.id, self.id))
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            print("Error deleting from database:", e)
        finally:
            cursor.close()
            conn.close()


    def update(self, id, new_value):
        self.id = id
        self.new_value = new_value

        conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
        cursor = conn.cursor()
        cursor.execute(f"""
                    UPDATE products
                    SET name = '{self.new_value}'
                    WHERE id = {self.id};
                    
                    """)
        
        conn.commit()
        
        cursor.close()
        conn.close()

    def find(self, id):
        self.id = id
        conn = psycopg2.connect("dbname=e-shop user=postgres password=qazwsx")
        cursor = conn.cursor()
        cursor.execute(f"""
                    SELECT products.ID, products.name, products.price_id, price.product_price, stock.id, stock.quantity 
                    FROM products
                    JOIN price ON products.price_id = price.id  
                    JOIN stock ON stock.product_id = products.id  
                    WHERE products.id = {id};
                    
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
            print("The record with the ID: ", id, "in the table products", "was not Found")