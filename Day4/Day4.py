# Advent of Code: Day 4
# Author: Laura Fry     Date: Dec 4, 2023

# Imports
import re

def calculateTotalPoints():
    file = open("Day4Data.txt", "r")
    totalPoints = 0
    for lineNumber, line in enumerate(file.readlines(), start=1):
        cardNoTitle = re.sub(r'Card\s+\d{1,3}.\s', "", line)
        splitData = cardNoTitle.split('|')
        winningNumbers = splitData[0].strip()
        scratchCardNumbers = splitData[1].strip()
        # print(winningNumbers)
        # print(scratchCardNumbers)
        winningNumbersSet = set(map(int, filter(None, winningNumbers.split())))
        scratchCardNumbersSet = set(map(int, filter(None, scratchCardNumbers.split())))
        winners = winningNumbersSet.intersection(scratchCardNumbersSet)
        if winners:
            print("Winners: ", winners)
            if (len(winners) == 10):
                points = 512
            elif (len(winners) == 9):
                points = 256
            elif (len(winners) == 8):
                points = 128
            elif (len(winners) == 7):
                points = 64
            elif (len(winners) == 6):
                points = 32
            elif (len(winners) == 5):
                points = 16
            elif (len(winners) == 4):
                points = 8
            elif (len(winners) == 3):
                points = 4
            elif (len(winners) == 2):
                points = 2
            elif (len(winners) == 1):
                points = 1
            else:
                points = 0
            totalPoints += points
            print(totalPoints)
        else:
            print("No Winners.")
    file.close()

def main():
    print("Welcome to the Advent of Code: Day 4!")
    calculateTotalPoints()

if __name__ == '__main__':
    main()