# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
#open file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
#declare variables
month = 0
change = 0
month_name = ""
total_months = 0
total_period = 0
greatest_increase = 0
increase_month = ""
greatest_decrease = 0
decrease_month = ""
decrease = 0
increase = 0
avg_change = 0
#declare dictionaries
profit = {}
loss = {}
# Format Final Table
print("Financial Analysis")

print("-------------------")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    csv_header = next(csvfile)
    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        total_period = total_period + int(row[1])
    
        #profit_loss.append(change)
        
    print ("Total Months: " + str(total_months) + "")
    print(("Total: $" + str(total_period) + ""))
    print("Average Change: $" + str(avg_change) + "")
    print(f"Greatest Increase in Profits: {increase_month} ${greatest_increase}")
    print (f"Greated Decrease in Profits: {decrease_month} ${greatest_decrease}")

# Specify the file to write to
output_path = os.path.join("..", "PyBank", "Analysis", "analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Total Months: " + str(total_months) +""])
    csvwriter.writerow([f"Total: ${total_period}"])
    csvwriter.writerow([f"Average Change: ${avg_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {increase_month} ${greatest_increase}"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {decrease_month} ${greatest_decrease}"])

    csvwriter.writerow(["--------------------------------------"])
  
#-------------------------unsure if this code runs---------------------