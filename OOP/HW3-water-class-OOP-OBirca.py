class Water:
    def __init__(self, volume = 0, temp = 18, state = "liquid"):
        ### water volume
        if type (volume) == int or type(volume) == float:
            self.volume = volume
            
        
        elif type(volume) == str\
         and volume in ["small", "medium", "large"]:
            if volume == "small":
                self.volume = 10
            elif volume == "medium":
                self.volume = 100
            elif volume == "large":
                self.volume = 1000

        else:
            print("ERROR! Wrong volume value!")

        ### water temperature
        self.temp = temp   


        ### water state
        if temp > 100:
            self.state = "vapor"

        elif temp <= 00:
            self.state = "solid"

        else:
            self.state = "liquid"

    #### Overloading str ####   
    def __str__(self):
        return f"WATER {self.volume}L | {self.temp}℃ | {self.state}"  
    
    #### Overloading length  #### 
    def __len__(self):
        return self.volume
    

    #### Overloading Addition / +   #### 
    def __add__ (self, other):
        if type(other) == int or type (other) == float:
            self.volume += other
            return self.volume 
        else:
            self.volume += other.volume

    
    #### Overloading Less than / <  #### 
    def __lt__(self, other):
        if type(other) == int or type (other) == float:
            return self.volume < other
        else:
            return self.volume < other.volume
        
    #### Overloading Less than or equal / <=  #### 
    def __le__(self, other):
        if type(other) == int or type (other) == float:
            return self.volume <= other
        else:
            return self.volume <= other.volume


    #### Overloading Equal / ==  #### 
    def __eq__(self, other):
        if type(other) == int or type (other) == float:
            return self.volume == other
        else:
            return self.volume == other.volume
        
    #### Overloading Not Equal / !=  #### 
    def __ne__(self, other):
        if type(other) == int or type (other) == float:
            return self.volume != other
        else:
            return self.volume != other.volume

    #### Overloading Greater than or equal / >=  #### 
    def __ge__(self, other):
        if type(other) == int or type (other) == float:
            return self.volume >= other
        else:
            return self.volume >= other.volume

    
    #### Overloading Greater than / >  #### 
    def __gt__(self, other):
        if type(other) == int or type (other) == float:
            return self.volume > other
        else:
            return self.volume > other.volume
        

#### HEATING Function
def heat (substance, deltaTemp = 0):
    result = substance.__class__ (substance.volume, substance.temp + deltaTemp, substance.state ) 
    return result

#### COOLING Function
def cool (substance, deltaTemp = 0):
    result = substance.__class__ (substance.volume, substance.temp - deltaTemp, substance.state ) 
    return result

           
###### TEST ######    
    
bottleWater = Water(500)
barWater = Water(750)


print (barWater >= 1000)

bottleWater + barWater

print(bottleWater)
print(type(bottleWater))


boiledWater = heat(bottleWater, -100)
print(boiledWater)
