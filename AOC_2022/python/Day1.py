from get_data import get_data

import numpy as np
import pandas as pd

# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(1)

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


    """ clean puzzle data """
    # put puzzle list into dataframe
    # start with row 3 (index 2+)
    df = pd.DataFrame(puzzleData)

    # assign board numbers
    # look 1 row above (shift data 1 row) for empty rows and mark with a 1
    df['block'] = np.where(df.shift(1) == "",1,0)

    # take cumsum for the column to make all rows within a board the same
    df['block'] = df['block'].cumsum()

    # remove lines that are empty
    df = df[df[0]!=""]

    # change to integer
    df = df.astype({0:int})

    '''sum calories by block'''
    dfSum = df.groupby('block')[0].sum()

    return dfSum.max()

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


    """ clean puzzle data """
    # put puzzle list into dataframe
    # start with row 3 (index 2+)
    df = pd.DataFrame(puzzleData)

    # assign board numbers
    # look 1 row above (shift data 1 row) for empty rows and mark with a 1
    df['block'] = np.where(df.shift(1) == "",1,0)

    # take cumsum for the column to make all rows within a board the same
    df['block'] = df['block'].cumsum()

    # remove lines that are empty
    df = df[df[0]!=""]

    # change to integer
    df = df.astype({0:int})

    '''sum calories by block'''
    dfSum = df.groupby('block')[0].sum()

    dfSum = dfSum.nlargest(3,'first').sum()

    return dfSum.max()


#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))