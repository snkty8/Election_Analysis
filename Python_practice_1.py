#Module 3 Practice

# Creat a list
counties = ["Arapahoe","Denver","Jefferson"]
#print(counties) 

# Add items to list using .append function
counties.append("El Paso")
#print(counties)

# Add items to a specific place in list using .insert
counties.insert(2, "El Paso")
#print(counties)

# Remove items from list using .remove
counties.remove("El Paso")
#print(counties)

# Remove items from list using .pop (3 refers to 4th position)
counties.pop(3)
#print(counties)

# Create dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#print(counties_dict)

# Show the length of the countries dictionary
#print(len(counties_dict))

#Print all keys and values in the dictionary
#print(counties_dict.items())

#Print all keys in the dictionary
#print(counties_dict.keys())

# Print all values in the dictionary
#print(counties_dict.values())

# Get value from specific key
#print(counties_dict.get("Denver"))

# Lists of Dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)

# If. Elif, and Else Statement (Do not have the indent like the nested loops) 
#Fav_Number = int(input("Guess my favorite number :)"))

#if Fav_Number == 7:
#   print("You got it!")

#elif Fav_Number == 8:
#   print("So close, but too high")

#elif Fav_Number == 6:
#   print("Close, but too low")

#else:
#   print("Too bad, so sad!!")

# Nest If Else statements
#Grade = int(input("What is your grade?"))
#if Grade >= 90:
#    print("You get an A")
#else:   
#    if Grade >=80:
#        print("You get a B") 
#    else:
#        if Grade >= 70:
#            print("You get a C")
#        else:
#            if Grade >=60:
#                print("You get a D") 
#            else:
#                print("You Fail")  


# Skill Drill: Use str to print out valules associated with numbers
#for county, voters in counties_dict.items():
#    print(str(county) + " county has ", str(voters) + " registered voters")

# Use F Strings to do the same as above
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

# The use of multiple F Strings and precision factor
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)

# print the number of voters in each county.  The :, after votes adds the comma
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters:,} registered voters.")



#Read CSV File
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #    print(row)


