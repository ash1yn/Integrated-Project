from pathlib import Path
import re, csv
from api import convertUSDtoSGD

def cash_on_hand_summary_report():
    """
    - Returns the 
    """
    try:
        cash_on_hand = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
        # Create a file path to the "Cash on Hand.csv" file in the "csv_reports" folder

        day_cash_list = []
        # Create an empty list to append    

        with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        # Open the "Cash on Hand.csv" file in read mode
            reader = csv.reader(file)
            # Reads the "Cash on Hand.csv" file
            next (reader)
            # Skips the header
            for line in reader:
                day_cash_list.append([int(line[0]), int(line[1])])
                # Appends the day and cash on hand values, found in the "Cash on Hand.csv" into the empty list (in a nested list format)

            last_index = len(day_cash_list)-1

            cash_on_hand_main = []
            # Create an empty list to append

            for i in range (last_index):
                    if day_cash_list[i][1] > day_cash_list[i+1][1]:
                    # If the cash on hand values is not consecutively higher each day,
                        cash_on_hand_main.append([day_cash_list[i+1][0], round(convertUSDtoSGD(day_cash_list[i][1]-day_cash_list[i+1][1]),2)])
                        # the day at which cash on hand is lesser than the previous day, and its corresponding cash on hand value in SGD, will be appended to another empty list

            return cash_on_hand_main

    except Exception as e:
        print(f"An error has occured. \nReason: {e}")
            