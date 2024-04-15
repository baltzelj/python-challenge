import os
import csv
# functions and dictionaries.
def candidate_votes(dictionary, candidate):
    if candidate not in dictionary:
        dictionary[candidate] = 1
    else:
        dictionary[candidate] = dictionary[candidate] + 1
def voting_printout(dictionary):
    print(
        f"Election Results\n"
        "-----------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-----------------------------"
         )
    for candidate, votes in dictionary.items():
        print(f"{candidate}: {round(votes/total_votes*100,3)}% ({votes})")
    print(
        f"-----------------------------\n"
        f"Winner: {elect}"
        )
# dictionaries and pre-set variables for use throughout the code.
candidates = {}
total_votes = 0
winner_votes = 0
# setting up file path.
polls_data = os.path.join("..","PyPoll","election_data.csv")
with open(polls_data) as election_data:
    polls = csv.reader(election_data, delimiter=",")
    header = next(election_data)
    # calculating total number of votes cast.
    for row in polls:
        total_votes += 1
        candidate_votes(candidates,row[2])
    # identifying the winner of the election.
    for key, value in candidates.items():
        if value > winner_votes:
            winner_votes = value
            winner_elect = key
    voting_printout(candidates)
# writing to text file.
poll_report = os.path.join("..","PyPoll","analysis.txt")
with open(poll_report, "w") as analysis_report:
    analysis_report.write(
        f"Election Results\n"
        "-----------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-----------------------------\n"
    )
    for candidate, votes in candidates.items():
        analysis_report.write(f"{candidate}: {round(votes/total_votes*100,3)}% ({votes})\n")
    analysis_report.write(
        f"-----------------------------\n"
        f"Winner: {elect}"
    )