import csv


def get_top_ten_avengers(inputfile):
 with open(inputfile, 'r') as csv_file:
    cr = csv.DictReader(csv_file)
    list_r = []
    for row in cr:
        data = (dict(row))
        data['Appearances'] = int(data['Appearances'])
        data['Year']= int(data['Year'])
        data['Years since joining']=int(2018-data['Year'])
        list_r.append(data)
    s = sorted(list_r, key=lambda d: d['Appearances'], reverse=True)
    top_ten_avengers = s[:10]
    new_top_ten_record = []
    for i in top_ten_avengers:
        wanted_keys = ['URL', 'Name/Alias', 'Appearances', 'Year', 'Years since joining', 'notes']  # The keys you want
        temp = dict((k, i[k]) for k in wanted_keys if k in i)
        new_top_ten_record.append(temp)
    return (new_top_ten_record)

#print(get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv'))