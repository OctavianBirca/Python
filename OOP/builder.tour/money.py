class Money:
    _currencies = ("MDL","USD","EUR","RUB","RON")
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency
       
        for c in range(len(self._currencies)):
            if self.currency == self._currencies[0]:
                self.amount = self.amount
                self.currency = "MDL"

            elif self.currency == self._currencies[1]:
                self.amount = self.amount*17.75
                self.currency = "MDL"

            elif self.currency == self._currencies[2]:
                self.amount = self.amount*19.49
                self.currency = "MDL"

            elif self.currency == self._currencies[3]:
                self.amount = self.amount*0.20
                self.currency = "MDL"

            elif self.currency == self._currencies[4]:
                self.amount = self.amount*3.92
                self.currency = "MDL"
            
            else: 
                self.currency = "000"


    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.amount + other
        else:
            return self.amount + other.amount
      
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.amount * other
        else:
            return self.amount * other.amount


    def __repr__(self) -> str:
        return self.__str__()

    def  __str__(self):
        if self.currency == "MDL" and self.amount >= 0:
            return f" {self.amount:.2f} {self.currency}"
        
        else:
            return f"ValueError/TypeError"

    

          
    
    #return ???      # e.g. "100.00MDL"
  
#lei = Money(100, "EUR")

#print (lei)