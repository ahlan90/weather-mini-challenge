from datetime import date, timedelta
import calendar

from weather.models import DayHumidity


def format_array_days(days):

    days_str = ""

    if len(days) >= 3:
        for day in days[:-2]:
            days_str = days_str + day + ", "

        days_str = days_str + days[-2] + " and " + days[-1] + "."

        return days_str

    if len(days) == 2:
        return days[-2] + " and " + days[-1] + "."

    if len(days) == 1:
        return days[0] + "."

    return days_str


def process_days_needs_umbrela(start_date, sum_days):

    prefix = f'You should take an umbrella in these days: '

    end_date = date.today() + timedelta(days=sum_days)

    days_humidity_interval = DayHumidity.objects.filter(date__gte=start_date, date__lt=end_date)

    days_string = []

    for day_humidity in days_humidity_interval:
        if day_humidity.humidity >= 70:
            days_string.append(calendar.day_name[day_humidity.date.weekday()])

    sufix = format_array_days(days_string)

    return prefix + sufix
