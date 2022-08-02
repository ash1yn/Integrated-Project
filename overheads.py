from pathlib import Path
import re, csv
from api import convertUSDtoSGD

overheads = Path.cwd()/"csv_reports"/"Overheads.csv"
# Create a file_path to the "Overheads.csv" file in the "csv_reports" folder
print(overheads.exists())

overheads_list = []
# Create an empty list to append
highest = 0
def overheads_summary_report():
    with overheads.open(mode = "r", encoding = "UTF-8") as file:
    # Opens "Overheads.csv" file in read mode
        reader = csv.reader(file)
        # Reads the file
        next(reader)
        # Skips the headers
        for line in reader:
            # print(line)
            overheads_list.append([line[0],float(line[1])])
            # Appends the expense(name) and overheads into the empty list

        last_index = len(overheads_list)

        for i in range(last_index):
            if overheads_list[i][1] > highest:
                highest = overheads_list[i][1]
                print(f"{overheads_list[i][0]} : SGD {convertUSDtoSGD(highest)}")
        # Finds the highest overhead category and its corresponding value in SGD
