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
def chat_recommendation(obj):
  # take all the other checks and prints out one block of text

  #Forcast for today

  #Temperature changes

  #Recommendations
  temp_change(obj)
  print(uv_recommendation(obj))
  print(rain_check(obj))
  print(obj)
  return None