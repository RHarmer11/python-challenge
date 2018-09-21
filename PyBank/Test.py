import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#C:\Users\Bobby\Desktop\BOOTCAMP FOLDERS\python-challenge\PyBank\Resources\budget_data.csv
print(csvpath)
with open(csvpath, newline='') as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(type(csv_header))

    TotalMonths = []
    TotalProfit = []
    # ChangeList = []
    # MonthList = []
    
    change = []
    for row in csvreader:
        TotalMonths.append(row[0])
        TotalProfit.append(int(row[1]))
        change.append(row[1])

    # for i in range(len(TotalMonths),-1):
    #     change = Total[i + 1] - Total[1]
    #     ChangeList.append(change)
        
        print(change)
    #    print(ChangeList)
    
    c=sum(TotalProfit)

    
    #print(c)  
        # print(f"TotalProfitLoss =" + str(sum(TotalProfit ))
        # print(Total)()
    
   # AvgProfitLoss = TotalProfit/int(TotalMonths )

    print(f"Total Months = " + str(len(TotalMonths )))
    print(f"TotalProfitLoss = " + str(c))
    #print(f"MinimumProfitLoss = " + str(min(ChangeList))
    #print(f"AvgProfitLoss = " + str(AvgProfitLoss )) 
    # print(f"TotalProfitLoss = " + str(TotalProfit ))

# # Set variable for output file
#  output_file = os.path.join("bank.csv")

# # #  Open the output file
#  with open(output_file, "w", newline="") as datafile:
#      writer = csv.writer(datafile)

# #     # Write the header row
#      writer.writerow("Financial Analysis")

# # Write second row
#      writer.writerow("________________________")
     
#     # Write in zipped row
#     writer.writerows(cleaned_csv)