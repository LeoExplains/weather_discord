## Helper functions for checking temperature
from api import *
# Check min & max temp
def temp_change(obj):
  feels_temp = {
    "morning": obj.feels_like_morn, 
    "daytime": obj.feels_like_day, 
    "evening": obj.feels_like_eve, 
    "night": obj.feels_like_night
  }
  # printing out the values 
  cold=(f'The coldest part of the day will be in the {min(feels_temp.keys())} with a temp of {min(feels_temp.values())}\u00B0c')
  hot=(f'The warmest part of the day will be in the {max(feels_temp.keys())} with a temp of {max(feels_temp.values())}\u00B0c')
  change = ""
  if (obj.temp_day - obj.temp_morn) > 3:
    change = (f"Morning > Afternoon will get warmer by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_eve - obj.temp_day) > 3:
    change = (f"Afternoon > Evening will get warmer by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_day - obj.temp_morn) < -2:
    change = (f"Morning > Afternoon will get colder by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_day - obj.temp_morn) < -2:
    change = (f"Afternoon > Evening will get colder by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  else: 
    change = (f"It's going to stay mostly the same temperature during the day")
  return (cold, hot, change)

# check uv index
def uv_recommendation(obj):
  """Returns true for sun protection and or Stay inside"""
# UV Index scale
# low (1-2)
# moderate (3-5)
# high (6-7)
# very high (8-10)
# extreme (11 and above).
  sunprotect = ""
  if obj.uvi >= 3:
    sunprotect = (f"You should wear suncreen or a hat today. It's going to be a UV Index of: {obj.uvi:.1f}")
  elif obj.uvi >= 8:
    sunprotect = (f"You should stay inside today. If you have to go out bring sunscreen. It's going to be a UV Index of: {obj.uvi:.1}")
  return (sunprotect)
  
# Check humidity
# need to check more about dew point vs humidity for accuracy. 

# check wind gust & speed
# need more information about wind gust and speed to feeling
  
# check rainfall
def rain_check(obj):
  rain_protect = ""
  if (obj.chance_of_rain * 100) > 40:
    rain_protect = (f"You should bring an umbrella today. It's {obj.chance_of_rain:.02%} likely to rain today")
  return (rain_protect)

  clothes = ""
  sunscreen = ""
  rain = ""
  inside = ""

#check description


# check change in day

# recommend Clothes

# recommend stay inside / go outside

# Set recommendation