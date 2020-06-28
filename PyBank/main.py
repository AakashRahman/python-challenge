#call dependency
import os
import csv


#declaration to the path where new file is creating
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
csv_path = r"C:\Users\zubay\OneDrive\Desktop\Working folder\RUT-SOM-DATA-PT-06-2020-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"
months=[]
profits=[]
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_ header}")
    
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

#Total calculation:
print(f"Total Months: {len(months)}")
print(f"Total : ${sum(profits)}")
print(f"Average Change: ${round(sum(profits)/len(months))}")
print(f"Greatest Increase in Profits: {months[profits.index(max(profits))]} (${max(profits)})")
print(f"Greatest Decrease in Profits: {months[profits.index(min(profits))]} (${min(profits)})")        


output_path = r"C:\Users\zubay\OneDrive\Desktop\Working folder\RUT-SOM-DATA-PT-06-2020-U-C\02-Homework\03-Python\python-challenge\PyBank\Financial_Analysis.txt"


# open file to use csv file using "write" mode

with open(output_path, 'w') as text:
    
    #inicialize the text writer
   
    #write column or row
    text.write('Financial Analysis \r\n')
    text.write('------------------ \r\n')
    
    text.write(f"Total : ${sum(profits)} \r\n")
    text.write(f"Average Change: ${round(sum(profits)/len(months))} \r\n")
    text.write(f"Greatest Increase in Profits: {months[profits.index(max(profits))]} (${max(profits)}) \r\n")
    text.write(f"Greatest Decrease in Profits: {months[profits.index(min(profits))]} (${min(profits)}) \r\n") 
    


    