from datetime import datetime, timedelta
from api import *
from check import *

def intro():
  my_date = datetime.now() + timedelta(days=7) 
  return(f"""Hello I'm Weather Bot. 
I can forcast from today ( {datetime.now():%d.%m.%Y} ) to 7 days ahead ( {my_date:%d.%m.%Y} ) for you""")

def set_user_location(location):
  try:
     city = (location[0], location[1], location[2])
     weather = get_current_weather(location[3], location[4])
     set_days_weather(weather, city)
  except Exception:
     print("location not provided")
  return location


def short_chat(obj):
  """Return short description of weather object"""
  uv_recommendation(obj)
  rain_check(obj)
  check_description(obj)
  bring = ", ".join(str(x) for x in clothes_true())
  text = (f"""
:satellite: Forcast -- {obj.name.title()} -- :wave:
{"+" * 20}
:cityscape: - City: {obj.city}, {obj.state}, {obj.country}
{"-" * 20}
[ {obj.description.title()} ]
{"-" * 20}
:thermometer: Min: {obj.temp_min}\u00B0c || Max: {obj.temp_max}\u00B0c
:blue_square: Coldest time of day: {temp_change(obj)[0].title()} ~ {temp_change(obj)[1]}\u00B0c
:orange_square: Warmest time of day: {temp_change(obj)[2].title()} ~ {temp_change(obj)[3]}\u00B0c
:bar_chart: Change over day: {temp_change(obj)[6]}\u00B0c
:sunglasses: UV Index: {obj.uvi}
:cloud_rain: Chance of Rain: {obj.chance_of_rain:.1%}
{"Bring:" if bring != "" else ""} {bring}
""")
  return text

def long_chat(obj):
  """Return long description of weather object"""
  uv_recommendation(obj)
  rain_check(obj)
  check_description(obj)
  bring = ", ".join(str(x) for x in clothes_true())
  text = (f"""
Forcast for {obj.name} in {obj.city}, {obj.state}, {obj.country}.
It's going to be a top of {obj.temp_max}\u00B0c with a low of {obj.temp_min}\u00B0c.
There's going to be {obj.description}.
{"-" * 50}
{obj.name.title()} will feel like:
Morning - {obj.feels_like_morn}\u00B0c
Day - {obj.feels_like_day}\u00B0c
Evening - {obj.feels_like_eve}\u00B0c
Night - {obj.feels_like_night}\u00B0c
{temp_change(obj)[4]}.
{temp_change(obj)[5]}.
{temp_change(obj)[7]}.
The difference between the min and max will be {temp_change(obj)[6]}\u00B0c
{"-" * 50}
{"You might want to bring your" if bring != "" else ""} {bring}
{uv_recommendation(obj)}
{rain_check(obj)}
""")
  return text