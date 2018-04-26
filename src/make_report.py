from src.msds510.util import get_top_ten_avengers

top_avengers = get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv')

for i in range(0,len(top_avengers)):
    print((i+1), '.', top_avengers[i]['Name/Alias'])
    print('                      '
          '                       ')
    for key in top_avengers[i]:
        top_avengers[i]['Name/Alias']=top_avengers[i].pop('Name/Alias')
        print('*', key,':', top_avengers[i][key])
    print('-----------------------'
          '-----------------------')
