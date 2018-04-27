import csv


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
        #print(fieldnames)

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

    with open(outputfile, 'w', encoding='utf-8', newline="") as csv_file_w:
         writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
         writer.writeheader()
         for each_row in list_r:
            writer.writerow(each_row)

get_processed_csv(r'C:\msds510\data\raw\avengers.csv',
                  r'C:\msds510\data\processed\avengers_processed1.csv')
