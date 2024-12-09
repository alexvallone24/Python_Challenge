# Import and set file path
import os
import csv

file_path = "C:/Users/vallo/Desktop/Homework/Python_Challenge/PyPoll/Resources/election_data.csv"

# Read csv
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

   # Set variables for counting votes
    candidate_votes = {}
    total_votes = 0
    
   # Count votes for each row in csv
    for row in csvreader:
        candidate =  row[2]
        total_votes += 1

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
        

# Create results list
results = []
results.append("Election Results")
results.append("--------------")
results.append(f"Total Votes: {total_votes}")
results.append("---------------")

# Set variables for winner
winner = ""
candidate_percentage = {}
winning_count = 0

# Calculate winner and each candidate's percentage
for candidate, votes in candidate_votes.items():
    percentage = ((votes / total_votes) * 100)
    candidate_percentage[candidate] = percentage
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Add to results list
results.append("-------------")
results.append(f"Winner: {winner}")
results.append("--------------")

# Print and set a file location for results
for line in results:
    print(line)

git_file = 'analysis/.gitkeep'
with open(git_file, 'w') as textfile:
    for line in results:
        textfile.write(line + '\n')  




    
