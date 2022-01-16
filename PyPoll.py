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

# Declare winning candidate string value
winning_candidate = ""

# Declare winning count tracker and percentage tracker
winning_count = 0
winning_percentage = 0


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

    # save the results to our text file
    with open (file_saved, "w") as txt_file:
        
        #print final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")

        #save the final vote count to the text file
        txt_file.write(election_results)

# determine percentage of votes for each candidate
for candidate_name in candidate_votes:

    # retrieve vote count of candidate
    votes = candidate_votes[candidate_name]

    # calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # print each candidate, their vote count and percentage of votes to terminal
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)

    # save the candidate results to txt_file
    txt_file.write(candidate_results)

    #Determine if vote count calculated is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count to votes and winning_percentage to vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and winning candidate to candidate name
            winning_candidate = candidate_name 

# # print out winning candidate summary
# winning_candidate_summary = (
#     f"-----------------------\n"
#     f"Winner: {winning_candidate}\n"
#     f"Winning Vote Count: {winning_count:,}\n"
#     f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
#     f"------------------------\n")

# print(total_votes)
# print(candidate_options)
# print(candidate_votes)
# print(winning_candidate_summary)


