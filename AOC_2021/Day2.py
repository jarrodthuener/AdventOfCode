from get_data import get_data

# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData, fullData = get_data(2)


# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer

def part1solution(puzzleData):
    horizontalPos = 0
    depth = 0
    dataLength = len(puzzleData)
    ascendingCount = 0



    for i in range(dataLength):
        direction = puzzleData[i].split(" ")[0]
        quantity = int(puzzleData[i].split(" ")[1])
        if direction == "forward":
            horizontalPos += quantity
            # print("horizontal position = "+str(horizontalPos))
            # print("depth = "+str(depth))
        elif direction == "down":
            depth += quantity
        elif direction == "up":
            depth -= quantity

    return str(horizontalPos) +" X "+ str(depth) +" = "+str(depth*horizontalPos)
    # print(str(horizontalPos) +" X "+ str(depth) +" = "+str(depth*horizontalPos))

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
    horizontalPos = 0
    depth = 0
    aim = 0

    """
    for each row starting with the fourth row check the sum of the previous 3 values 
    against the trailing 3 rows starting with the previous row to see if it is ascending
    skip first 3 rows since there isn't a previous trailing value to compare
    return the ascendingCount as the answer
    """
    for i in range(dataLength):
        direction = puzzleData[i].split(" ")[0]
        quantity = int(puzzleData[i].split(" ")[1])
        if direction == "forward":
            horizontalPos += quantity
            depth += aim * quantity
            # print("horizontal position = " + str(horizontalPos))
            # print("depth = " + str(depth))
        elif direction == "down":
            aim += quantity
        elif direction == "up":
            aim -= quantity

    return str(horizontalPos) + " X " + str(depth) + " = " + str(depth * horizontalPos)

#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))