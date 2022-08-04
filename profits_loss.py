from pathlib import Path
import re, csv
from api import convertUSDtoSGD

def profits_and_loss_summary_report():
    """
    - Computes the difference in the net profit between each day, from the data found in the "Profits and Loss.csv"
    - Highlights the day where net profit is lower than the previous day, and the value difference, in the scenario that net profit is not higher each day
    """
    
    try:
        profits_loss = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
        # Create a file path to the "Profit and Loss.csv" file in the "csv_reports" folder

        day_profit_list = []
        # Create an empty list to append    

        with profits_loss.open(mode = "r", encoding = "UTF-8") as file:
        # Opens the "Profits and Loss.csv" file in read mode
            reader = csv.reader(file)
            # Reads the file
            next(reader)
            # Skips the header
            for line in reader:
                day_profit_list.append([int(line[0]),int(line[4])])
                # Appends the day and net profit values, found in the "Profit and Loss.csv" into the empty list (in a nested list format)

            last_index = len(day_profit_list)-1

            profits_loss_main = []
            # Create an empty list to append
            for i in range (last_index):
                if day_profit_list[i][1] > day_profit_list[i+1][1]:
                # If the net profit values is not consecutively higher each day,
                    profits_loss_main.append([day_profit_list[i+1][0], (round(convertUSDtoSGD(day_profit_list[i][1]-day_profit_list[i+1][1]),2))])
                    # the days at which net profit is lesser than the previous day, and its corresponding value in SGD, is appended to another empty list

            return profits_loss_main
        
    except Exception as e:
        print(f"An error has occurred. \nReason : {e}")