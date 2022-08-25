import wikipedia
import requests, json
import random
import math

#this is all old code from NoFsHere/JoeTheChatBot. not even going to try to comment all of this 

def weathersection():
  api_key = "4ffee1e418062d81fa80423119db1262"

  base_url = "http://api.openweathermap.org/data/2.5/weather?"

  city_name = cityplace

  complete_url = base_url + "appid=" + api_key + "&q=" + city_name

  response = requests.get(complete_url)

  x = response.json()

  if x["cod"] != "404":

    y = x["main"]
    
    current_temperature = y["temp"]
   
    current_pressure = y["pressure"]

    current_humidity = y["humidity"]

    z = x["weather"]
    celcisus_temp = current_temperature - 273.15
    fahrenheit_temp1 = celcisus_temp * ( 9 / 5 ) + 32
    fahrenheit_temp = round(fahrenheit_temp1)

    weather_description = z[0]["description"]
 
    if fahrenheit_temp > 60:
      isnice = True
    else:
      isnice = False
  if isnice == True:
    goodweather = input(f"Nice Weather Today!, {fahrenheit_temp} and {weather_description} ")
  else:
    badweather = input(f"The Weather really sucks today, {fahrenheit_temp} and {weather_description}")
  
def interestsection():
  #Interest section starts here
  interest = input("What are you interested in? ")
  interestinfo = wikipedia.summary(interest ,sentences=1, auto_suggest= False)
  print(f"I love {interest}, heres what I know about {interest}: {interestinfo}")
  print("     ")
  intspecific = input(f"What is your favorite thing about {interest}? ")
  print(f"{intspecific} is my favorite thing about {interest} too!")
  #Interest section ends here
bye = ["bye", "Goodbye", "Bye", "goodbye", "Cya", "say goodbye", "ayo thx fr talkin to me c u ltr m8", ]
def chatbot():
  start = input("Hello ")
  name = input("What is your name? ")
  global cityplace 
  cityplace = input("Where Do you live? ")
  doing = input("Are you feeling good? ")
  if doing == 'no':
    sad = input("why are you feeling sad? ")
    print("thats sad")
    keepgoing = input("Do you think a chat would cheer you up? ")
    if keepgoing == "yes":
      interestsection()
      weathersection()  
    else:
      print(f"{random.choice(bye)} Its been great chatting with you!")
  if doing == 'yes':
    interestsection()
    weathersection()
    print(f"{random.choice(bye)} {name} It's Been Nice Chatting With You")