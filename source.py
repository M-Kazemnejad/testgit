import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    outputString = ''
    with open(input_file_name) as f: # Opening CSV file
        reader = csv.reader(f) # Reading CSV file
        for row in reader:  # Reading each row of CSV file
            nameOfStudent = row[0] # Name of student in this file is first item
            scores = row[1:] # After first item is scores
            listOfScores = list(map(int,scores)) # Converting list of string scores to list of integer scores
            average = mean(listOfScores)
            outputString = outputString + '%s,%f\n' % (nameOfStudent,average)
    with open(output_file_name, 'w') as outputFile:
        outputFile.write(outputString)


def calculate_sorted_averages(input_file_name, output_file_name):
    outputString = ''
    mydict = dict()
    with open(input_file_name) as f: # Opening CSV file
        reader = csv.reader(f) # Reading CSV file
        for row in reader:  # Reading each row of CSV file
            nameOfStudent = row[0] # Name of student in this file is first item
            scores = row[1:] # After first item is scores
            listOfScores = list(map(int,scores)) # Converting list of string scores to list of integer scores
            average = mean(listOfScores)
            mydict[nameOfStudent] = average # Adding items to dictionary
        
        # Sorting values of dictionry    
        sortedDict = sorted(mydict.items(), key=lambda a:(a[1],a[0]))
        # Reading our ordered dictionary
        for name,averageScore in sortedDict:
            outputString = outputString + '%s,%f\n'%(name, averageScore)
    with open(output_file_name, 'w') as f:
        f.write(outputString)


def calculate_three_best(input_file_name, output_file_name):
    outputString = ''
    mydict = dict()
    with open(input_file_name) as f: # Opening CSV file
        reader = csv.reader(f) # Reading CSV file
        for row in reader:  # Reading each row of CSV file
            nameOfStudent = row[0] # Name of student in this file is first item
            scores = row[1:] # After first item is scores
            listOfScores = list(map(int,scores)) # Converting list of string scores to list of integer scores
            average = mean(listOfScores)
            mydict[nameOfStudent] = average # Adding items to dictionary
        
        # Sorting values of dictionry: Descending by fisrt item and Ascending by second item
        sortedDict = sorted(mydict.items(), key=lambda a: (-a[1],a[0]))
        threeBestStudents = sortedDict[0:3]
        # Reading our ordered dictionary
        for name,averageScore in threeBestStudents:
            outputString = outputString + '%s,%f\n'%(name, averageScore)
    with open(output_file_name, 'w') as f:
        f.write(outputString)
    


def calculate_three_worst(input_file_name, output_file_name):
    outputString = ''
    mydict = dict()
    with open(input_file_name) as f: # Opening CSV file
        reader = csv.reader(f) # Reading CSV file
        for row in reader:  # Reading each row of CSV file
            nameOfStudent = row[0] # Name of student in this file is first item
            scores = row[1:] # After first item is scores
            listOfScores = list(map(int,scores)) # Converting list of string scores to list of integer scores
            average = mean(listOfScores)
            mydict[nameOfStudent] = average # Adding items to dictionary
        
        # Sorting values of dictionry
        sortedDict = sorted(mydict.items(), key=lambda a: (a[1],a[0]))
        threeWorstStudents = sortedDict[0:3]
        # Reading our ordered dictionary
        for name,averageScore in threeWorstStudents:
            outputString = outputString + '%f\n'%(averageScore)
    with open(output_file_name, 'w') as f:
        f.write(outputString)


def calculate_average_of_averages(input_file_name, output_file_name):
    listOfAverage = list()
    with open(input_file_name) as f: # Opening CSV file
        reader = csv.reader(f) # Reading CSV file
        for row in reader:  # Reading each row of CSV file
            nameOfStudent = row[0] # Name of student in this file is first item
            scores = row[1:] # After first item is scores
            listOfScores = list(map(int,scores)) # Converting list of string scores to list of integer scores
            average = mean(listOfScores)
            listOfAverage.append(average) 
        averageOfaverage = mean(listOfAverage)

    with open(output_file_name, 'w') as f:
        f.write(str(averageOfaverage))