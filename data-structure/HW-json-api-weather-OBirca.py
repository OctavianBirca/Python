import requests

### Get City coordonates
def getCity(domain, endpoint, city, apikey):
    key = f"&appid={apikey}"
  
    adress = f"{domain}{endpoint}{city}{key}"
    reponse = requests.get(adress)
    data = reponse.json()
    
    if not data:
        print("The city was not found")
        return None, None
    else:
        lat = data[0]["lat"]
        lon = data[0]["lon"]

    return lat, lon

### Get City weather data
def getData(adress, info): # City=name / weather / main=temp / weather-icon=w-icon /  
    if info == "cod":       
        reponse = requests.get(adress)
        data = reponse.json()
        return data["cod"]
   
    elif info == "name":
        reponse = requests.get(adress)
        data = reponse.json()
        return data["name"]

    elif info == "weather":
        reponse = requests.get(adress)
        data = reponse.json()
        return data["weather"][0]["description"] 
    
        
    elif info == "main":
        reponse = requests.get(adress)
        data = reponse.json()
        return data["main"]["temp"] 
    
    elif info == "wind":
        reponse = requests.get(adress)
        data = reponse.json()
        return data["wind"]["speed"] 
    
    elif info == "w-icon":
        reponse = requests.get(adress)
        data = reponse.json()
        return data["weather"][0]["main"] 



### Get Icons
def getIcon (icon):
    if icon == "Thunderstorm":
        return "☇"
    
    elif icon == "Drizzle":
        return "🌦"
    
    elif icon == "Rain":
        return "⛆"
    
    elif icon == "Snow":
        return "❄"
    
    elif icon == "Mist":
        return "☉"
    elif icon == "Smoke":
        return "☉"
    elif icon == "Haze":
        return "☉"
    elif icon == "Dust":
        return "☉"
    elif icon == "Fog":
        return "☉"
    elif icon == "Sand":
        return "☉"
    elif icon == "Dust":
        return "☉"
    elif icon == "Ash":
        return "☉"
    elif icon == "Squall":
        return "☉"
    elif icon == "Tornado":
        return "☉"
    
    elif icon == "Clear":
        return "☀"
    
    elif icon == "Clouds":
        return "☁"


####### Weather app     ################################
    
while True:
    lang = input("Select the language en/fr/ro/ru: ")
    key = "9bfe943c8982b9ea74aee2a6275e62da"
    domain = "https://api.openweathermap.org"
    endpoint_coord = "/geo/1.0/direct?q="
    city = input ("Enter the city: ") 
    lat, lon = getCity(domain, endpoint_coord, city, key)

    endpoint = f"/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric&lang={lang}"

    adress = f"{domain}{endpoint}"

    
    if getData(adress, "cod") == 200:
        print("🏘 :", getData(adress, "name"))
        print(getIcon(getData(adress, "w-icon")), " :", getData(adress, "weather"))
        print(" ° :", getData(adress, "main",),  "℃")
        print("🌀:", getData(adress, "wind", ), "m/s")

    else :
        print ("Error", getData(adress, "cod"))











