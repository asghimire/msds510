import csv
from time import strptime
import re


def get_processed_csv(inputfile, outputfile):
    with open(inputfile, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        header = reader.fieldnames
        # print(header)
        list_r = []
        for row in reader:
            data = (dict(row))
            list_r.append(data)


    fieldnames = []
    for each_field in header:
        formatted_header = each_field.lower().replace('/', '_').replace(' ', '_').strip('?').strip('\n')
        fieldnames.append(formatted_header)
    fieldnames.append('month_joined')


    for item in list_r:
        item['url'] = item.pop('URL')
        item['name_alias'] = item.pop('Name/Alias')
        item['appearances'] = item.pop('Appearances')
        item['current'] = item.pop('Current?')
        item['gender'] = item.pop('Gender')
        item['probationary_introl'] = item.pop('Probationary Introl')
        item['full_reserve_avengers_intro'] = item.pop('Full/Reserve Avengers Intro')
        item['year'] = item.pop('Year')
        item['years_since_joining'] = item.pop('Years since joining')
        item['honorary'] = item.pop('Honorary')
        item['death1'] = item.pop('Death1')
        item['return1'] = item.pop('Return1')
        item['death2'] = item.pop('Death2')
        item['return2'] = item.pop('Return2')
        item['death3'] = item.pop('Death3')
        item['return3'] = item.pop('Return3')
        item['death4'] = item.pop('Death4')
        item['return4'] = item.pop('Return4')
        item['death5'] = item.pop('Death5')
        item['return5'] = item.pop('Return5')
        item['notes'] = item.pop('Notes')
        # print(item)
        # print(header)
        #print(list_r)
    for item in list_r:
        item['appearances']= int( item['appearances'])
        item['current']=item['current']=='YES'
        item['year'] = int(item['year'])
        item['years_since_joining'] = int(2018-item['year'])
        item['death1'] =  item['death1']=='YES'
        item['return1'] =  item['return1']=='YES'
        item['death2'] =   item['death2']=='YES'
        item['return2'] =  item['return2']=='YES'
        item['death3'] =  item['death3']=='YES'
        item['return3'] =  item['return3']=='YES'
        item['death4'] =  item['death4']=='YES'
        item['return4'] =  item['return4']=='YES'
        item['death5'] =  item['death5']=='YES'
        item['return5'] =  item['return5']=='YES'
        # month = re.sub("[^a-zA-Z]+", "",item['month_joined'] )
        # item['month_joined'] = (strptime(month,'%b').tm_mon)
        # print(item)
    for item in list_r:
         item['month_joined']= item['full_reserve_avengers_intro']
    #     item['month_joined'] = re.sub("[^a-zA-Z]+", "", item['month_joined'])
    #     item['month_joined'] = (strptime(item['month_joined'], '%b').tm_mon)
    #     list_r.append(item['month_joined'])
         for key in item:
            if key == 'month_joined':
                new_value = re.sub("[^a-zA-Z]+", "", item[key])
                new_value = (strptime(new_value, '%b').tm_mon)
                item['month_joined'] = new_value
                item.update(new_value)

    print(list_r)
    print(item)

    with open(outputfile, 'w', encoding='utf-8', newline="") as csv_file_w:
         writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
         writer.writeheader()
         for each_row in list_r:
            writer.writerow(each_row)


if __name__ == "__main__":
    get_processed_csv(r'C:\msds510\data\raw\avengers.csv',
                  r'C:\msds510\data\processed\avengers_processed1.csv')


