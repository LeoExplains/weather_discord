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
  uv_recommendation(obj)
  rain_check(obj)
  check_description(obj)
  text = (f"""
Forcast -- {obj.name.title()} --
City: {obj.city}, {obj.state}, {obj.country}
{"-" * 20}
[ {obj.description.title()} ]
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
  uv_recommendation(obj)
  rain_check(obj)
  check_description(obj)
  """Return long description of weather object"""
  text = (f"""
  Forcast for {obj.name} in {obj.city},{obj.state},{obj.country}.
  It's going to be a top of {obj.temp_max} with a low of {obj.temp_min}.
  {obj.name.title()} will feel like
  Morning: {obj.feels_like_morn}
  Day: {obj.feels_like_day}
  Evening: {obj.feels_like_eve}
  Night: {obj.feels_like_night}
  {temp_change(obj)[4]}.
  {temp_change(obj)[5]}.
  {temp_change(obj)[7]}, with a difference between the min and max of {temp_change(obj)[6]}\u00B0c
  You might want to bring your {", ".join(str(x) for x in clothes_true())}
  {rain_check(obj)}
  {uv_recommendation(obj)}
  """)
  return text

#Recommendations
print(today.msg())
print(short_chat(today))
print(long_chat(today))