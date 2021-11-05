#import Libraries
import os
import csv

#search for a file
budget_data_csv = os.path.join("C:\Users\Victor M Diaz\python-challenge\Resources")

#set the output of the text file
file_path = "output.txt"

#Set variables
Months_In_Total = 0
The_Total_Revenue = 0
Revenue = []
The_Previous_Revenue = 0
The_Change_Of_Month = []
The_Change_In_Revenue = 0
most_decrease = ["", 9999999]
most_increase = ["", 0]
revenue_change_list = []
The_Revenue_Avg = 0


#open the csv file
with open('budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        Months_In_Total += 1

        #Calculate the total revenue over the entire period
        The_Total_Revenue = The_Total_Revenue + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        The_Change_In_Revenue = float(row["Profit/Losses"])- The_Previous_Revenue
        The_Previous_Revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [The_Change_In_Revenue]
        The_Change_Of_Month = [The_Change_Of_Month] + [row["Date"]]
       

        #The greatest increase in revenue (date and amount) over the entire period
        if The_Change_In_Revenue > most_increase[1]:
            most_increase[1]= The_Change_In_Revenue
            most_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if The_Change_In_Revenue < most_decrease[1]:
            most_decrease[1]= The_Change_In_Revenue
            most_decrease[0] = row['Date']
    The_Revenue_Avg = sum(revenue_change_list)/len(revenue_change_list)

#write changes to csv
with open(file_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("The Total Months Is: %d\n" % Months_In_Total)
    file.write("Total Revenue: $%d\n" % The_Total_Revenue)
    file.write("Average Revenue Change $%d\n" % The_Revenue_Avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (most_increase[0], most_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (most_decrease[0], most_decrease[1]))
