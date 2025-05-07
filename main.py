#This File Completes Requirements for C3, C5, C6

from weather_data import WeatherData
from weather_db import WeatherDB

if __name__ == "__main__":
    # Details for Washington Square Park in Salt Lake City, Utah
    slc = {"latitude": 40.7590, "longitude": 111.8876, "day": 11, "month": 12, "year": 2024}
    slc_weather = WeatherData(latitude=slc["latitude"], longitude=slc["longitude"], day=slc["day"], month=slc["month"],
                              year=slc["year"])

    slc_weather.fetch_weather_data()
    print(slc_weather)

    mean_temp = slc_weather.fetch_mean_temp()
    print(f"mean temp: {mean_temp}")

    max_wind_speed = slc_weather.fetch_max_wind_speed()
    print(f"max wind speed: {max_wind_speed}")

    precipitation_sum = slc_weather.fetch_precipitation_sum()
    print(f"precipitation sum: {precipitation_sum}")

    #This portion fulfills requirements for C5
    #Initialize weather database in memory, then add SLC values into it
    db = WeatherDB()
    db.create_table()
    db.insert_weather(slc_weather)

    #This portion fulfills requirements for C6
    # Fetch and print all records from the weather table
    db.fetch_weather_data()