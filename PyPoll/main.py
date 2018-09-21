import os
import csv
import string
from collections import Counter


csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#C:\Users\Bobby\Desktop\BOOTCAMP FOLDERS\python-challenge\PyBank\Resources\budget_data.csv
print(csvpath)

with open(csvpath, newline='') as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    votes = []
    persons = []
    words_counted = []
# #     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))

    # TotalVotes = len(list(csvreader))
    # print(f"Total Votes =" + str(TotalVotes ))

# Get all Candidates
    # for row in csvreader:
    #     votes.append(row{2])
    # print(votes)
    #  lines = [line for line in csvreader] 
    #  counts = Counter([1[1] for 1 in lines])
    # #  for row in csvreader 
    # #     cnt[row] += 1
    #  print(counts)
    for row in csvreader:
        csv_words = row[2].split(" ")
        for i in csv_words:
          persons.append(i)

    words_counted = []
    for i in persons:
    x = persons.count(i)
    words_counted.append((i,x))
print(words_counted)

# with open('output.csv', 'wb') as f:
# writer = csv.writer(f)
# writer.writerows(edgl)