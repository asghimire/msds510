### msds510
Project Description: This data science project takes a csv file as input. The file used is avenger.csv. The project then converts the
file into utf-8 file and cleans it in order to generate python friendly fieldnames. The processed csv file is saved in data/processed/avengers_processed.csv.

The project implements different functions that does date manipulations and conversions. Finally it generates the desired reports in report folder

All the utility functions are located in utils package (src/msds510/utils).

To process the raw csv file, run src/process_csv.py script.
* Avenger.py module implements Avenger class that has methods for all fields in input csv
* Unit tests for all functions and methods in avenger class is located in src/tests directory

To EXECUTE all unit tests, run src/run_tests.py

To generate a markdown report
* run src/make_report.py script.

