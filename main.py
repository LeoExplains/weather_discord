from datetime import datetime, timedelta
dt = datetime.now()
td = timedelta(days=7)
# your calculated date
my_date = dt + td
# Help

# Command
print(f"Hello I can forcast up to {my_date} for you")
# Display Results

from api import *
location = get_lat_lon("hughesdale")
try:
   city = (location[0], location[1], location[2])
   weather = get_current_weather(location[3], location[4])
   set_days_weather(weather, city)
  
   print(today.msg())
   print(tomorrow.msg())
except Exception:
   print("location not provided")

# print(get_pollution(location[0], location[1]))