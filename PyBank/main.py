import os
import csv

with open('Analysis/analysis.txt', 'a') as f:

    budget_csv = os.path.join(".", "Resources", "budget_data.csv") # "." since both folders areat the same "level"


    # Open and read csv
    with open(budget_csv) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)

    # Calculate the total number of months included in the dataset
    # Calculate the net total amount of "Profit/Losses" over the entire period
        month = 0
        Total_amount = 0

        for i in csv_reader:
            month = month + 1
            Total_amount = Total_amount + int(i[1])

        print(f"Total Months: {month}")
        f.write(f"Total Months: {month}")
       
        print(f"Total: ${Total_amount}")
        f.write(f"Total: ${Total_amount}")


    # Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes

    ## Open and read csv
    with open(budget_csv) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)

        previous_num = 0
        change = 0
        change_list = []
        month_list = []

        for i in csv_reader:
            current_num = int(i[1])
            change = current_num - previous_num
            change_list.append(change)
            previous_num = current_num
            month_list.append(i[0])

        change_list.pop(0)
        
        Total = 0

        for i in change_list:
            Total = Total + i

        Total = Total/len(change_list)
        print(f"Average Change: $ {Total}")    
        f.write(f"Average Change: $ {Total}")

    # Calculate the greatest increase in profits (date and amount) over the entire period
    max_val = max(change_list)
    find = change_list.index(max_val)
    date = month_list[find+1]  # "fins+1" because I had to remove the first row since it is not part of the time period

    print(f"Greatest Increase in Profits: {date} (${max_val})")
    f.write(f"Greatest Increase in Profits: {date} (${max_val})")

    # Calculate the greatest decrease in profits (date and amount) over the entire period    
    ## Greatest Decrease in Profits: Feb-14 ($-1825558)
    min_val = min(change_list)
    find2 = change_list.index(min_val)
    date2 = month_list[find2+1]  # "fins+1" because I had to remove the first row since it is not part of the time period                      
        
    print(f"Greatest Decrease in Profits: {date2} (${min_val})")
    f.write(f"Greatest Decrease in Profits: {date2} (${min_val})")
    











