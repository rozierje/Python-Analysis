# import operating system
import os

# impoert the csv reader
import csv
#locate csv file for election results
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
#create empty carts for candidate list
candidate_list = []
#static adding candidates
candidates = {}
candidatename = ""
#dynamic adding candidates
#candidates["Khan"] = 0
winnervotes = 0
winner = ""
#set vote count total
total_votes = 0

# Format Final Table
print("Election Results")
print("-------------------")

#Gather Total Votes
with open(csvpath) as election_results:
   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(election_results, delimiter=',')
   # reading first row of the file
   header = next(csvreader)
   # Read each additional row of data after the header
   for row in csvreader:
      #building total votes
      total_votes += 1
      #getting candidate name from column index 2
      candidatename = row[2]
         #searching for candidate name in candidate_list
      if candidatename not in candidate_list:
      # if not in list, add it; if in list move on
         candidate_list.append(candidatename)
         #if already in list, add the candidate to the dictionary; 
         # initialize candidate with 1 vote
         #{"Khan":0}
         candidates[candidatename] = 0
      candidates[candidatename] = candidates[candidatename] + 1
   print("Total Votes")
   print(total_votes)
   print("-----------------------")
#-------------------- good to this point------------------------------        
      #finding the individual candiate names
   for candidate in candidates:
      #for each candidate, get the votes for that candidate
      candidate_votes = candidates[candidate]
      #for total per candidate, divide by total votes cast
      candidate_percentage = candidate_votes/total_votes * 100
      #print the strings for formatting
      print(f"{candidate}: {candidate_percentage:.3f}% ({candidate_votes})")
      #going through dictionary to find candidate with most votes (line 51)
      if candidate_votes > winnervotes:
         #assigning candidate_votes to winner votes
         winnervotes = candidate_votes
         #assigns candidate to winner
         winner = candidate
   print("--------------------------------")
   print(f"Winner: {winner}")
   print("--------------------------------")


################### write new text file ########################

# Specify the file to write to
output_path = os.path.join("..", "PyPoll", "Analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

   # Initialize csv.writer
   csvwriter = csv.writer(txtfile, delimiter=',')

   # Write the Vote results as CSV
   csvwriter.writerow(["Election Results"])
   csvwriter.writerow(["-------------------------------------"])
   csvwriter.writerow(["Total Votes: " + str(total_votes) +" "])
   csvwriter.writerow(["--------------------------------------"])
   csvwriter.writerow(f'{candidates}: {candidate_percentage:.3f}% ({candidate_votes})')
   csvwriter.writerow(["--------------------------------------"])
   csvwriter.writerow([f"Winner: {winner}"])
   csvwriter.writerow(["--------------------------------------"])