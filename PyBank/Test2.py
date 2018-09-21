import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

print(csvpath)
with open(csvpath, newline='') as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))

    #AvgChange = 0
    TotalMonths = []
    ChangeList = []
    MonthList = []
    
    change = 0
    #for i in csvreader:
    # for i, row in enumerate(csvreader):
    #     print(i,row[1],i+1,row([1][+1])
    #     #print(row[1], row[1]-1)

    for row in csvreader:
        TotalMonths.append(row[0])



    for i in range(len(TotalMonths),-1):
        change = Total[i + 1] - Total[1]
        ChangeList.append(change)
        
    print(change)
    print(ChangeList)