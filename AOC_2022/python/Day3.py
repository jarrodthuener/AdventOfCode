from get_data import get_data

import numpy as np
import pandas as pd

# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(3)

# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer

def part1solution(puzzleData):
    """
    Objective:
    summarize each elf's calories and find the total calories for the elf with the most.

    Steps to be taken to solve the problem:
    break apart the data on empty values to create groups of elves
    summarize the total calories per elf
    find what the max value is
    """
    # x = [i for i, s in enumerate(puzzleData) if s == '']
    # y = x[1:] + [len(puzzleData)]
    # z = [puzzleData[i:j] for i, j in zip(x,y)]
    #
    # print(z)
    # print(puzzleData)

    # print(puzzleData)
    charIntSum = 0

    def charIntConv(char):
        if ord(char) < 91:
            return ord(char)-38
        else:
            return ord(char)-96

    for row in puzzleData:
        matchedChar = ''
        length = len(row)
        splitlen = int(length/2)
        left = row[0:splitlen]
        right = row[splitlen:length]
        for i in left:
            if right.__contains__(i):
                matchedChar = i
                charIntSum += charIntConv(matchedChar)

                break
            else:
                continue

        #print(row)
        #print(left)
        #print(matchedChar)
        #print(ord(matchedChar))



    return charIntSum

#Run the sampleData
print("Part 1 sample data answer: "+ str(part1solution(sampleData)))

#Run the fullData
print("Part 1 full data answer: "+ str(part1solution(fullData)))


def part2solution(puzzleData):
    """
    Objective:
    summarize each elf's calories and find the total calories for the elf with the most.

    Steps to be taken to solve the problem:
    break apart the data on empty values to create groups of elves
    summarize the total calories per elf
    find what the max value is for the top 3 elves
    """

    return


#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))