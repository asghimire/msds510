from src.msds510.util import get_top_ten_avengers

top_avengers = get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv')

for index in range(len(top_avengers)):
    for key in top_avengers[index]:
        print(key,':', top_avengers[index][key])
    print('-----------------------'
          '-----------------------')