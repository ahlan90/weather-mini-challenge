from datetime import date, timedelta
import calendar

from weather.models import DayHumidity


def format_array_days(days):

    days_str = ""

    if days:
        if len(days) > 1:
            days_str = days_str
        else:
            days_str = days[0] + "."
    else:
        return ""

    return days_str


def process_days_needs_umbrela(start_date, sum_days):

    prefix = f'You should take an umbrella in these days:'

    end_date = date.today() + timedelta(days=sum_days)

    days_humidity_interval = DayHumidity.objects.filter(date__gte=start_date, date__lt=end_date)

    days_string = []

    for day_humidity in days_humidity_interval:
        days_string.append(calendar.day_name[day_humidity.date.weekday()])

    sufix = format_array_days(days_string)

    return prefix + sufix
