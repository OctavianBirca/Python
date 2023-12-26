class Product:
  def __init__(self, name, price, rating):
    self.name = name
    self.price = price
    self.rating = rating


# 1. какую роль играет init() ? 
#    defineste caracteristicile obiectelor 
    
# 2. почему метод init - принимает аргумент self и откуда он берется?
#    It's some kind of Magic (c) Freddy Mercury
#    self - preia rolul de denumire a obiectului

  def __str__(self):
    return f' -= PRODUCT ("{self.name:<20}" ${self.price:>5.2f} {self.rating:>1.1f}) =-'

  def __gt__(self, other):
    return self.rating > other.rating
      
  def __lt__(self, other):
    return self.rating < other.rating
  

p1 = Product("Programming book", 100, 4.5)
p2 = Product("Hacking book",     150, 5.0)

print (p1)
print (p2)

if p1 > p2:
  print("First book is better")
elif p1 < p2:
  print("Second book is better")