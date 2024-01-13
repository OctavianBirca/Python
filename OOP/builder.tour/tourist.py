
class Tourist:
  def __init__(self,name,age):
    self.name = name
    self.age = age      


  def __gt__(self, other):
      if type(other) == int:
         return self.age > other
      else:
         return self.age > other.age
      
  def __ge__(self, other):
      if type(other) == int:
         return self.age >= other
      else:
         return self.age >= other.age
      
  def __eq__(self, other):
      if type(other) == int:
         return self.age == other
      else:
         return self.age == other.age
  
  def __le__(self, other):
      if type(other) == int:
         return self.age <= other
      else:
         return self.age <= other.age
      
  def __lt__(self, other):
      if type(other) == int:
         return self.age < other
      else:
         return self.age < other.age
  
  def __repr__(self) -> str:
     return self.__str__()

  def  __str__(self):
    if len(self.name) < 3 or self.age < 1:
        return f"ValueError"
    else:
        return f"{self.name} ({self.age} years)"
         



  

#list1 = [Tourist("ion", 33), Tourist("ida", 36), Tourist("oda",3)]

#print (list1[2])