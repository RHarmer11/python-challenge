import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#C:\Users\Bobby\Desktop\BOOTCAMP FOLDERS\python-challenge\PyBank\Resources\budget_data.csv
print(csvpath)

with open(csvpath, newline='') as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#      print(csvreader)

# Read the header row first (skip this step if there is now header)
     #csv_header = next(csvreader)
     #print(f"CSV Header: {csv_header}")
     #print(type(csv_header))

    # for colname in csv_header:
    #     print(colname)
    Total = 0
#     # Read each row of data after the header
     #for row in csvreader:
     #   print(row)
     # Calc for # of months
    #  TotalMonths = len(list(csvreader))
    #  print(TotalMonths)  
     
     # Calc for Total Profits/Losses
    for row in csvreader:
        Total = sum(int(row[1]) for row in csvreader)
        print(Total)
      #  Total += int(row[1])
     #calc for Avg Profit/Losses   
#         AvgProfitLoss = Total/TotalMonths

#      #calc for Greatest incr in Profits
     
     
     
#      #calc for greatest increase in losses
        
#     #    print(TotalMonths) 
#        # print(Total)

# # Set variable for output file
 output_file = os.path.join("bank.csv")

# #  Open the output file
 with open(output_file, "w", newline="") as datafile:
     writer = csv.writer(datafile)

#     # Write the header row
     writer.writerow("Financial Analysis")

# Write second row
     writer.writerow("________________________")
     
#     # Write in zipped row
#     writer.writerows(cleaned_csv)
  
        
