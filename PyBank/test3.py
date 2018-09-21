import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    print(budget_data)
    header = next(budget_data)
    print(header)
    budget_data_rows = list(budget_data)

print(budget_data_rows)

date_col = [row[0] for row in budget_data_rows]
rev_col = [int(row[1]) for row in budget_data_rows]

print(len(date_col))
print(sum(rev_col))
