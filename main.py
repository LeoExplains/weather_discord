# Help

# Command
#Hello I can forcast up to {date} for you
# Display Results

from api import *
location = get_lat_lon("hughesdale")
city = (location[0], location[1], location[2])
weather = get_current_weather(location[3], location[4])
set_days_weather(weather, city)

print(today.msg())
print(tomorrow.msg())
# print(get_pollution(location[0], location[1]))