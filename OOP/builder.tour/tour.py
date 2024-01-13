from money import Money
from datetime_1 import Period
from tourist import Tourist
from datetime import date

_destinations = (
                 { "name": "Greece", "description": "Mythical Landscapes", "price": Money(100,"EUR")},
                 { "name": "France", "description": "Chic Romance","price": Money(120,"EUR")},
                 { "name": "Italy", "description": "Baroque Splendor","price": Money(200,"EUR")}, 
                 { "name": "USA", "description": "Boundless Horizons","price": Money(300,"USD")})


class _Tour:
  def __init__(self,destination, tourists, period):
    self.destination = destination
    for d in range(len(_destinations)):
        if self.destination == _destinations[d]["name"]:
            self.destination = _destinations[d]["name"]
            self.name = _destinations[d]["description"]
            self.price = _destinations[d]["price"]
        
    self.period = period      
    self.tourists = tourists
    
      
    self.cost = self.calculateCost()


  def calculateCost(self):
    self.total = Money(0, "EUR")
    self.cost_list = [self.total]
    for t in range(len(self.tourists)):
      
      if self.tourists[t] < 1 :
        self.person = Money(0, "MDL") 
        self.cost_list.append(self.person)
        self.cost_list[0] = Money(self.cost_list[0] + self.total, "MDL")
        t += 1
      
      elif  self.tourists[t] <= 6:
        self.person = self.price * 0.5
        self.cost_list.append(Money(self.person, "MDL"))
        self.cost_list[0] = Money(self.cost_list[0] + self.total, "MDL")
        
        t += 1

      elif 7 <= self.tourists[t]  <= 15:
        self.person = self.price * 0.75
        self.cost_list.append(Money(self.person, "MDL"))
        self.cost_list[0] = Money(self.cost_list[0] + self.person, "MDL")
        t += 1
          
      elif self.tourists[t] >= 16 :
        self.total = self.price * 1 
        self.cost_list.append(Money(self.total, "MDL"))
        self.cost_list[0] = Money(self.cost_list[0] + self.total, "MDL")
        t += 1
      
     
      

    return self.cost_list
    
      
  def __str__(self):
        
    return f"Destination: {self.destination}, the {self.name} \n Dates: {self.period} \n Tourists: {self.tourists} \n Price: {self.cost}"
         


class TourBuilder:
  def __init__(self,destination, tourists,period):
    self._tour = _Tour(destination,tourists,period)
    self.ensurance = False
    self.guide = False
    self.ensurance_cost = Money(self._tour.cost[0]*0.05, "MDL")
     
    
    if self._tour.destination == "Greece" or self._tour.destination == "Italy" or self._tour.destination == "France":
      self.currency =  "EUR"
    elif _Tour.destination == "USA":
      self.currency =  "USD"
    elif _Tour.destination == "Russia":
      self.currency =  "RUB"

    self.guide_cost = Money(100, self.currency)


  def build(self):
    return self._tour 
  
  def withEnsurance(self):
    self.ensurance = True
    self._tour.cost[0] = Money(self._tour.cost[0]+self.ensurance_cost, "MDL") 
    return self 
    
  def getEnsuranceCost(self):
    return self.ensurance_cost  
  
  def withGuide(self):
    self.guide = True
    
    self._tour.cost[0] = Money(self._tour.cost[0] +self.guide_cost, "MDL")

    return self 
    
  def getEnsuranceCost(self):
    return self.ensurance_cost  
  
  def getGuideCost(self):
    return self.guide_cost









