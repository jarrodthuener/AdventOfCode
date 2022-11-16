from get_data import get_data

# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(1)

# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer

def part1solution(puzzleData):
    """
    Objective: look at the data 1 row behind and check if it is ascending or descending.
    create a counter to track how many ascending rows
    """

    #    find length of puzzleData (number of rows)
    dataLength = len(puzzleData)

    # set variables to be used in the for loop
    prev = puzzleData[0]
    ascendingCount = 0

    """
    for each row starting with the second row check the previous value to see if it is ascending
    skip first since there isn't a previous value
    return the ascendingCount as the answer
    """
    # for each row in the data
    for i in range(1, dataLength):
        if int(puzzleData[i]) > int(prev):
            # increase ascendingCount by 1
            ascendingCount += 1
        # set current value as "previous" for the next run.
        prev = puzzleData[i]
    return ascendingCount


#Run the sampleData
print("Part 1 sample data answer: "+ str(part1solution(sampleData)))

#Run the fullData
print("Part 1 full data answer: "+ str(part1solution(fullData)))


def part2solution(puzzleData):
    """
    Objective: look at the data 1 row behind and check if it is ascending or descending.
    create a counter to track how many ascending rows
    """

    #    find length of puzzleData (number of rows)
    dataLength = len(puzzleData)

    # set variables to be used in the for loop
    prev = puzzleData[0]
    ascendingCount = 0

    """
    for each row starting with the fourth row check the sum of the previous 3 values 
    against the trailing 3 rows starting with the previous row to see if it is ascending
    skip first 3 rows since there isn't a previous trailing value to compare
    return the ascendingCount as the answer
    """
    # create a windowCume function to summarize the 3 previous values
    def windowCume(data, start, lag):
        cume = 0
        for i in range(lag):
            cume = cume + int(data[start - i])
        return cume

    # set prev to the first 3 rows so we can start comparing values
    prev = windowCume(puzzleData, 2, 3)

    # for each row in the data starting with row 4 (index = 3)
    for i in range(3, dataLength):
        if windowCume(puzzleData, i, 3) > prev:
            ascendingCount += 1
        prev = windowCume(puzzleData, i, 3)

    return ascendingCount


#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))