# Analysis of Election Audit

## Overview of Project
An analysis of election audit data for 3 different counties.

### Purpose
The purpose of this project was to analyze the total election-audit data for 3 different counties, determine the winner, which county had the highest voter turnout, and write a set of repeatable code that would place these results into a text file for easy reference.

## Results

- A total of 369,711 votes were cast for the election. 38,855 (10.5%) in Jefferson county, 306,055 (82.8%) in Denver county and 24,801 (6.7%) in Arapahoe county
- Of the three candidates: Charles Gaspar Stockholm received 85,213 (23%) votes, Dianne DeGette received 272,892 (73.8%) votes and Raymon Anthony Doane recived 11,606 (3.1%) votes
- Diana DeGette won the election with ~74% of the vote, and Denver County had the highest turnout with ~83% (306,055) votes coming from there.

I obtained these results with the following code. The steps used are noted within the hashes:

# Add our dependencies.
import csv
from itertools import count
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_vote = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
Highest_turnout = ""
county_turnout = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
     
            # 4c: Begin tracking the county's vote count.
            county_vote[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_vote[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_vote:
        # 6b: Retrieve the county vote count.
        cvotes = county_vote.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        cvote_percent = float(cvotes) / float(total_votes) *100
        county_results = (f"{county_name}: {cvote_percent:.1f}% ({cvotes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cvotes > county_turnout):
            county_turnout = cvotes
            Highest_turnout = county_name

    # 7: Print the county with the largest turnout to the terminal.
    Winning_county_summary = (
         f"-------------------------\n"
        f"County with the Highest Turnout is {Highest_turnout} with {county_turnout} voters\n"
        f"-------------------------\n")
    print(Winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(Winning_county_summary)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)



### Election-Audit Summary
With some modifications, this script can be utilized in most elections. For example, to analyze a larger election with more counties involved, all one would need to do is either update the existing 'election_results.csv' file with the new data or link a new .csv file to the 'file_to_load' and 'file_to_save' variables (shown in my code above under the third and fourth hash) and the code will be able to print the results to a text file with minimal effort. This could apply at the national level as well, where the referenced .csv file would need to be updated as mentioned prior, and then the variables at the county-level would just need to be updated to reflect the desired states. If county variables and results are still desired, the code usd for the candidates and the counties can be used as a framework to write a new state-level analysis.
