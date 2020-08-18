from django.db import models


class Coordinate(models.Model):

    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return f'lat: {self.latitude} - lng: {self.longitude}'
