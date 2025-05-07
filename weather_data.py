import requests
import numpy as np

# This class completes requirements C1: Create a class with the following instance variables for your chosen location and date
class WeatherData:
    """
    A class to store and retrieve historic weather data from a specific location
    from the last five years since specified date.
    """
    # This is the base url to connect to the open-meteo archived weather endpoint
    base_url = "https://archive-api.open-meteo.com/v1/archive"

    # Initialize class instance variables with specified location and date
    def __init__(self,*, latitude, longitude, day, month, year):
        self.latitude = latitude
        self.longitude = longitude
        self.year = year
        self.month = month
        self.day = day

        # Initialize with None
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None

        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None

    def fetch_weather_data(self):
        """Fetches and stores weather data for the selected location and date."""
        # Initialize lists to store weather values over the last 5 years for calculation after all 5 years are gathered
        min_temps = []
        mean_temps = []
        max_temps = []

        min_wind_speeds = []
        mean_wind_speeds = []
        max_wind_speeds = []

        precipitations = []

        # Fetch data from open-meteo on the specified date. Then iterate over the last 5 years of that date
        # Note this pulls values in imperial units and in the Denver timezone
        for i in range(5):
            year = self.year - i
            event_date = f'{year}-{self.month:02d}-{self.day:02d}'
            daily = (
                'temperature_2m_min,temperature_2m_mean,temperature_2m_max,'
                'wind_speed_10m_min,wind_speed_10m_mean,wind_speed_10m_max,'
                'precipitation_sum'
            )

            url = (
                f"{self.base_url}?latitude={self.latitude}&longitude={self.longitude}"
                f"&start_date={event_date}&end_date={event_date}"
                f"&daily={daily}"
                f"&timezone=America%2FDenver"
                f"&temperature_unit=fahrenheit"
                f"&wind_speed_unit=mph"
                f"&precipitation_unit=inch"
            )

            response = requests.get(url)
            # Check for errors: if received, note the year and error code.
            if response.status_code != 200:
                print(f"Error fetching data for {event_date}: {response.status_code}")
                continue
            data = response.json()

            #add received values for the year into list for processing
            min_temps.append(data["daily"]["temperature_2m_min"][0])
            mean_temps.append(data["daily"]["temperature_2m_mean"][0])
            max_temps.append(data["daily"]["temperature_2m_max"][0])

            min_wind_speeds.append(data["daily"]["wind_speed_10m_min"][0])
            mean_wind_speeds.append(data["daily"]["wind_speed_10m_mean"][0])
            max_wind_speeds.append(data["daily"]["wind_speed_10m_max"][0])

            precipitations.append(data["daily"]["precipitation_sum"][0])

        # Now process and store the values into instance variables
        self.min_temp = round(float(np.min(min_temps)), 2)
        self.avg_temp = round(float(np.mean(mean_temps)), 2)
        self.max_temp = round(float(np.max(max_temps)), 2)

        self.min_wind_speed = round(float(np.min(min_wind_speeds)), 2)
        self.avg_wind_speed = round(float(np.mean(mean_wind_speeds)), 2)
        self.max_wind_speed = round(float(np.max(max_wind_speeds)), 2)

        self.sum_precip = float(np.sum(precipitations))
        self.min_precip = float(np.min(precipitations))
        self.max_precip = float(np.max(precipitations))

    def __str__(self):
        return (f"Weather Data for ({self.latitude}, {self.longitude}) on {self.day}/{self.month} over 5 years:\n"
                f"Temperature - Avg: {self.avg_temp}°F, Min: {self.min_temp}°F, Max: {self.max_temp}°F\n"
                f"Wind Speed - Avg: {self.avg_wind_speed} mph, Min: {self.min_wind_speed} mph, Max: {self.max_wind_speed} mph\n"
                f"Precipitation - Sum: {self.sum_precip} in, Min: {self.min_precip} in, Max: {self.max_precip} in")

    # Complete Requirements for C2: Write a method for each of the following daily weather variables using the "Weather API" web link to pull data for your chosen location and date for the most recent five years
    def fetch_mean_temp(self):
        """Fetches the mean temperature for the selected location and date from the last 5 years."""
        mean_temps = []
        for i in range(5):
            year = self.year - i
            event_date = f'{year}-{self.month:02d}-{self.day:02d}'
            mean_temp_url = (f"https://archive-api.open-meteo.com/v1/archive?"
                                  f"latitude={self.latitude}&longitude={self.longitude}"
                                  f"&start_date={event_date}&end_date={event_date}"
                                  f"&daily=temperature_2m_mean"
                                  f"&timezone=America%2FDenver"
                                  f"&temperature_unit=fahrenheit")
            response = requests.get(mean_temp_url)

            # Check for errors: if received, note the year and error code.
            if response.status_code != 200:
                print(f"Error cannot fetch data for {year}: {response.status_code}")
            else:
                data = response.json()
                # add value for the year into list for processing
                mean_temps.append(data["daily"]["temperature_2m_mean"][0])
        # Return processed values for the past 5 years
        return round(float(np.average(mean_temps)), 2)

    def fetch_max_wind_speed(self):
        """
        Fetches the maximum wind speed in miles per hour for the selected location and date
        over the most recent five years using the open-meteo Weather API.
        :return: max_wind_speed
        """
        wind_speeds = []
        for i in range(5):
            year = self.year - i
            event_date = f'{year}-{self.month:02d}-{self.day:02d}'
            max_wind_speed_url = (f"https://archive-api.open-meteo.com/v1/archive?"
                                  f"latitude={self.latitude}&longitude={self.longitude}"
                                  f"&start_date={event_date}&end_date={event_date}"
                                  f"&daily=wind_speed_10m_max"
                                  f"&timezone=America%2FDenver"
                                  f"&wind_speed_unit=mph")
            response = requests.get(max_wind_speed_url)

            # Check for errors: if received, note the year and error code.
            if response.status_code != 200:
                print(f"Error cannot fetch data for {year}: {response.status_code}")
            else:
                data = response.json()
                # add value for the year into list for processing
                wind_speeds.append(data["daily"]["wind_speed_10m_max"][0])
        # Return processed values for the past 5 years
        return round(float(np.max(wind_speeds)), 2)

    def fetch_precipitation_sum(self):
        """
        Fetches the total precipitation in inches for the selected location and date
        over the most recent five years using the open-meteo Weather API.
        :return: sum_precipitation
        """
        precipitation_sums = []
        for i in range(5):
            year = self.year - i
            event_date = f'{year}-{self.month:02d}-{self.day:02d}'
            precipitation_sum_url = (f"https://archive-api.open-meteo.com/v1/archive?"
                                  f"latitude={self.latitude}&longitude={self.longitude}"
                                  f"&start_date={event_date}&end_date={event_date}"
                                  f"&daily=precipitation_sum"
                                  f"&timezone=America%2FDenver"
                                  f"&precipitation_unit=inch")
            response = requests.get(precipitation_sum_url)

            # Check for errors: if received, note the year and error code.
            if response.status_code != 200:
                print(f"Error cannot fetch data for {year}: {response.status_code}")
            else:
                data = response.json()
                #add value for the year into list for processing
                precipitation_sums.append(data["daily"]["precipitation_sum"][0])
        # Return processed values for the past 5 years
        return float(np.sum(precipitation_sums))

