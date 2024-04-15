import os
import csv

file = os.path.join("..","PyBank","budget_data.csv")
# Previewing report.
print("Financial Analysis")
print("----------------------------------------")
with open(file) as budget_data:
    # Things below this are in the right place. Stop touching them...
    budget = csv.reader(budget_data, delimiter = ",")
    budget_header = next(budget_data)
    length = 0
    total = 0
    greatest_profit = 0
    greatest_losses = 0
    for row in budget:
        # Total months
        length += 1
        # Total profits.
        total += int(row[1])
        # Average Change.
        average = round(total / length)
        # Greatest profits.
        if int(row[1]) >= greatest_profit:
            greatest_profit = int(row[1])
            profit_month = str(row[0])
        # Greatest losses.
        if int(row[1]) <= greatest_losses:
            greatest_losses = int(row[1])
            loss_month = str(row[0])
    print(f"Total Months: {length}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {profit_month} ${greatest_profit}")
    print(f"Greatest Decrease in Profits: {loss_month} ${greatest_losses}")
# Generating text report.
txt = os.path.join("..","PyBank","analysis.txt")
with open(txt,"w") as analysis_report:
    analysis_report.write(
        "Financial Analysis \n"
        "---------------------------------------- \n"
        f"Total Months: {length} \n"
        f"Total: ${total} \n"
        f"Average Change: ${average} \n"
        f"Greatest Increase in Profits: {profit_month} ${greatest_profit} \n"
        f"Greatest Decrease in Profits: {loss_month} ${greatest_losses} \n"
    )
    