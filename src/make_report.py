import subprocess
with open(r'C:\msds510\reports\top_ten_appearances.md', 'w') as write_to_report:
    subprocess.call(['python', r'C:\msds510\src\msds510\util.py'], stdout=write_to_report )


