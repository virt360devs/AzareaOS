#again, old code. you can tell this is from github lol
import requests, json
def weather():
 # Enter your API key here
  api_key = "4ffee1e418062d81fa80423119db1262"
  # base_url variable to store url
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  # Give city name
  city_name = input("what citys weather do you want?")
  # complete_url variable to store
  # complete url address
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  # get method of requests module
  # return response object
  response = requests.get(complete_url)
  # json method of response object
  # convert json format data into
  # python format data
  x = response.json()
  # Now x contains list of nested dictionaries
  # Check the value of "cod" key is equal to
  # "404", means city is found otherwise,
  # city is not found
  if x["cod"] != "404":
    # store the value of "main"
    # key in variable y
    y = x["main"]
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
    z = x["weather"]
    celcisus_temp = current_temperature - 273.15
    fahrenheit_temp1 = celcisus_temp * ( 9 / 5 ) + 32
    fahrenheit_temp = round(fahrenheit_temp1)
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
    # print following values
  print(f"the weather in {city_name} is {fahrenheit_temp} and {weather_description} ")