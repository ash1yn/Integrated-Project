from api import convertUSDtoSGD
from cash_on_hand import cash_on_hand_summary_report
from overheads import overheads_summary_report
from profits_loss import profits_and_loss_summary_report
from pathlib import Path

summary_report = Path.cwd()/"summary_report.txt"
print(summary_report.exists())

with summary_report.open(mode = "w", encoding = "UTF-8", newline = "") as file:
    file.write(f"{overheads_summary_report()}\n")
    file.write(f"{cash_on_hand_summary_report()}\n")
    file.write(f"{profits_and_loss_summary_report()}\n")

