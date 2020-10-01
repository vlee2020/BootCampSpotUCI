
import os                                                                       # Import os module...This will allow us to create file paths across operating systems
import csv                                                                      # Import csv module...Module for reading CSV files


cwd = os.getcwd()                                                               # Path to collect data from the Resources folder
election_data_filepath = os.path.join(cwd, "Resources", "election_data.csv")    # Path to election data


with open(election_data_filepath) as csv_file:                                  
    csv_reader = csv.reader(csv_file, delimiter=",")
    election_data = [word for word in [row for row in csv_reader]]


#Start Poll Analysis
print('')
print('Election Results')
print("---------------------------------------------------")

# Calculate Total Votes Cast
vote_count = len(election_data)-1                                           # Vote count.  Reducing 1 which is the header row
print(f'Total Votes: {vote_count}')
print("---------------------------------------------------")

# Identify unique candidates
unique_candidates_list = []
x = 1

for row in election_data[1:]:
    candidate = row[2]
   
    if candidate not in unique_candidates_list:    
        unique_candidates_list.append(candidate)  

#Calculate the total number of votes each candidate won

votes_list = []
votes_4_Khan = 0
votes_4_Correy = 0
votes_4_Li = 0
votes_4_Otooley = 0

for row in election_data[1:]:
    candidate = row[2]
    if candidate == "Khan": 
        votes_4_Khan = votes_4_Khan + 1
    if candidate == "Correy":
        votes_4_Correy = votes_4_Correy + 1
    if candidate == "Li":
        votes_4_Li = votes_4_Li + 1
    if candidate == "O'Tooley":
        votes_4_Otooley = votes_4_Otooley + 1

votes_list.append(votes_4_Khan)
votes_list.append(votes_4_Correy)
votes_list.append(votes_4_Li)
votes_list.append(votes_4_Otooley)

# Calculate the % of votes each candidate won
percent_list = []
pct_votes_Khan = votes_4_Khan / vote_count * 100
pct_votes_Correy = votes_4_Correy / vote_count * 100
pct_votes_Li = votes_4_Li / vote_count * 100
pct_votes_Otooley = votes_4_Otooley / vote_count * 100

percent_list.append(pct_votes_Khan)
percent_list.append(pct_votes_Correy)
percent_list.append(pct_votes_Li)
percent_list.append(pct_votes_Otooley)

# Calculate the winner of the election based on popular vote
winner_index = percent_list.index(max(percent_list))
winner = unique_candidates_list[winner_index]


# Print complete list of candidates who received votes
print(f'Khan: {"%.3f"%pct_votes_Khan}% ({votes_4_Khan})')
print(f'Correy: {"%.3f"%pct_votes_Correy}% ({votes_4_Correy})')
print(f'Li: {"%.3f"%pct_votes_Li}% ({votes_4_Li})')
print(f"O'Tooley: {'%.3f'%pct_votes_Otooley}% ({votes_4_Otooley})")
print("---------------------------------------------------")
print(f'Winner: {winner}')
print("---------------------------------------------------")

# Zip the lists together
#result = zip(unique_candidates_list, votes_list, percent_list)

# Export text file with the results

output_path = os.path.join(cwd, "Resources", "results.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------------------------------\n")
    txtfile.write(f'Khan: {"%.3f"%pct_votes_Khan}% ({votes_4_Khan})\n')
    txtfile.write(f'Correy: {"%.3f"%pct_votes_Correy}% ({votes_4_Correy})\n')
    txtfile.write(f'Li: {"%.3f"%pct_votes_Li}% ({votes_4_Li})\n')
    txtfile.write(f"O'Tooley: {'%.3f'%pct_votes_Otooley}% ({votes_4_Otooley})\n")
    txtfile.write("---------------------------------------------------\n")
    txtfile.write(f'Winner: {winner}\n') 
    txtfile.write("---------------------------------------------------\n")