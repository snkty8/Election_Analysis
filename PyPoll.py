# The data we need to retrieve 
#import csv
#import os

# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    #print(election_data)


# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Write into the analysis text file
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")
    # Write three counties to the file.
    # Words are printed with no spaces
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

    # Write three counties to the file.
    #txt_file.write("Arapahoe, Denver, Jefferson")

    # Write three counties to the file. This way puts them on new lines.
    #txt_file.write("Counties in the Election\n\nArapahoe\nDenver\nJefferson")


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)






# 1. The total number of votes casted
# 2. A complete lists of canidates who recieved votes
# 3. The percentage of votes of each canidate won
# 4. The total number of votes of each canidate won
# 5. The winner of the election based on popular vote 

