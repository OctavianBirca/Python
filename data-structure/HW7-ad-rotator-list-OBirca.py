
from os import system
from time import sleep

# ads

ads = [
    "Black Friday!!! Buy now for only $ 99.99", 
    "Take your Python course for free", 
    "Today is the day!!!"

]

ads_time = [
    5, # Ad 1 - time in seconds
    3, # Ad 2 - time in seconds
    2, # Ad 3 - time in seconds

]

while True:
    ad = ads.pop(0)
    time = ads_time.pop(0)
    
    system("cls")
    print (" >> ", ad, " << ")
    
    sleep (time)

    ads.append(ad)
    ads_time.append(time)