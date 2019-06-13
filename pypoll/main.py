# * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

import csv
import os


total_votes=0
list_candidates=set()
total_votes_candidate={}
percent_votes_candidate=0



csvpath = os.path.join("election_data.csv")
output = os.path.join("election_results.txt")


with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader, None)  # skip the headers
   row = next(csvreader)
   
  
   for row in csvreader:
        # Calculate total number of votes 
       
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate not in total_votes_candidate:
            total_votes_candidate[candidate] = 1
        else:
            total_votes_candidate[candidate] += 1
        if row[2] in list_candidates:
            #print(row[2])
            continue
        else:
            list_candidates.add(row[2])

         #  make candidate dictionary, candidate = key, votes = count

        

   for key, value in total_votes_candidate.items():
       percent_votes_candidate = str(round((value/total_votes)*100,3)) + "%"   

#Find winner with max 

winner = max(total_votes_candidate, key= total_votes_candidate.get)
     
       
   
# Print the results to the terminal            
# print(total_votes)
# print("List of candidates"+ (str)(list_candidates)  
# print(f"{key}: {percent_votes_candidate} ({value})\n" )
# print(winner)   


#Output to terminal
print("-------------------------------------------\n")
print("Election Results\n")    
print("-------------------------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------------------------\n")
print(f"List of candidates: {list_candidates}\n")  
print("-------------------------------------------\n")
for key, value in total_votes_candidate.items():
    percent_votes_candidate = str(round((value/total_votes)*100,3)) + "%"
    print(f"{key}: {percent_votes_candidate}  ({value})\n" )
print("-------------------------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------------------------\n")


# Generate Output Summary

Election_results = os.path.join("election_results.txt")

with open(Election_results, "w+") as election_results:
    election_results.writelines("-------------------------------------------\n")
    election_results.writelines("Election Results\n")
    election_results.writelines("-------------------------------------------\n")
       
    election_results.writelines(f"Total Votes: {total_votes}\n")
    election_results.writelines("-------------------------------------------\n")
    election_results.writelines(f"List of candidates: {list_candidates}\n")      
    for key, value in total_votes_candidate.items():
        percent_votes_candidate = str(round((value/total_votes)*100,3)) + "%"
        election_results.writelines(f"{key}: {percent_votes_candidate}  ({value})\n" )
    election_results.writelines("-------------------------------------------\n")
    election_results.writelines(f"Winner: {winner}\n")
    election_results.writelines("-------------------------------------------\n")












