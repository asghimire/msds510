import csv


def get_top_ten_avengers(inputfile):
    file = open(inputfile, 'r')
    rows = file.readlines()
    for line in rows:
     print(type(line))

    # list_r = []
    # for row in cr:
    #     data = (dict(row))
    #     data['appearances'] = int(data['appearances'])
    #     list_r.append(data)
    # s = sorted(list_r, key=lambda d: d['appearances'], reverse=True)
    # top_ten_avengers = s[:10]
    # new_top_ten_record = []
    # for i in top_ten_avengers:
    #     desired_fields = ['url', 'name_alias', 'appearances', 'year', 'years_since_joining', 'notes']
    #     temp = dict((k, i[k]) for k in desired_fields if k in i)
    #     new_top_ten_record.append(temp)
    # return (new_top_ten_record)
if __name__ == "__main__":
    print(get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv'))