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

def short_chat(obj):
  """Return short description of weather object"""
  text = (f"""
  Forcast -- {obj.name} --
  City: {obj.city, obj.state, obj.country}
  Min: {obj.min} Max: {obj.max}
  Coldest: {temp_change(obj)[0]}
  Warmest: 
  UV Index: 
  Clothes: 
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
  print(short_chat)
  return None

long_chat(today)