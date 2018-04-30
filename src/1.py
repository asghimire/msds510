import re
import datetime
import calendar
from time import strptime

d = {'probationary_introl': 'Jul-03'}
month = re.sub("[^a-zA-Z]+", "", d['probationary_introl'])
month = (strptime(month, '%b').tm_mon)
temp_year = int(re.sub("\D", "", d['probationary_introl']))
if 59 <= temp_year <= 99:
    year_s = '19' + str(temp_year)

if 00 <= temp_year < 10:
        year_s = 20 + (temp_year)
else:
 year_s = 20 + str(temp_year)

year = int(year_s)
#print(datetime.date(year, month, 1))
month_int= {v: k for k,v in enumerate(calendar.month_abbr)}
print(month_int['Jul'])