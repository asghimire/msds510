from src.msds510.util import get_top_ten_avengers

top_avengers = get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv')

for index in range(0,len(top_avengers)):
    print((index+1), '.', top_avengers[index]['Name/Alias'])
    print('                      '
          '                       ')
    for key in top_avengers[index]:
        top_avengers[index]['Name/Alias']=top_avengers[index].pop('Name/Alias')
        print('*', key,':', top_avengers[index][key])
    print('-----------------------'
          '-----------------------')
