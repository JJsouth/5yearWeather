#This file fulfills requirements for Portion D

from weather_data import WeatherData
from weather_db import WeatherDB

if __name__ == '__main__':
    # Details for Washington Square Park in Salt Lake City, Utah
    washington_square = {"latitude": 40.7590, "longitude": -111.8876, "day": 11, "month": 12, "year": 2024}
    washington_square_weather = WeatherData(latitude=washington_square["latitude"], longitude=washington_square["longitude"],
                                            day=washington_square["day"], month=washington_square["month"], year=washington_square["year"])
    washington_square_weather.fetch_weather_data()
    print('Washington Square')
    print(washington_square_weather)

    mean_temp = washington_square_weather.fetch_mean_temp()
    print(f"mean temp: {mean_temp}°F")
    max_wind_speed = washington_square_weather.fetch_max_wind_speed()
    print(f"max wind speed: {max_wind_speed} mph")
    precipitation_sum = washington_square_weather.fetch_precipitation_sum()
    print(f"precipitation sum: {precipitation_sum} inches")

    # Details for the Space Needle in Seattle, Washington
    print('Space Needle')
    space_needle = {"latitude": 47.6205, "longitude": -122.3493, "day": 11, "month": 12, "year": 2024}
    space_needle_weather = WeatherData(latitude=space_needle["latitude"], longitude=space_needle["longitude"],
                                       day=space_needle["day"], month=space_needle["month"], year=space_needle["year"])
    space_needle_weather.fetch_weather_data()
    print(space_needle_weather)

    mean_temp = space_needle_weather.fetch_mean_temp()
    print(f"mean temp: {mean_temp}°F")
    max_wind_speed = space_needle_weather.fetch_max_wind_speed()
    print(f"max wind speed: {max_wind_speed} mph")
    precipitation_sum = space_needle_weather.fetch_precipitation_sum()
    print(f"precipitation sum: {precipitation_sum} inches")

    # Details for Hobbiton New Zealand
    print('Hobbiton')
    hobbiton = {"latitude": -37.8721, "longitude": 175.6829, "day": 11, "month": 12, "year": 2024}
    hobbiton_weather = WeatherData(latitude=hobbiton["latitude"], longitude=hobbiton["longitude"],
                                       day=hobbiton["day"], month=hobbiton["month"], year=hobbiton["year"])
    hobbiton_weather.fetch_weather_data()
    print(hobbiton_weather)

    mean_temp = hobbiton_weather.fetch_mean_temp()
    print(f"mean temp: {mean_temp}°F")
    max_wind_speed = hobbiton_weather.fetch_max_wind_speed()
    print(f"max wind speed: {max_wind_speed} mph")
    precipitation_sum = hobbiton_weather.fetch_precipitation_sum()
    print(f"precipitation sum: {precipitation_sum} inches")

    # Initialize weather database in memory, then add values into it
    db = WeatherDB()
    db.create_table()
    db.insert_weather(washington_square_weather)
    db.insert_weather(space_needle_weather)
    db.insert_weather(hobbiton_weather)

    # Fetch and print all records from the weather table
    db.fetch_weather_data()
