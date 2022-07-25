# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# add our dependencies
import csv
import os

# add a variable to load a file from a path
# file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")
# add a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# candidate options & candidate votes
candidate_options = []
candidate_votes = {}

# 1. create a county list & county votes dictionary
county_names = []
county_votes = {}

# track the winning candidate, vote count & %
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2. track the largest county & county voter turnout
largest_county_turnout = ""
largest_county_vote = 0

# read the csv & convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # read the header
    header = next(reader)

    # for each row in the CSV file
    for row in reader:

        # add to the total vote count
        total_votes = total_votes + 1

        # get the candidate name from each row
        candidate_name = row[2]

        # 3. extract the county name from each row
        county_name = row[1]

        # if the candidate doesn't match any existing candidate 
        # add it to the candidate list
        if candidate_name not in candidate_options:

            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # & begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a. write an if statement that checks that the county 
        # doesn't match any existing county in the county list
        if county_name not in county_names:

            # 4b. add the existing county to the list of counties
            county_names.append(county_name)

            # 4c. begin tracking the county's vote count
            county_votes[county_name] = 0

        # 5. add a vote to that county's vote count
        county_votes[county_name] += 1


# save the results to the text file
with open(file_to_save, "w") as txt_file:

    # print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a. write a for loop to get the county from the county dictionary
    for county in county_votes:
        # 6b. retrieve the county vote count
        county_vote = county_votes[county]
        # 6c. calculate the % of votes for the county
        county_percent = float(county_vote) / float(total_votes) * 100

         # 6d. print the county results to the terminal
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end="")

        # 6e. save the county votes to a text file
        txt_file.write(county_results)

        # 6f. write an if statement to determine the winning county & get its vote count
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    #  7. print the county with the largest turnout to the terminal
    largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_turnout)

    # 8. save the county with the largest turnout to a text file
    txt_file.write(largest_county_turnout)

    # save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # retrieve vote count & %
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print each candidate's voter count & % to the
        # terminal
        print(candidate_results)
        #  Save the candidate results to our text file
        txt_file.write(candidate_results)

        # determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
