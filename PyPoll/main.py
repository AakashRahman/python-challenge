import os
import csv
#import Counter

#declaration to the path where new file is creating
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
open_path=r"C:\Users\zubay\OneDrive\Desktop\Working folder\RUT-SOM-DATA-PT-06-2020-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

voter = []
county =[]
candidate=[]
candidate_votes = {}
total_votes = 0

with open(open_path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    
    for row in csvreader:
        candidate.append(row[2])
        voter.append(row[0])
        total_votes += 1
        candidate_name = row[2]
# calculate vote percentage and identify winner

        if candidate_name not in candidate_votes:
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#print(candidate_votes)
#Count the votes for persons and stores in the dictionary

khan_pct = (candidate_votes['Khan'] / float(total_votes)) * 100
Correy_pct = (candidate_votes['Correy'] / float(total_votes)) * 100
Li_pct = (candidate_votes['Li'] / float(total_votes)) * 100
OTooley_pct = (candidate_votes["O'Tooley"] / float(total_votes)) * 100

print("Election Results")
print("----------------")
print(f"Total Votes: {len(voter)}")
print("----------------")
print(f"Khan: {khan_pct:.3f}% ({candidate_votes['Khan']})")
print(f"Correy: {Correy_pct:.3f}% ({candidate_votes['Correy']})")
print(f"Li: {Li_pct:.3f}% ({candidate_votes['Li']})")
print(f"O'Tooley: {OTooley_pct:.3f}%")  
print("----------------")

candidate_name=max(candidate_votes, key=candidate_votes.get)
print(f"Winner:  {candidate_name}")

#Output the entire result as text file
output_path = r"C:\Users\zubay\OneDrive\Desktop\Working folder\RUT-SOM-DATA-PT-06-2020-U-C\02-Homework\03-Python\python-challenge\PyPoll\Election_Results.txt"


# open file to use csv file using "write" mode

with open(output_path, 'w') as text:
    
    #inicialize the text writer
   
    #write column or row
    text.write("Election Results \r\n" )
    text.write("----------------\r\n")
    text.write(f"Total Votes: {len(voter)} \r\n")
    text.write("----------------\r\n")
    text.write(f"Khan: {khan_pct:.3f}% ({candidate_votes['Khan']}) \r\n")
    text.write(f"Correy: {Correy_pct:.3f}% ({candidate_votes['Correy']}) \r\n")
    text.write(f"Li: {Li_pct:.3f}% ({candidate_votes['Li']}) \r\n")
    text.write(f"O'Tooley: {khan_pct:.3f}% \r\n")
    text.write("---------------- \r\n")
    text.write(f"Winner:  {candidate_name} \r\n")






   

    
    
     
