from django.core.management import BaseCommand

from weather.data_import import get_weather_city


class Command(BaseCommand):
    help = 'Import data of Weather of Open Weather to database'

    def handle(self, *args, **kwargs):
        get_weather_city('-23.704985', '-46.404064')
