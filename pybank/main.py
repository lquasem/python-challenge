import os
import csv
 #Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset so create variable

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period
months_row_count=0
Profit_loss_Total=0
Month_of_change= []
Net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999999999999999]


csvpath = os.path.join("budget_data.csv")
csvoutput = os.path.join("budget_analysis.txt")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers
    first_row = next(csvreader)
    months_row_count = (months_row_count  + 1)
    previous_net_profit_loss = int(first_row[1])

    for row in csvreader:
         # track the total
         months_row_count = (months_row_count  + 1)
         Profit_loss_Total = Profit_loss_Total+ (float)(row[1])
         # track the change
            #  Month_of_change= row[0]
        #  Net_change_list = row[1]
         net_change = int(row[1]) - previous_net_profit_loss
         previous_net_profit_loss = int(first_row[1])
         Net_change_list = Net_change_list + [net_change]
         Month_of_change = Month_of_change + [row[0]] 
        # greatest increase
         if net_change > greatest_increase[1]:
           greatest_increase[0]= row[0]
           greatest_increase[1]= net_change
        # greatest decrease
         if net_change < greatest_decrease[1]:
           greatest_decrease[0]= row[0]
           greatest_decrease[1]= net_change


# calculate average change
average_change= sum(Net_change_list)/len(Net_change_list)
round_average_change = round(average_change,2)

#print results
print("Total Months: " + (str)(months_row_count))
print("Net total Profit_Loss:" + (str)(Profit_loss_Total))
print("Average Change: " + (str)(round_average_change))
print("Greatest Increase: " + (str)(greatest_increase))
print("Greatest Decrease: " + (str)(greatest_decrease))

#Generate Output Summary
Output = (
    f"\nFinancial Analysis\n"
    f".....................\n"
    f"Total Months:{months_row_count}\n"  
    f"Average Change: ${round_average_change}\n" 
    f"Greatest Increase:  + {greatest_increase}\n"
    f"Greatest Decrease:  + {greatest_decrease}\n"
)


f= open("Financial Analysis.txt","w+")
f.write(Output)

         
     
    



















         
#     for i = row[1]:
#     if i != next() 
#      in range(0,len(Profit_loss_Avg)):
        
         
#          # Sum = sum(numbers) 
# #average= Sum/len(numbers)  
# #print average 

# print("Total Months:" + (str)(months_row_count))
# print("Net Profit/Losses: " + (str)(Profit_loss_Total))
# print("Avg of Changes:" + (str)(Profit_loss_Avg))

