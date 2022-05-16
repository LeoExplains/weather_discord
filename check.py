## Helper functions for checking temperature
from api import *

# recommend Clothes
clothes = { 
  'umbrella': False,
  'hat': False,
  'jumper': False,
  'windbreaker': False,
  'sunscreen': False,
  'mask': False,
  'stay inside': False
}

def clothes_true():
  result = list({k: v for k, v in clothes.items() if v == True})
  return result
  
# Check min & max temp
def temp_change(obj):
  """Check if temperature will get hotter or colder during the day"""
  # printing out the values 
  temp = {
          "morning": obj.temp_morn, 
          "afternoon": obj.temp_day, 
          "evening": obj.temp_eve, 
          "night": obj.temp_night
         }
  cold = min(temp, key=temp.get)
  cold_temp = temp[cold]
  hot = max(temp, key=temp.get)
  hot_temp = temp[hot]
  change = f"{obj.temp_max - obj.temp_min:.2f}"
  cold_text=(f'The coldest part of the day will be in the {cold.title()} with a temp of {temp[cold]}\u00B0c')
  hot_text=(f'The warmest part of the day will be in the {hot.title()} with a temp of {temp[hot]}\u00B0c')
  change_text = ""
  if (obj.temp_day - obj.temp_morn) > 3:
    change_text = (f"Afternoon will be warmer than Morning by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_eve - obj.temp_day) > 3:
    change_text = (f"Evening will be warmer than Afternoon by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_day - obj.temp_morn) < -2:
    change_text = (f"Afternoon will be colder than Morning by {obj.temp_day - obj.temp_morn:.2f}\u00B0c.")
    clothes['jumper'] = True
  elif (obj.temp_day - obj.temp_morn) < -2:
    change_text = (f"Evening will be colder than Afternoon {obj.temp_day - obj.temp_morn:.2f}\u00B0c.")
    clothes['jumper'] = True
  else: 
    change_text = (f"It's going to stay mostly the same temperature during the day")
  return (cold, cold_temp, hot, hot_temp, cold_text, hot_text,change, change_text)

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
    sunprotect = (f"It's going to be a UV Index of: {obj.uvi:.1f}")
    clothes['hat'] = True
    clothes['sunscreen'] = True
  elif obj.uvi >= 8:
    sunprotect = (f"It's going to be a UV Index of: {obj.uvi:.1}")
    clothes['hat'] = True
    clothes['sunscreen'] = True
    clothes['stay inside'] = True
  return (sunprotect)
  
# Check humidity
# need to check more about dew point vs humidity for accuracy. 

# check wind gust & speed
# need more information about wind gust and speed to feeling
  
# check rainfall
def rain_check(obj):
  """Check if an umbrella is needed"""
  rain_protect = ""
  if (obj.chance_of_rain * 100) > 60:
    rain_protect = (f"It's {obj.chance_of_rain:.1%} likely to rain {obj.name}")
    clothes['umbrella'] = True
  return (rain_protect)

#check description
def check_description(obj):
  "Check weather description to set inside"
  # Snow
  if obj.id > 601 and obj.id < 700:
    clothes['stay inside'] = True
  # Rain
  if obj.id > 502 and obj.id < 600:
    clothes['stay inside'] = True
    clothes['umbrella'] = True
  # Thunderstorm
  if obj.id > 200 and obj.id < 300:
    clothes['stay inside'] = True 


