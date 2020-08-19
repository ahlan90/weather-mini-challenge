from django.test import TestCase

from weather.utils import format_array_days


class FormatStringDays(TestCase):

    def test_empty(self):
        days = format_array_days([])
        self.assertEqual(days, '')

    def test_one_day(self):
        days = format_array_days(['Thursday'])
        self.assertEqual(days, 'Thursday.')

    def test_two_days(self):
        days = format_array_days(['Monday', 'Thursday'])
        self.assertEqual(days, 'Monday and Thursday.')

    def test_more_then_two_days(self):
        days = format_array_days(['Monday', 'Thursday', 'Saturday'])
        self.assertEqual(days, 'Monday, Thursday and Saturday.')
