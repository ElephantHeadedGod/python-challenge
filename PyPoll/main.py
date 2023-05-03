#import OS allows us to create file paths for Mac, Linux, or Windows
import os 
#Importing csv allows us to read csv files
import csv 
import statistics

csvpath = os.path.join( 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the header in variable csv_header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

 # Read each row of data after the header
    #create new variable row count
    rowCount = 0
    ballotIDArray= []
    countyArray = []
    candidateArray = []
    for row in csvreader:
       # print(row)
        #add one to rowcount every time a new row is printed
        rowCount = rowCount + 1
        ballotIDArray.append(row[0])
        countyArray.append(row[1])
        candidateArray.append(row[2])

    print("Total Votes:",rowCount)
    candidateRowCount = 0
    uniquecandidates = []
    for i in candidateArray:
        if candidateRowCount == 0:
            uniquecandidates.append(candidateArray[candidateRowCount])
        else:
            if candidateArray[candidateRowCount] != candidateArray[candidateRowCount - 1]:
                if candidateArray[candidateRowCount] not in uniquecandidates:
                    uniquecandidates.append(candidateArray[candidateRowCount])
        candidateRowCount = candidateRowCount + 1
    print(uniquecandidates)

    candidateVoteCount = [0,0,0]
    candidateIndex = 0
    for i in uniquecandidates:
        for j in candidateArray:
            if i == j:
                candidateVoteCount[candidateIndex] = candidateVoteCount[candidateIndex] + 1
        candidateIndex =candidateIndex + 1
    print(candidateVoteCount)
    totalVotes = candidateVoteCount[0] + candidateVoteCount[1] + candidateVoteCount[2]
    Candidate1VotesPercent = (candidateVoteCount[0]/totalVotes)*100
    Candidate2VotesPercent = (candidateVoteCount[1]/totalVotes)*100
    Candidate3VotesPercent = (candidateVoteCount[2]/totalVotes)*100
    print(Candidate1VotesPercent)
    print(Candidate2VotesPercent)
    print(Candidate3VotesPercent)

    print(uniquecandidates[0],":",Candidate1VotesPercent,"%","(", candidateVoteCount[0],")")
    print(uniquecandidates[1],":",Candidate2VotesPercent,"%","(", candidateVoteCount[1],")")
    print(uniquecandidates[2],":",Candidate3VotesPercent,"%","(", candidateVoteCount[2],")")

    if Candidate1VotesPercent > Candidate2VotesPercent and Candidate1VotesPercent > Candidate3VotesPercent:
        print("Winner:", uniquecandidates[0])
    elif Candidate2VotesPercent > Candidate1VotesPercent and Candidate2VotesPercent > Candidate3VotesPercent:
        print("Winner:", uniquecandidates[1])
    elif Candidate3VotesPercent > Candidate1VotesPercent and Candidate3VotesPercent > Candidate2VotesPercent:
        print("Winner:", uniquecandidates[2])


    Analysis= open("analysis\Analysis.txt","w+")

Analysis.write("Election Results" + "\n")
Analysis.write("Total Votes:"+ str(rowCount) + "\n")
Analysis.write(str(uniquecandidates[0]) + ":" + str(Candidate1VotesPercent) +"%" + "(" + str(candidateVoteCount[0]) + ")"+"\n")
Analysis.write(str(uniquecandidates[1]) + ":" + str(Candidate2VotesPercent) +"%" + "(" + str(candidateVoteCount[1]) + ")"+"\n")
Analysis.write(str(uniquecandidates[2]) + ":" + str(Candidate3VotesPercent) +"%" + "(" + str(candidateVoteCount[2]) + ")"+"\n")
Analysis.write("Winner:" + str(uniquecandidates[1]))

Analysis.close()