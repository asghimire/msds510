import csv
from time import strptime
import re
# record['is_current'] = record['is_current']=='YES'
# record['Year']= int(record['Year'])
# record['Years since joining']= int(record['Years since joining'])
# record['Years since joining'] = 2018 - record['Year']
from time import strptime

with open(r'C:\msds510\data\processed\avengers_processed1.csv', 'r') as dr:
    dr = csv.DictReader(dr)
    for row in dr:
        print(row)
        # new_D['first_name'], new_D['last_name'] = row['name_alias'].split(' ')
    row['month_joined'] = row['full_reserve_avengers_intro']
    each_month = row['month_joined']
    each_month = re.sub("[^a-zA-Z]+", "", each_month)
    each_month = (strptime(each_month, '%b').tm_mon)

print(dict(row))

record = [dict(year='1988', intro='Jun-88'),
          dict(year='1989', intro='may-89'),
          dict(year='2005', intro='5-may'),
          dict(year='2013', intro='13-Nov'),
          dict(year='2014', intro='14-Jan'),
          ]


# print(record)
def get_month(intro_str):
    intro = []
    for each_record in record:
        intro_str = each_record['intro']
        intro_str = re.sub("[^a-zA-Z]+", "", intro_str)
        intro_str = (strptime(intro_str, '%b').tm_mon)
        intro.append(intro_str)
    return intro

# print(get_month(record))
