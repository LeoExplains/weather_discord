## Helper functions for checking temperature
from api import *

# recommend Clothes
clothes = { 
  'Umbrella': False,
  'Hat': False,
  'Jumper': False,
  'Windbreaker': False,
  'Suncreen': False,
  'Mask': False,
  'Inside': False
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
  cold_text=(f'The coldest part of the day will be in the {cold} with a temp of {temp[cold]}\u00B0c')
  hot_text=(f'The warmest part of the day will be in the {hot} with a temp of {temp[hot]}\u00B0c')
  change_text = ""
  if (obj.temp_day - obj.temp_morn) > 3:
    change_text = (f"Morning > Afternoon will get warmer by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_eve - obj.temp_day) > 3:
    change_text = (f"Afternoon > Evening will get warmer by {obj.temp_day - obj.temp_morn:.2f}\u00B0c")
  elif (obj.temp_day - obj.temp_morn) < -2:
    change_text = (f"Morning > Afternoon will get colder by {obj.temp_day - obj.temp_morn:.2f}\u00B0c. You should bring a jumper")
    clothes['jumper']
  elif (obj.temp_day - obj.temp_morn) < -2:
    change_text = (f"Afternoon > Evening will get colder by {obj.temp_day - obj.temp_morn:.2f}\u00B0c. You should bring a jumper")
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
    sunprotect = (f"You should wear suncreen or a hat today. It's going to be a UV Index of: {obj.uvi:.1f}")
    clothes['hat'] = True
    clothes['suncreen'] = True
  elif obj.uvi >= 8:
    sunprotect = (f"You should stay inside today. If you have to go out bring sunscreen. It's going to be a UV Index of: {obj.uvi:.1}")
    clothes['hat'] = True
    clothes['suncreen'] = True
    clothes['inside'] = True
  return (sunprotect)
  
# Check humidity
# need to check more about dew point vs humidity for accuracy. 

# check wind gust & speed
# need more information about wind gust and speed to feeling
  
# check rainfall
def rain_check(obj):
  """Check if an umbrella is needed"""
  rain_protect = ""
  if (obj.chance_of_rain * 100) > 40:
    rain_protect = (f"You should bring an umbrella today. It's {obj.chance_of_rain:.1%} likely to rain today")
    clothes['umbrella'] = True
  return (rain_protect)

#check description
def check_description(obj):
  "Check weather description to set inside"
  # Snow
  if obj.id > 601 and obj.id < 700:
    clothes['inside'] = True
  # Rain
  if obj.id > 502 and obj.id < 600:
    clothes['inside'] = True
    clothes['umbrella'] = True
  # Thunderstorm
  if obj.id > 200 and obj.id < 300:
    clothes['inside'] = True 


