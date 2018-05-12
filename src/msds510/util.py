"""This module contains all the utility functions needed"""
import csv
import re
import datetime
from time import strptime


def get_top_ten_avengers(inputfile):
 """This function take input file as args
    returns
    top ten avengers record"""
 with open(inputfile, 'r') as csv_file:
    cr = csv.DictReader(csv_file)
    list_r = []
    for row in cr:
        data = (dict(row))
        data['appearances'] = int(data['appearances'])
        list_r.append(data)
    s = sorted(list_r, key=lambda d: d['appearances'], reverse=True)
    top_ten_avengers = s[:10]
    new_top_ten_record = []
    for i in top_ten_avengers:
        desired_fields = ['url', 'name_alias', 'appearances', 'year', 'years_since_joining', 'notes']
        temp = dict((k, i[k]) for k in desired_fields if k in i)
        new_top_ten_record.append(temp)
    return (new_top_ten_record)


def get_date_joined(year, month):
 """This function takes year and month as args:
    returns date joined """
    formatted_month = re.sub("[^a-zA-Z]+", "", month)
    formatted_month = (strptime(formatted_month, '%b').tm_mon)
    return(datetime.date(year,formatted_month,1))


def days_since_joined(year, month):
   """This function takes year and month as args:
    returns days since joined """
    date_joined_input = get_date_joined(year=year, month=month)
    Todays_date = datetime.date.today()
    number_of_days_since_joined = (Todays_date-date_joined_input)
    return (number_of_days_since_joined)


top_avengers = get_top_ten_avengers(r'C:\msds510-midterm\data\processed\avengers_processed.csv')


def print_report(filepath):
 """This function takes filepath args:
    prints top ten avengers """
 # if __name__ == "__main__":
    top_avengers = get_top_ten_avengers(filepath)
    for i in range(0, len(top_avengers)):
     print('#', (i + 1), '.', top_avengers[i]['name_alias'])
     print()
     print('*', 'Number of Appearances', ':', top_avengers[i]['appearances'])
     print('*', 'Year Joined', ':', top_avengers[i]['year'])
     print('*', 'Years Since Joining', ':', top_avengers[i]['years_since_joining'])
     print('*', 'URL', ':', top_avengers[i]['url'])
     print()
     print('## Notes')
     print()
     print(top_avengers[i]['notes'])
     print()

if __name__ == "__main__":
    print_report(r'C:\msds510-midterm\data\processed\avengers_processed.csv')
