import unittest
from src.msds510.utils.conversion import*
from ddt import ddt, data, unpack

@ddt
class TestConversion(unittest.TestCase):

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


suite = unittest.TestLoader().loadTestsFromTestCase(TestConversion)
unittest.TextTestRunner(verbosity=2).run(suite)