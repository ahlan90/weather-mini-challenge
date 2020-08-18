from django.core.management import BaseCommand

from weather.data_import import get_weather_city


class Command(BaseCommand):

    help = 'Import data of Weather of Open Weather to database'
    open_weather_key = ''

    def handle(self, *args, **kwargs):
        get_weather_city('-23.704985', '-46.404064', '913f387c969f35bfbf6885090d166e5a')

