from money import Money
from datetime_1 import Period
from tourist import Tourist
from datetime import datetime
from tour import *


tour_data = TourBuilder("Italy",[Tourist("John Doe", 21), Tourist("Jane Doe", 30), Tourist("Jenny", 6)],Period("01.01.2021", "02.01.2021")).withGuide().withEnsurance()

tour = tour_data.build()

print (f"Destination: {tour.destination}")
print (f"       Name: {tour.name}")
print (f"      Dates: {tour.period}")
print (f"   Tourists: ", end="")

for l in range(len(tour.tourists)):
    print (f'{tour.tourists[l]} - {tour.cost[l+1]} ', end="\n\t     ")

print()

print (f"  Ensurence: {tour_data.getEnsuranceCost()}")   
print (f"      Guide: {tour_data.getGuideCost() }") 
print (f"      Total: {tour.cost[0] }") 

