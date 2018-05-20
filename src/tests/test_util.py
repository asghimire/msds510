import unittest
from src.msds510.util import*
from ddt import ddt, data, unpack

@ddt
class TestUtil(unittest.TestCase):
    @data(('2.22', 2), ('.879', 0))
    @unpack
    def test_float_str(self, actual, expected):
        actual_output = to_int(actual)
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    @data(('archana', None), ('_)(*&^%+', None))
    @unpack
    def test_invalid_str(self, actual, expected):
        actual_output = to_int(actual)
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    @data(('2567', 2567), (7.89, 7), (1/2, 0))
    @unpack
    def test_int_input(self, actual, expected):
        actual_output = to_int(actual)
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    @data(({'a': 1, 'b': 52, 'd': 6}, 6))
    @unpack
    def test_valid_dict_input(self, actual, expected):
        actual_output = get_value(actual, 'd')
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    @data(({'a': 1, 'b': 52, 'd': 6}, None))
    @unpack
    def test_dict_missing_key(self, actual, expected):
        actual_output = get_value(actual, 'h')
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    @data((['a', 'c', 'd'], 1))
    @unpack
    def test_valid_list_input(self, actual, expected):
        actual_output = get_value(actual, 'c')
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    @data(([ 'a', 'c', 'd' ], None))
    @unpack
    def test_missing_list_input(self, actual, expected):
        actual_output = get_value(actual, 'h')
        expected_output = expected
        self.assertEqual(actual_output, expected_output)

    def test_get_date_joined(self):
        actual_output_1 = get_date_joined(1963, 'may')
        actual_output_2 = get_date_joined(1999, 'aug')
        expected_output_1 = datetime.date(1963,5,1)
        expected_output_2 = datetime.date(1999, 6,1)
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
