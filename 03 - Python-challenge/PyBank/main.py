# Import os module...This will allow us to create file paths across operating systems
import os

# Import csv module...Module for reading CSV files
import csv

file_path = os.path.join('Homework', '03 - Python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Check to see that we can open the csv file
with open(file_path) as file_object:

    csvreader = csv.reader(file_object, delimiter=',')

    print(csvreader)


# Calculate total number of months included in the dataset

# Calculate net total amount of "Profit/Losses" over the entire period

# Calculate the average of the changes in "Profit/Losses" over the entire period

# Calculate the greatest increase in profits (data and amount) over the entire period

# Calculate the greatest decrease in losses (data and amount) over the entire period