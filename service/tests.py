from django.test import TestCase

from service.db import check_time_difference


class MiscTestCase(TestCase):

    def test_check_time_difference(self):
        opening_time = '10:00'
        closing_time = '12:00'
        self.assertEquals(
            check_time_difference(opening_time, closing_time), True
        )
        with self.assertRaises(ValueError):
            check_time_difference(closing_time, opening_time)
