import os
import csv

total_months = 0
net_total = 0
previous_profit = 0
changes = []
months = []
greatest_increase = ("", 0)
greatest_decrease = ("", 0)


file_path = "C:/Users/vallo/Desktop/Homework/Python_Challenge/PyBank/Resources/budget_data.csv"

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        date = row[0]
        profit_loss = int(row[1])
        net_total += profit_loss
        
        if total_months > 1:
            change = profit_loss - previous_profit
            changes.append(change)
            months.append(date)

            if change > greatest_increase[1]:
                greatest_increase = (date,change)
            
            if change < greatest_decrease[1]:
                greatest_decrease = (date,change)

        previous_profit = profit_loss

average_change = sum(changes) / len(changes) 

results = []
results.append("analysis")
results.append("----------------------")
results.append(f"Total Months: {total_months}")
results.append(f"Total: ${net_total}")
results.append(f"Average Change: ${average_change:,.2f}")
results.append(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})")
results.append(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})")




for line in results:
    print(line)


git_file = 'analysis/.gitkeep'
with open(git_file, 'w') as textfile:
    for line in results:
        textfile.write(line + '\n')

    






