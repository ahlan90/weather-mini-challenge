from django.apps import AppConfig


class CustomersConfig(AppConfig):
    name = 'weather'

    def ready(self):
        import weather.signals # noqa
