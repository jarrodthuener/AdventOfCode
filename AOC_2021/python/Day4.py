from get_data import get_data

import pandas as pd
import numpy as np
# np.random.BitGenerator = np.random.bit_generator.BitGenerator
# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(4)

# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer
# print(sampleData)
# newSampleData = sampleData[2:]
# # newSampleData.split()
#
# for row in newSampleData:
#     print(row.split())

# https://www.youtube.com/watch?v=Jv8dQT3uodY

def part1solution(puzzleData):
    """
    Objective: track the numbers called for each board and when each board wins.

    Steps to be taken to solve the problem:
    extract numbers called for later
    insert puzzle data into dataframe and label with board numbers.
    """
    # extract the numbers called into a separate list
    numbersCalled = puzzleData[0].split(',')

    """ clean puzzle data """
    # put puzzle list into dataframe
    # start with row 3 (index 2+)
    df = pd.DataFrame(puzzleData[2:])

    # assign board numbers
    # look 1 row above (shift data 1 row) for empty rows and mark with a 1
    df['boardNum'] = np.where(df.shift(1) == "",1,0)

    # take cumsum for the column to make all rows within a board the same
    df['boardNum'] = df['boardNum'].cumsum()

    # remove lines that are empty
    df = df[df[0]!=""]

    # replace multiple spaces with a single space
    df[0] = df[0].str.strip().replace('\s+',' ',regex=True)
    # print(df)

    # split the board lines into columns by a single space
    df[["a","b","c","d","e"]] = df[0].str.split(' ', 4, expand=True)

    # df[["a","b","c","d","e"]] = df[0].str.split()

    # drop the first field
    df = df.drop([0],axis=1)

    # add a "solved" field for the flag
    df["solved"]=False

    """ for all boards replace the number called with a dash ("-") """
    def replaceNumber(df,numberCalled):
        df[['a','b','c','d','e']] = df[['a','b','c','d','e']].replace(numberCalled,'-')
        return df

    def checkBoard(df,boardnumber):
        board = df[df['boardNum'] == boardnumber]
        columns = ['a','b','c','d','e']
        rows = [0, 1, 2, 3, 4]
        if max([len(board[board[x] == '-']) for x in columns]) == 5:
            return True
        elif max([len(board.iloc[x][board.iloc[x] == '-']) for x in rows]) == 5:
            return True
        else:
            return False


    # if checkBoard(df,0):
    #     df["solved"]=True

    # Call the numbers in order
    # print(df)
    for i in numbersCalled:
        # print(i)
        replaceNumber(df, i)
        # print('number called: '+i)
        for boardNum in range(df['boardNum'].max()+1):
            # print(df[df['boardNum']==boardNum])
            if checkBoard(df,boardNum):
                # now we found the first solved board, so let's find all the numbers to add them up
                """keep this line below for future reference, it is how we will identify boards that have been solved"""
                df["solved"]=np.where(df['boardNum'] == boardNum,True,df["solved"])

                winningBoard = df[df["boardNum"]==boardNum]
                # print(winningBoard)
                winningBoard[['a','b','c','d','e']] = winningBoard[['a','b','c','d','e']].replace('-','0')

                # # we need to find the sum of all unmarked numbers and multiply it by the number just called
                numberLastCalled = int(i)

                sum = 0
                for i in ['a','b','c','d','e']:
                    sum += winningBoard[i].astype('int32').sum()
                # print(numberLastCalled)
                # print(sum)
                # return sum
                return sum * numberLastCalled

                # return df[df['boardNum']==boardNum]
                # print('This is done')
                # return df
                break
            else:
                continue
    # print(df)
    # print(df)





    # print(checkBoard(df,0))
    # print(df)

    # print(df)


    # for i in range(df['boardNum'].max()):
    #     print(i)



    # board = df[df['boardNum']==1]
    # print(board)

    # for df.columns in df:
    #     print(df.columns)

    # print(df)
    #
    # df["boardNum"] =
    # boards = df.transpose()
    # print(boards)


    # return df



#Run the sampleData
print("Part 1 sample data answer: "+ str(part1solution(sampleData)))

#Run the fullData
# print("Part 1 full data answer: "+ str(part1solution(fullData)))


def part2solution(puzzleData):
    """
    Objective:

    Steps to be taken to solve the problem:

    """
    



#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))