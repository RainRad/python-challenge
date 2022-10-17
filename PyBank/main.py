#imports
import os
import csv

#starting data sets
total_months = 0
net_profit_loss = 0

greatest_profit_date = ""
greatest_profit_amount = 0

greatest_loss_date = ""
greatest_loss_amount = 0

changes = 0
start = 0
prior_month = 0


#import data csv file
budget_csv = os.path.join('Resources','budget_data.csv')
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        #total month count
        total_months += 1

        #total profit track
        net_profit_loss += int(row[1])

        #average check
        if start > 0:
            difference = int(row[1]) - prior_month
            changes += difference

            #greatest increase check
            if difference > greatest_profit_amount:
                greatest_profit_date = row[0]
                greatest_profit_amount = difference
            
            #greatest loss check
            if difference < greatest_loss_amount:
                greatest_loss_date = row[0]
                greatest_loss_amount = difference

        start += 1
        prior_month = int(row[1])

#average calc
average = round(changes / (total_months-1),2)
  
#output to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Net Profit/Loss: ${net_profit_loss}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_profit_date} : ${greatest_profit_amount}")
print(f"Greatest Decrease in Profits: {greatest_loss_date} : ${greatest_loss_amount}")



#output to txt file
outputfile = os.path.join('analysis','budget_analysis.txt')

with open(outputfile,"w") as text:
    text.write(f"Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total Net Profit/Loss: ${net_profit_loss}\n")
    text.write(f"Average Change: ${average}\n")
    text.write(f"Greatest Increase in Profits: {greatest_profit_date} : ${greatest_profit_amount}\n")
    text.write(f"Greatest Decrease in Profits: {greatest_loss_date} : ${greatest_loss_amount}\n")
    text.close()
