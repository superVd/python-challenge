 
# Import Libraries
import os
import csv

# Set Files Path for Input and Output
csvpath = os.path.join("C:\Users\Victor M Diaz\python-challenge")
output_of_election = "election_results.txt"

# Create Variables 
Count_Total_Votes = 0
Candidates = []
Per_Candidate_Votes = {}
Total_Win_Count = 0
winner_is = ""




# Open the File
with open('election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #find the total votes
    for row in csvreader:

        # count the votes
        Count_Total_Votes += 1
        candidate = row["Candidate"]

        # run first occurance and distinguish unique candidates
        if candidate not in Candidates:
            Candidates.append(candidate)
            Per_Candidate_Votes[candidate] = 1
        
        Per_Candidate_Votes[candidate] = Per_Candidate_Votes[candidate] + 1



#the winning candidate is
with open(output_of_election, 'w') as txt_file:

    #create header
    write_election_header = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(write_election_header)

    #Calculte total votes of each candidate and output winner
    for candidate in Per_Candidate_Votes:
        Overall_votes = Per_Candidate_Votes[candidate]
        vote_percentage = float(Overall_votes)/float(Count_Total_Votes)*100
        if (Overall_votes > Total_Win_Count):
            Total_Win_Count = Overall_votes
            winner_is = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({Overall_votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    congrats_winning_summary = (
        f"Winner: {winner_is}"
    )
    print(congrats_winning_summary)
    txt_file.write(congrats_winning_summary)


   