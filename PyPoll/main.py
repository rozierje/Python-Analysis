# import operating system
import os

# impoert the csv reader
import csv
#locate csv file for election results
csvpath = os.path.join('Resources', 'election_data.csv')
#create empty carts for candidate list
candidate_list = []
votes = []
table = []
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
         table.append(candidatename)
         #if already in list, add the candidate to the dictionary; 
         # initialize candidate with 1 vote
         #{"Khan":0}
         candidates[candidatename] = 0
      candidates[candidatename] = candidates[candidatename] + 1
   print("Total Votes: " + str(total_votes))
   print("-----------------------")
       
      #finding the individual candiate names
   for candidate in candidates:
      #for each candidate, get the votes for that candidate
      candidate_votes = candidates[candidate]
      table.append(candidate_votes)
      #for total per candidate, divide by total votes cast
      candidate_percentage = round((candidate_votes/total_votes * 100),3)
      table.append(candidate_percentage)
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
output_path = os.path.join("Analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

   # Initialize csv.writer
   wr = csv.writer(txtfile, quoting=csv.QUOTE_ALL)

   # Write the Vote results as CSV
   wr.writerow(["Election Results"])
   wr.writerow(["-------------------------------------"])
   wr.writerow(["Total Votes: " + str(total_votes) +" "])
   wr.writerow(["--------------------------------------"])
   x=len(candidate_list)
   for i in range(x):
      wr.writerow([f'{candidate_list[i]}: {table[i+x]} {table[i+x+1]}%'])
      table.pop(i+x)
      i=i+1
   wr.writerow(["--------------------------------------"])
   wr.writerow([f"Winner: {winner}"])
   wr.writerow(["--------------------------------------"])