import sqlite3
from weather_data import WeatherData
from tabulate import tabulate

#This Class Fulfills requirements for C4
class WeatherDB:
    def __init__(self, db_path=':memory:'):
        """
        Initialize the WeatherDatabase with a SQLite connection.
        Use ':memory:' for in-memory DB or provide a filepath.
        """
        self.db_path = db_path  # Set the db_path here
        self.conn = sqlite3.connect(self.db_path)  # Use self.db_path to connect
        self.cursor = self.conn.cursor()

    def create_table(self):
        '''
        Creates the weather data table if it doesn't exist in the weather database.
        '''
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS weather (
                pk INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                latitude REAL,
                longitude REAL,
                month INTEGER,
                day INTEGER,
                YEAR INTEGER,
                five_year_avg_temp REAL,
                five_year_min_temp REAL,
                five_year_max_temp REAL,
                five_year_avg_wind_speed REAL,
                five_year_min_wind_speed REAL,
                five_year_max_wind_speed REAL,
                five_year_sum_precipitation REAL,
                five_year_min_precipitation REAL,
                five_year_max_precipitation REAL)
            """)
        self.conn.commit()

    def insert_weather(self, weather_data):
        """
        Inserts weather data into the weather data table.
        """
        self.cursor.execute("""
            insert into weather (
                latitude, longitude, 
                month, day, year, 
                five_year_avg_temp, five_year_min_temp, five_year_max_temp, 
                five_year_avg_wind_speed, five_year_min_wind_speed, five_year_max_wind_speed, 
                five_year_sum_precipitation, five_year_min_precipitation, five_year_max_precipitation
            ) 
            values (:latitude, :longitude, 
                    :month, :day, :year, 
                    :five_year_avg_temp , :five_year_min_temp, :five_year_max_temp, 
                    :five_year_avg_wind_speed, :five_year_min_wind_speed, :five_year_max_wind_speed, 
                    :five_year_sum_precipitation, :five_year_min_precipitation, :five_year_max_precipitation)
        """, {'latitude': weather_data.latitude,
              'longitude': weather_data.longitude,
              'month': weather_data.month,
              'day': weather_data.day,
              'year': weather_data.year,
              'five_year_avg_temp': weather_data.avg_temp,
              'five_year_min_temp': weather_data.min_temp,
              'five_year_max_temp': weather_data.max_temp,
              'five_year_avg_wind_speed': weather_data.avg_wind_speed,
              'five_year_min_wind_speed': weather_data.min_wind_speed,
              'five_year_max_wind_speed': weather_data.max_wind_speed,
              'five_year_sum_precipitation': weather_data.sum_precip,
              'five_year_min_precipitation': weather_data.min_precip,
              'five_year_max_precipitation': weather_data.max_precip
              })
        self.conn.commit()

    #This Method fulfills requirements for C6
    def fetch_weather_data(self):
        """
        Fetches and prints all records from the weather table in a fancy grid.
        """
        self.cursor.execute("SELECT * FROM weather")
        all_weather = self.cursor.fetchall()

        headers = [description[0] for description in self.cursor.description]
        print(tabulate(all_weather, headers=headers, tablefmt="fancy_grid"))

if __name__ == '__main__':
    #Fetch Weather Data for Washington Square Park in Salt Lake City, Utah
    slc = {"latitude": 40.7590, "longitude": 111.8876, "day": 11, "month": 12, "year": 2024}
    slc_weather = WeatherData(latitude=slc["latitude"], longitude=slc["longitude"], day=slc["day"], month=slc["month"],
                              year=slc["year"])
    slc_weather.fetch_weather_data()

    #Initialize database in memory and populate it with fetched weather values
    db = WeatherDB()
    db.create_table()
    db.insert_weather(slc_weather)

    # Fetch and print all records from the weather table
    db.fetch_weather_data()
