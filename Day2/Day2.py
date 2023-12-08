# Advent of Code: Day 2
# Author: Laura Fry     Date: Dec 2, 2023

# Imports
import re

regexRed = r"\d{1,2}\sred"
regexGreen = r"\d{1,2}\sgreen"
regexBlue = r"\d{1,2}\sblue"

def calculateSumIDs():
    file = open("Day2Data.txt", "r")
    sumIDs = 0
    for lineNumber, line in enumerate(file.readlines(), start=1):
        gameNoTitle = re.sub(r'Game\s\d{1,3}.\s', '', line)
        redValue = re.findall(regexRed, gameNoTitle)
        redNumbers = [int(number) for number in re.findall(r'\d+', ' '.join(redValue))]
        greenValue = re.findall(regexGreen, gameNoTitle)
        greenNumbers = [int(number) for number in re.findall(r'\d+', ' '.join(greenValue))]
        blueValue = re.findall(regexBlue, gameNoTitle)
        blueNumbers = [int(number) for number in re.findall(r'\d+', ' '.join(blueValue))]
        if any(number > 12 for number in redNumbers):
            print("Greater")
        elif any(number > 13 for number in greenNumbers):
            print("Greater")  
        elif any(number > 14 for number in blueNumbers):
            print("Greater")  
        else:
            sumIDs += lineNumber
            print("Good")
    print("Sum of IDs:")
    print(sumIDs)
            
    file.close()

def main():
    print("Welcome to the Advent of Code: Day 2!")
    calculateSumIDs()

if __name__ == '__main__':
    main()