# Import os module...This will allow us to create file paths across operating systems
import os

# Import csv module...Module for reading CSV files
import csv

# Path to collect data from the Resources folder
cwd = os.getcwd()
budget_data_filepath = os.path.join(cwd, "Resources", "budget_data.csv")

with open(budget_data_filepath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
                                #reader = csv.DictReader(budget_data)
                                #for row in reader:
                                #print(row)

                                # Read the header row first 
                                #header = next(csv_reader)
                                #print(header)
                                #print(budget_data)
    #budget_data = [word for word in [row for row in csv_reader]]
                                #print(data)
                                #print(data[0])
                                #print(data[0][1])
                                #print(data[1][1])
                                #total = int(budget_data[0][1]) + int(budget_data[1][1])
                                #print(total)    

    # Convert profit/loss column to integers
    for row in budget_data[1:]:         #loop through each row in budget_data starting with row 2 (index 1) since row 1 (index 0) is the header row 
        pl_range = row[1]               #profit/losses range is found in column 2 (index 1)
        pl_range = int(pl_range)        #convert each range number from a string to an integer so that i can perform calculatons on them later
        row[1] = pl_range               #assign range, which is now an integer, bact to indext 1 in each row
                                        #print(budget_data) to view updated budget_data set

     # Calculate total number of month records included in the dataset
    for row in budget_data:
        number_of_months = len(budget_data)
    
    print(f'Total Months: {number_of_months}')

    # Calculate net total amount of "Profit/Losses" over the entire period
    pl_net_total = 0
    for row in budget_data[1:]:
        pl_range = row[1]
        pl_net_total += pl_range

    print(f'Total: ${pl_net_total}')

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    
    while len(budget_data) <= number_of_months:
        budget_data.append
        #change_total = 0
        #for row in budget_data[1:]:
            #p1_range = row[1]

            #pl_net_total += pl_range

            #print(f'Total: ${pl_net_total}')


                                    #average = pl_net_total / number_of_months
                                    #print(f'Average Change: ${average}')

    # Calculate the greatest increase in profits (data and amount) over the entire period
    

    print(f'Greatest Increase in Profits: TBD')

    # Calculate the greatest decrease in losses (data and amount) over the entire period

    print(f'Greatest Decrease in Profits: TBD')
