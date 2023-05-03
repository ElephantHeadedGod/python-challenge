#import OS allows us to create file paths for Mac, Linux, or Windows
import os 
#Importing csv allows us to read csv files
import csv 
import statistics

csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header in variable csv_header
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #create new variable row count
    rowCount = 0
    dateArray= []
    profitArray = []
    for row in csvreader:
       # print(row)
        #add one to rowcount every time a new row is printed
        rowCount = rowCount + 1
        dateArray.append(row[0])
        profitArray.append(row[1])
    #print row count as the total months
    print("Total Months:",rowCount)
   # print(dateArray)
   # print(profitArray)

    profitSum = 0
    profitLength = len(profitArray)

    for i in profitArray:
        profitSum = profitSum + int(i)

    print("Total: $",profitSum) 

    profitAverage = profitSum/profitLength
    #print(profitAverage)

    profitArrayRowCount = 0
    profitChange = []  
    profitChangeSum = 0
    lastProfit = profitArray[profitLength-1]
    for i in profitArray:
        if profitArrayRowCount == 0:
            profitChange.append(0)
            tempValue = int(i)
        else:
            profitChange.append(int(i)-(tempValue))
            tempValue = int(i)
        #profitChange.append(int(i)-int(tempValue))
        profitChangeSum = profitChangeSum + profitChange[profitArrayRowCount]
    #    print(profitChangeSum)
        profitArrayRowCount = profitArrayRowCount + 1
    #print(profitChangeSum)
    #print(profitArrayRowCount)
    #print(profitChange)
    #profitChange[profitArrayRowCount]
    #print(profitChangeSum)
    averageProfitChange = statistics.mean(profitChange)
    #averageProfitChange = profitChangeSum/86 
    print("Average Change: $",averageProfitChange)

    maxRow = 0
    minRow = 0
    minMaxrowCount = 0
    for i in profitChange:
        if max(profitChange) == int(i):
            maxRow = minMaxrowCount
        if min(profitChange) == int(i):
            minRow = minMaxrowCount
        minMaxrowCount = minMaxrowCount + 1
    print("Greatest Increase in Profits:",dateArray[maxRow],"($",max(profitChange),")")
    print("Greatest Decrease in Profits:",dateArray[minRow],"($",min(profitChange),")")

    increaseProfitsDate = dateArray[maxRow]
    increaseProfits = max(profitChange)
    decreaseProfitsDate = dateArray[minRow]
    decreaseProfits = min(profitChange)

 
Analysis= open("analysis\Analysis.txt","w+")

Analysis.write("Total Months:"+str(rowCount)+"\n")
Analysis.write("Total: $" + str( profitSum)+"\n")
Analysis.write("Average Change: $" + str(averageProfitChange)+"\n")
Analysis.write("Greatest Increase in Profits:"+str(increaseProfitsDate)+"($" + str(increaseProfits)+")\n")
Analysis.write("Greatest Decrease in Profits:"+str(decreaseProfitsDate)+"($"+str(decreaseProfits)+")")

Analysis.close()
