#Get data/csv file
#Remove any potential duplicates
#List of each candidate who received votes
#Tally total number of votes
#Tally number of votes per candidate received
#Calculate % vote for each candidate to determine winner

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
#Create a filename variable to a direct or indirect file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Defining variables for candidates
candidate_options = []
candidate_votes = {}
#Defining variables for winners
winning_candidate = ""
winning_count = 0
winning_percent = 0

# # Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read and print the header row
    headers = next(file_reader)
    # #Confirm Header removal
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
              
        # Print the candidate name from each row
        candidate_name = row[2]

        # Add only unique candidates
        if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)
             #Tracking votes/candidate
             candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the winner and votes
    print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")
    
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    #Determine Winning Candidate and vote total
    if (votes > winning_count) and (vote_percentage > winning_percent):
        winning_count = votes
        winning_percent = vote_percentage
        winning_candidate = candidate_name
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)





# #3. Print the total votes 
# print(total_votes)

# # To do: perform analysis.
# print(election_data)


# Close the file
# outfile.close()
# election_data.close()


#################################
# Earlier class example         #
#################################
# #Using the open() funtion with the 'w' mode we will write data to the file
# open(file_to_save,"w")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Arapahoe, \nDenver, \nJefferson")



# # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)