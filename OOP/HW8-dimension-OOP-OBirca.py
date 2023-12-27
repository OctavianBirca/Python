from os import system


class Bar:
    units = ('mm', 'cm', 'dm', 'm')

    def __init__ (self, value, unit):
        self.value = value

        self.unit = unit
        for u in range(len(self.units)):
            if self.unit == self.units[u]:
                if self.unit == self.units[3]:
                    self.value = self.value * 1000
                    self.unit = self.units[0]
                elif self.unit == self.units[2]:
                    self.value = self.value * 100
                    self.unit = self.units[0]
                elif self.unit == self.units[1]:
                    self.value = self.value * 10
                    self.unit = self.units[0]

                else: print("wrong value")


    def __str__(self):
        return f"{self.value:>5} {self.unit}"
    

    def __add__(self, other):
        return Bar(self.value + other.value, self.unit) 

    ### 

def menu():
    print()
    print("----Action----")
    print(" 1. Add a rail")
    print(" 0. Exit")

def showList(list, total):
    print("  -= ORDER =-\n")
    for l in range(len(list)):
        print ("-Bar ", list[l] )


    print()
    print ("Total:", total )


order = []
select = -1
total = Bar (0, "mm")


while select != 0:
    system ("cls")

    showList(order, total)


    menu()


    select = int(input( ">>"))

    if select == 1:

        ord_value = int(input("Lenght = "))
        

        ord_unit = input ("unit = ")

        order_rail = Bar (ord_value, ord_unit)

        print(order_rail)

        order.append (order_rail)

        total = total + order_rail

        

    elif select == 0:
        break



    else:
        continue

    print ("Total:", total )



    