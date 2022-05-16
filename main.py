from datetime import datetime, timedelta
from api import *
from check import *

# Help

def intro():
  my_date = datetime.now() + timedelta(days=7) 
  print(f"Hello I can forcast up to {my_date} for you")

  
# Display Results
intro()


location = get_lat_lon("cremorne")

# Command
try:
   city = (location[0], location[1], location[2])
   weather = get_current_weather(location[3], location[4])
   set_days_weather(weather, city)
except Exception:
   print("location not provided")

# Set recommendation
def clothes_true():
  result = list({k: v for k, v in clothes.items() if v == True})
  return result

def short_chat(obj):
  """Return short description of weather object"""
  text = (f"""
Forcast -- {obj.name.title()} --
City: {obj.city}, {obj.state}, {obj.country}
{"-" * 20}
{obj.description.title()}
Min: {obj.temp_min}\u00B0c || Max: {obj.temp_max}\u00B0c
Coldest time of day: {temp_change(obj)[0].title()} - {temp_change(obj)[1]}\u00B0c
Warmest time of day: {temp_change(obj)[2].title()} - {temp_change(obj)[3]}\u00B0c
Change over day: {temp_change(obj)[6]}\u00B0c
UV Index: {obj.uvi}
Chance of Rain: {obj.chance_of_rain:.1%}
Bring: {", ".join(str(x) for x in clothes_true())}
  """)
  return text

def long_chat(obj):
  # take all the other checks and prints out one block of text

  #Forcast for today

  #Temperature changes

  #Recommendations
  print(temp_change(obj))
  print(uv_recommendation(obj))
  print(rain_check(obj))
  print(clothes)
  check_description(obj)
  print(today.msg())
  print(short_chat(obj))
  return None

long_chat(today)