"""The "generate_report function generates the report of top ten avengers and writes to top_ten_appearances.md file"""
import subprocess
with open(r'C:\msds510-midterm\reports\top_ten_appearances.md', 'w') as write_to_report:
    subprocess.call(['python', r'C:\msds510-midterm\src\msds510\util.py'], stdout=write_to_report )


