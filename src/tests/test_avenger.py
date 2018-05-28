import unittest
from src.msds510.avenger import Avenger
from src.process_csv import*
from src.msds510.utils.conversion import *
from src.msds510.utils.date import *

output_file = get_processed_csv\
        (r'C:\msds510-midterm\data\raw\avengers.csv',
            r'C:\msds510-midterm\data\processed\avengers_processed.csv')
with open(output_file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    record_list = []
    for row in reader:
        data = (dict(row))
        record_list.append(data)

class TestAvenger(unittest.TestCase):
    for item_index in range(len(record_list)):
         pym_record = record_list[0]
    hank_pym = Avenger(pym_record)
    def test_url(self):
        actual_url = self.hank_pym.url()
        self.assertEqual(actual_url, 'http://marvel.wikia.com/Henry_Pym_(Earth-616)')

    def test_name_alias(self):
        actual_output = self.hank_pym.name_alias()
        expected_output = 'Henry Jonathan "Hank" Pym'
        self.assertEqual(actual_output, expected_output)

    def test_appearances(self):
        actual_output = self.hank_pym.appearances()
        expected_output = int(self.pym_record.get('appearances'))
        self.assertEqual(actual_output, expected_output)

    def test_is_current(self):
        actual_output =str(self.hank_pym.is_current())
        self.assertTrue(actual_output)

    def test_gender(self):
        actual_output = self.hank_pym.gender()
        expected_output = self.pym_record.get('gender')
        self.assertEqual(actual_output, expected_output)

    def test_year(self):
        actual_output = self.hank_pym.year()
        expected_output = to_int(self.pym_record.get('year'))
        self.assertEqual(actual_output, expected_output)

    def test_date_joined(self):
        actual_output = self.hank_pym.date_joined()
        expected_output = get_date_joined(self.pym_record.get('year'), self.pym_record.get('full_reserve_avengers_intro'))
        self.assertEqual(actual_output, expected_output)

    def test_days_since_joining(self):
        actual_output = str(self.hank_pym.days_since_joining())
        expected_output = days_since_joined(self.pym_record.get('year'), self.pym_record.get('full_reserve_avengers_intro'))
        self.assertEqual(actual_output,expected_output )

    def test_years_since_joining(self):
        actual_output = self.hank_pym.years_since_joining()
        expected_output = (datetime.date.today().year - to_int(self.pym_record.get('year')))
        self.assertEqual(actual_output, expected_output)

    def test_notes(self):
        actual_output = self.hank_pym.notes()
        expected_output = self.pym_record.get('notes')
        self.assertEqual(actual_output, expected_output)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAvenger)
unittest.TextTestRunner(verbosity=2).run(suite)
