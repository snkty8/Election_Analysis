# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of canidates who received votes.
3. Calculate the total number of votes each canidate recieved.
4. Calculate the percentage of votes each canidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python and Visual Studio Code

## Summary
The analysis of the election show that:
- There were 369,711 votes in the election
- The canidates were:
Charles Casper Stockham
Diana DeGette
Raymon Anthony Doane
- The candidate results were:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
- The winner if the election was:
    - Candidate Diana DeGette, who received 73.8%, and 272,892 number of votes.

## Challenge Overview

An additional data is needed for the election audit.  The election commission has requested a complete audit for:
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count 
3. The county with the largest turnout


## Election Audit Results

 ![image](https://github.com/snkty8/Election_Analysis/blob/main/Resources/Terminal%20Election%20Results.png)]

 As seen in the image above:

 - There were 369,711 total votes casted in the congressional election

 - Total votes for each county include:
    Jefferson County: 38,855 (10.5%)
    Denver County: 306, 055 (82.8%)
    Arapahoe: 24,801 (6.7%)

- Denver County had the largest number of votes: 306,055

- Total votes for each candidate include:
    Charles Casper Stockham: 85,213 (23.0%)
    Diana DeGette: 272,892 (73.8%)
    Raymon Anthony Doane: 11,606 (3.1%)

- Diana DeGette got was the winner of the election with 272,892 votes (82.8%).

## Election Audit Summary 

This particular code works well for this election, but with a few modifications it can also work for other elections. Variable names, dictionary keys, and lists can be changed.  For example, the presidental election.  We could change county to state in order to see what states has the highest turnout.  To make the total percentage of voters more accurate, we could use the total amount of the of age population for each state.  Another example would be high school student class president elections.  Where instead of canidate in the case, we could use the variable student. 