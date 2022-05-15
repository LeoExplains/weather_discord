from datetime import datetime, timedelta
from api import *
from check import *
dt = datetime.now()
td = timedelta(days=7)
# your calculated date
my_date = dt + td
# Help

# Command
print(f"Hello I can forcast up to {my_date} for you")
# Display Results

location = get_lat_lon("cremorne")
try:
   city = (location[0], location[1], location[2])
   weather = get_current_weather(location[3], location[4])
   set_days_weather(weather, city)
except Exception:
   print("location not provided")

print(temp_change(today))
print(uv_recommendation(today))
print(rain_check(today))
# print(get_pollution(location[0], location[1]))