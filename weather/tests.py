from django.test import TestCase

from weather.utils import format_array_days


class FormatStringDays(TestCase):

    def test_empty(self):
        days = format_array_days([])
        self.assertEqual(days, '')

    def test_one_day(self):
        days = format_array_days(['Thursday'])
        self.assertEqual(days, 'Thursday.')
