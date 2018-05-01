"""The util module has all the helper fucntions to work with dates and bool and stuff"""
import csv


def get_top_ten_avengers(inputfile):
 """The "get_top_ten_avengers" function returns the record for top ten avengers by appearances"""
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


 top_avengers = get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv')


def print_report(filepath):
    """The "print_report" function prints the top ten avengers with the desired fields that we provided."""
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
    print_report(r'C:\msds510\data\processed\avengers_processed.csv')
