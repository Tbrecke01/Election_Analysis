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

# # Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read and print the header row
    headers = next(file_reader)
    # #Confirm Header removal
    # print(headers)

    # # To do: perform analysis.
    # print(election_data)


# Close the file
# outfile.close()
election_data.close()


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