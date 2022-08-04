from api import convertUSDtoSGD
from api import exchange_rate
from cash_on_hand import cash_on_hand_summary_report
from overheads import overheads_summary_report
from profits_loss import profits_and_loss_summary_report
from pathlib import Path

summary_report = Path.cwd()/"summary_report.txt"
# Create a file path to the "summary_report.txt" file 

cash_on_hand = cash_on_hand_summary_report()
profits_and_loss = profits_and_loss_summary_report()

with summary_report.open(mode = "w", encoding = "UTF-8", newline = "") as file:
    file.write(f"[REAL TIME CURRENCY CONVERSION] USD 1 = SGD {exchange_rate()}\n")
    # Writes the real time currency conversion from USD to SGD, into the "summary_report.txt" file

    file.write(f"{overheads_summary_report()}\n")
    # Writes the highest overheads category and value into the "summary_report.txt" file
    
    if len(cash_on_hand) == 0:
        file.write(f"[CASH SURPLUS] Cash on hand for each period is higher than the previous period\n") 
    for l in range (len(cash_on_hand)): 
        file.write(f"[CASH DEFICIT] DAY: {cash_on_hand[l][0]}, AMOUNT: SGD {cash_on_hand[l][1]}\n") 
    
    if len(profits_and_loss) == 0:
        file.write(f"[NET SURPLUS] Net Profit for each period is higher than the previous period\n")
    for i in range (len(profits_and_loss)):
        file.write(f"[NET DEFICIT] DAY: {profits_and_loss[i][0]}, AMOUNT: SGD {profits_and_loss[i][1]}\n")
    
#
    print(AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)
