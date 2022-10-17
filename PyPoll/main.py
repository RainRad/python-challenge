#imports
import os
import csv
import copy

#starting values
total_votes = 0
candidates = {}

#read file
election_csv = os.path.join('Resources','election_data.csv')
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:

        #counts total votes
        total_votes += 1

        #counts existing candidate votes
        if row[2] in candidates:
            candidates[row[2]] += 1

        #adds new candidates to candidate list
        if row[2] not in candidates:
            candidates[row[2]] = 1
        
#determine winner
winner = max(candidates, key=candidates.get)

#create vote percentage dictionary
vote_percent = candidates.copy()

#calcs and sets values for vote % dictionary
for x in vote_percent:
    y = vote_percent[x]
    vote_percent[x] = round((y/total_votes) *100, 3)

#output terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for key, value in candidates.items():
    print(f"{key} {vote_percent[key]}% ({candidates[key]})")
print("-------------------------")
print(f"{winner}")
print("-------------------------")



#output to txt file
outputfile = os.path.join('analysis','election_analysis.txt')

with open(outputfile,"w") as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------\n")
    for key, value in candidates.items():
        text.write(f"{key} {vote_percent[key]}% ({candidates[key]})\n")
    text.write("-------------------------\n")
    text.write(f"{winner}\n")
    text.write("-------------------------\n")
