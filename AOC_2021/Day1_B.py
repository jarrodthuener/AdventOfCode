# import numpy as np

def get_data(day=1):
    """
    Returns test and real data in list format.
    Raw data should be maintained as:
        [test data]
        Split From Here
        [actual data]
    """
    file_name = f"data/day{day}.txt"

    with open(file_name) as fp:
        data = fp.read().strip().split("Split From Here")
        data = [d.strip().split("\n") for d in data]
        return data
get_data()

data,data1 = get_data()

puzzleData = data1.copy()



print(puzzleData)
dataLength = len(puzzleData)
# print(dataLength)

ascendingCount = 0

def windowCume(data,start,lag):
    cume = 0
    for i in range(lag):
        cume = cume + int(data[start-i])
    return cume
print(windowCume(puzzleData,2,3))


prev = windowCume(puzzleData,2,3)

for i in range(3,dataLength):
    if windowCume(puzzleData,i,3) > prev :
        ascendingCount += 1
    prev = windowCume(puzzleData,i,3)

print(ascendingCount)