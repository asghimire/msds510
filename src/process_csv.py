import csv


def get_processed_csv(inputfile, outputfile):
    with open(inputfile, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        header = reader.fieldnames
        list_r = []
        for row in reader:
            data = (dict(row))
            list_r.append(data)
        #print(list_r)
    # print(header)
        fieldnames = []
        for each_field in header:
            formatted_header = each_field.lower().replace('/', '_').replace(' ', '_').strip('?').strip('\n')
            fieldnames.append(formatted_header)
            #print(fieldnames)

        with open(outputfile, 'w',encoding='utf-8', newline="") as csv_file_w:
            writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
            writer.writeheader()
            #for row1 in list_r:
            writer.writerows(list_r)


if __name__ == "__main__":
    get_processed_csv(r'C:\Users\archa\Documents\bellevue_University\msds510\data\raw\avengers.csv',
                  r'C:\Users\archa\Documents\bellevue_University\msds510\data\processed\avengers_processed.csv')

