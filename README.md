
# WeatherData

**WeatherData** is a Python project for retrieving and analyzing historical weather data for a specific geographic location on a specific date across multiple years. It utilizes the [Open-Meteo Archive API](https://open-meteo.com/) to gather data such as temperature, wind speed, and precipitation for the last 5 years.

## Features

- Fetches and averages historic weather data for:
  - Temperature (min, mean, max)
  - Wind speed (min, mean, max)
  - Precipitation (sum, min, max)
- Works with any valid latitude/longitude pair
- Easily extendable for other metrics or time ranges

## Installation

Ensure you have the required Python packages:

```bash
pip install requests numpy sqlite3 tabulate
```

## Usage
### Fetch Weather Data
```python
from weather_data import WeatherData

# Define the location and date
latitude = 40.7590
longitude = 111.8876
day = 11
month = 12
year = 2024

# Create an instance
weather = WeatherData(latitude=latitude, longitude=longitude, day=day, month=month, year=year)

# Fetch and calculate weather data
weather.fetch_weather_data()

# Print the summary
print(weather)

# Fetch individual data points
mean_temp = weather.fetch_mean_temp()
max_wind = weather.fetch_max_wind_speed()
precip_total = weather.fetch_precipitation_sum()
```
### Store Weather Data in SQLite
```python
from weather_data import WeatherData
from weather_db import WeatherDB

# Fetch weather data (same as the previous example)
latitude = 40.7590
longitude = 111.8876
day = 11
month = 12
year = 2024
weather = WeatherData(latitude=latitude, longitude=longitude, day=day, month=month, year=year)
weather.fetch_weather_data()

# Initialize the database
db = WeatherDB()  # By default it will create a database in memory, to save values you can specify a path: WeatherDB('weather.db')
db.create_table()

# Insert the fetched weather data into the database
db.insert_weather(weather)

# Fetch and print all records from the weather table in fancy grid format
db.fetch_weather_data()

```
## Output

Example console output after calling `print(weather)`:

```
Weather Data for (40.759, 111.8876) on 11/12 over 5 years:
Temperature - Avg: 18.24°F, Min: 6.1°F, Max: 34.3°F
Wind Speed - Avg: 5.72 mph, Min: 0.5 mph, Max: 15.0 mph
Precipitation - Sum: 0.016 in, Min: 0.0 in, Max: 0.008 in
```

## Class Reference

### `WeatherData(latitude, longitude, day, month, years)`

- `latitude` (float): Latitude of the location
- `longitude` (float): Longitude of the location
- `day` (int): Day of interest
- `month` (int): Month of interest
- `years` (int): Year of interest

### Methods

- `fetch_weather_data()`: Fetches data for all metrics and stores aggregated values.
- `fetch_mean_temp()`: Returns the average temperature for the given date across 5 years.
- `fetch_max_wind_speed()`: Returns the maximum wind speed for the given date across 5 years.
- `fetch_precipitation_sum()`: Returns the total precipitation for the given date across 5 years.

## Notes

- This module uses the Open-Meteo Archive API which is free and does not require authentication.
- Make sure your date (month/day) is valid for all years to avoid errors from leap days or missing data.

## License

This project is open-source and available under the MIT License.
