import urllib.request, json

from weather.models import Coordinate, DayHumidity
from datetime import datetime


def get_weather_city(lat, long, key):

    print('Starting import data...')

    with urllib.request.urlopen(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}5&lon={long}&exclude=hourly,minutely&appid={key}') as url:

        data = json.loads(url.read().decode())

        coordinate, created = Coordinate.objects.get_or_create(latitude=lat, longitude=long)

        for day in data["daily"]:

            received_date = datetime.fromtimestamp(day["dt"])

            check_days_exists = DayHumidity.objects.filter(
                coordinate=coordinate,
                date=received_date
            )

            if check_days_exists:
                day_humidity = check_days_exists[0]
                day_humidity.humidity = day["humidity"]
            else:
                day_humidity = DayHumidity.objects.create(
                    coordinate=coordinate,
                    date=received_date,
                    humidity=day["humidity"]
                )

            print(f'This day imported -> {day_humidity}')

    print('End of import data...')
