from django.db import models


class Coordinate(models.Model):

    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return f'lat: {self.latitude} - lng: {self.longitude}'


class DayHumidity(models.Model):

    coordinate = models.ForeignKey(Coordinate, on_delete=models.CASCADE)

    date = models.DateField()
    humidity = models.IntegerField()

    def __str__(self):
        return f'Date: {self.date} - Humidity: {self.humidity}'
