import unittest
import datetime
from time import strptime
from src.msds510.utils.date import*


class TestDate(unittest.TestCase):
    def test_get_date_joined(self):
        actual_output_1 = get_date_joined(1963, 'may')
        actual_output_2 = get_date_joined(1999, 'aug')
        expected_output_1 = datetime.date(1963, 5, 1)
        expected_output_2 = datetime.date(1999, 6, 1)
        self.assertEqual(actual_output_1, expected_output_1)
        self.assertNotEqual(actual_output_2, expected_output_2)

    def test_get_date_joined_invalid_input(self):
        actual_output = get_date_joined('2003', 5)
        expected_output = None
        self.assertEqual(actual_output, expected_output)

    def test_get_date_joined_missing_input(self):
        actual_output = get_date_joined(' ', 'jun')
        expected_output = None
        self.assertEqual(actual_output, expected_output)

    def test_days_since_joined(self):
        actual_output = days_since_joined(1985, 'jun')
        expected_output = str(datetime.date.today()-get_date_joined(1985, 'jun'))
        self.assertEqual(actual_output, expected_output)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDate)
unittest.TextTestRunner(verbosity=2).run(suite)