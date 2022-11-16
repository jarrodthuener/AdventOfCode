from get_data import get_data

# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(3)

# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer

def part1solution(puzzleData):
    """
    Objective: for each character position, find whether 0 or 1 is more common and piece together a single string to convert to an integer.

    Steps to be taken to solve the problem: build gamma and epsilon values then convert to integer
    for each character position, cycle through all of the rows and keep track of
    """
    # set variables to be used
    # we are going to build each number one character at a time.
    gamma = ''
    epsilon = ''

    for i in range(len(puzzleData[0])):
        cnt0 = 0
        cnt1 = 0
        for row in puzzleData:
            if row[i] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
        if cnt1 > cnt0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma,2) * int(epsilon,2)

#Run the sampleData
print("Part 1 sample data answer: "+ str(part1solution(sampleData)))

#Run the fullData
print("Part 1 full data answer: "+ str(part1solution(fullData)))


def part2solution(puzzleData):
    """
    Objective:

    Steps to be taken to solve the problem:

    """
    # Find oxygen generator rating:
    oxyRating = puzzleData.copy()
    for i in range(len(oxyRating[0])):
        if len(oxyRating) > 1:
            cnt0 = 0
            cnt1 = 0
            for row in oxyRating:
                if row[i] == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
            print("done with rows")
            # now go back and delete the entries that have the least amount of
            if cnt0 > cnt1:
                most = '0'
            else:
                most = '1'
            print("count 0 = "+str(cnt0)+ ", count 1 = "+str(cnt1)+ " most = "+str(most))

            # only keep rows that aren't
            print('items to be removed: '+str([row for row in oxyRating if row[i] != most]) )
            oxyRating = [row for row in oxyRating if row[i] == most]
            print("New list: "+str(oxyRating))

    print('----- end of oxygen rating -----')

    # Find CO2 generator rating:
    co2Rating = puzzleData.copy()
    for i in range(len(co2Rating[0])):
        if len(co2Rating) > 1:
            cnt0 = 0
            cnt1 = 0
            for row in co2Rating:
                if row[i] == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
            print("done with rows")
            # now go back and delete the entries that have the least amount of
            if cnt0 > cnt1:
                most = '0'
            else:
                most = '1'
            print("count 0 = " + str(cnt0) + ", count 1 = " + str(cnt1) + " most = " + str(most))

            # only keep rows that aren't the most common
            print('items to be removed: ' + str([row for row in co2Rating if row[i] == most]))
            co2Rating = [row for row in co2Rating if row[i] != most]
            print("New list: " + str(co2Rating))
    print('----- end of oxygen rating -----')

    return int(oxyRating[0],2)*int(co2Rating[0],2)


#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))


