# Import os module...This will allow us to create file paths across operating systems
import os

# Import csv module...Module for reading CSV files
import csv

# Path to collect data from the Resources folder
cwd = os.getcwd()
budget_data_filepath = os.path.join(cwd, "Resources", "budget_data.csv")

#Start Financial Analysis
print('')
print('Financial Analysis')
print("---------------------------------------------------")


with open(budget_data_filepath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    budget_data = [word for word in [row for row in csv_reader]]
                                  
    # Convert profit/loss column to integers
    for row in budget_data[1:]:         #loop through each row in budget_data starting with row 2 (index 1) since row 1 (index 0) is the header row 
        pl_range = row[1]               #profit/losses range is found in column 2 (index 1)
        pl_range = int(pl_range)        #convert each range number from a string to an integer so that i can perform calculatons on them later
        row[1] = pl_range               #assign range, which is now an integer, bact to indext 1 in each row
                                        #note: print(budget_data) to view updated budget_data set

     # Calculate total number of month records included in the dataset
    for row in budget_data:
        number_of_months = len(budget_data)-1
    
    print(f'Total Months: {number_of_months}')

    # Calculate net total amount of "Profit/Losses" over the entire period
    
    pl_net_total = 0
    for row in budget_data[1:]:
        pl_range = row[1]
        pl_net_total += pl_range
  
    print(f'Total: ${pl_net_total}')

    prior_month_pl = [867884]                                    #create a list to store prior month profit/loss
    change_list = []                                             #create a list to store monthly change results
    x = 1
    total_change = 0

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    for row in budget_data[1:]:
        pl_current_month = row[1]
        pl_prior_month = prior_month_pl[(x-1)]
        
        change = pl_current_month - pl_prior_month
        total_change += change
        
        prior_month_pl.append(pl_current_month)                 #append value to prior_month_pl list      
        change_list.append(change)                              #append value to change_list to be referenced for greatest increase and greatest decrease questions following
        x = x + 1 

    average_change = total_change / (number_of_months-1)

    print(f'Average Change: ${"%.2f"%average_change}')    

    # Calculate the greatest increase in profits (data and amount) over the entire period
    greatest_increase = max(change_list)
    r_index = change_list.index(greatest_increase)
    corresponding_month = budget_data[(r_index+1)][0]
    
    print(f'Greatest Increase in Profits: {corresponding_month} $({greatest_increase})')

    # Calculate the greatest decrease in losses (data and amount) over the entire period
    greatest_decrease = min(change_list)
    r_index = change_list.index(greatest_decrease)
    corresponding_month = budget_data[(r_index+1)][0]

    print(f'Greatest Decrease in Profits: {corresponding_month} $({greatest_decrease})')
    
    # Export results to a text file
   
    output_path = os.path.join(cwd, "Resources", "results.txt")

    with open(output_path, 'w') as txtfile:
        txtfile.write('\n')
        txtfile.write('Financial Analysis\n')
        txtfile.write("---------------------------------------------------\n")
        txtfile.write(f'Total Months: {number_of_months}\n')
        txtfile.write(f'Total: ${pl_net_total}\n')
        txtfile.write(f'Average Change: ${"%.2f"%average_change}\n') 
        txtfile.write(f'Greatest Increase in Profits: {corresponding_month} $({greatest_increase})\n') 
        txtfile.write(f'Greatest Decrease in Profits: {corresponding_month} $({greatest_decrease})\n')  
        txtfile.write(f'Greatest Increase in Profits: {corresponding_month} $({greatest_decrease})\n')

  

      
