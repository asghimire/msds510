from src.msds510.util import get_top_ten_avengers

top_avengers = get_top_ten_avengers(r'C:\msds510\data\processed\avengers_processed.csv')

for i in range(0,len(top_avengers)):
    print((i+1), '.', top_avengers[i]['name_alias'])
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


