"""The "generate_report function generates the report of top ten avengers and writes to top_ten_appearances.md file"""
import subprocess
from src.msds510.avenger import Avenger


def generate_report():
        with open(r'C:\msds510-midterm\reports\avengers_record_report.md', 'w') \
            as write_to_report:
            subprocess.call(['python', r'C:\msds510-midterm\src\msds510\avenger.py' ],
                        stdout=write_to_report)


if __name__ == '__main__':
 generate_report()