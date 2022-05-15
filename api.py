## Getting Weather Data from API calls to https://openweathermap.org/api/one-call-api & https://openweathermap.org/api/air-pollution and mapping them to an object

import json
import os
import requests
from datetime import datetime

weather_api = os.environ['WEATHER_API']

class weather_of_day:
  """Object for storing weather data"""
  def __init__(self):
    self.city = ""
    self.lat = 0
    self.lon = 0
    self.state = ""
    self.country = ""
    self.datestring = 0
    # conditions
    self.uvi = 0
    self.description = ""
    self.humidity = 0
    self.chance_of_rain = 0
    self.rain = 0
    self.windspeed = 0
    self.windgust = 0
    #temp
    self.temp_min = 0
    self.temp_max = 0
    self.temp_night = 0
    self.temp_eve = 0
    self.temp_day = 0
    self.temp_morn = 0
    #feels like temp
    self.feels_like_night = 0
    self.feels_like_eve = 0
    self.feels_like_day = 0
    self.feels_like_morn = 0
    #pollution if available
    self.aqi = 0
  def msg(self):
    return f"""This is the weather object
    City: {self.city},
    State: {self.state},
    Country: {self.country},
    Lat: {self.lat},
    Lon: {self.lon},
    Country: {self.country},
    Date Time: {self.datestring},
    Date Time Text: {datetime.utcfromtimestamp(self.datestring)},
    -----
    UV Index: {self.uvi},
    Description: {self.description},
    Humidity: {self.humidity}%,
    Chance of Rain: {self.chance_of_rain:.02%},
    Rainfall: {self.rain},
    Air Quality Index: {self.aqi},
    Wind Speed: {self.windspeed},
    Wind Gust: {self.windgust},
    -----
    Min: {self.temp_min}\u00B0c,
    Max: {self.temp_max}\u00B0c,
    -----
    Morning: {self.temp_morn}\u00B0c,
    Day: {self.temp_day}\u00B0c,
    Evening: {self.temp_eve}\u00B0c,
    Night: {self.temp_night}\u00B0c,
    -----
    Feels like Morning: {self.feels_like_morn}\u00B0c,
    Feels like Day: {self.feels_like_day}\u00B0c,
    Feels like Evening: {self.feels_like_eve}\u00B0c,
    Feels like Night: {self.feels_like_night}\u00B0c,
    """

def get_lat_lon(city):
  """ This is code for setting a lat, lon from a location name (lat, lon)"""
  response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=10&appid={weather_api}")
  location = json.loads(response.text)
  for i, j in enumerate(location):
    coord = (location[i]['name'],location[i]['country'],location[i]['state'],location[i]['lat'], location[i]['lon'])
    print(coord)
    choice = input(f"""is this the right location? (y/n): """)
    if choice.lower() == "y":
      return(coord)
    else:
      continue
  return(-1)


def get_current_weather(lat, lon):
  """ This is code for getting current weather at set lat and lon coordinates"""
  response = requests.get(f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={weather_api}&units=metric")
  temp = json.loads(response.text)
  return temp

#objects created manually as it's limited to 7 days in the API
today = weather_of_day()
tomorrow = weather_of_day()
two_days = weather_of_day()
three_days = weather_of_day()
four_days = weather_of_day()
five_days = weather_of_day()
six_days = weather_of_day()
seven_days = weather_of_day()

days = [today, tomorrow, two_days, three_days, four_days, five_days, six_days, seven_days]

def set_days_weather(data, city):
  """Initalizes objects in days array with data from api response"""
  day_list = data['daily']
  for i, j in enumerate(data):
    days[i].city = city[0]
    days[i].state = city[2]
    days[i].country = city[1]
    days[i].lat = data['lat']
    days[i].lon = data['lon']
  for i, j in enumerate(day_list):
    days[i].datestring = j['dt']
    days[i].description = j['weather'][0]['description']
    days[i].uvi = j['uvi']
    days[i].humidity = j['humidity']
    days[i].chance_of_rain = j['pop']
    if 'rain' in j:
      days[i].rain = j['rain']
    days[i].windspeed = j['wind_speed']
    days[i].windgust = j['wind_gust']
    days[i].temp_min = j['temp']['min']
    days[i].temp_max = j['temp']['max']
    days[i].temp_night = j['temp']['night']
    days[i].temp_eve = j['temp']['eve']
    days[i].temp_day = j['temp']['day']
    days[i].temp_morn = j['temp']['morn']
    days[i].feels_like_night = j['feels_like']['night']
    days[i].feels_like_eve = j['feels_like']['eve']
    days[i].feels_like_day = j['feels_like']['day']
    days[i].feels_like_morn = j['feels_like']['morn']
  return None

