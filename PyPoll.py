# Add in dependencies
import csv
import os

# Assign a vairable to load a file from a path
load_file = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_saved = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare a new list (empty dictionary) to get candidates recieving votes
candidate_options = []

# Declare a new list (empty dictionary) for candidate vote totals
candidate_votes = {}

# Open the election results
with open(load_file) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the csv file
    for row in file_reader:
        total_votes += 1

        # print candidate name from each row
        candidate_name = row [2]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add candidate name to the candidate list
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count and set to zero
            candidate_votes[candidate_name] = 0
        
        # begin adding to candidates vote count
        candidate_votes[candidate_name] += 1

# determine percentage of votes for each candidate
for candidate_name in candidate_votes:

    # retrieve vote count of candidate
    votes = candidate_votes[candidate_name]

    # calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100

# print(total_votes)
# print(candidate_options)
# print(candidate_votes)
print(f"{candidate_name}: recieved {vote_percentage}% of the vote.")


