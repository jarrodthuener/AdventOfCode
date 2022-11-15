import numpy as np

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


# for i in range(dataLength):
#     print(data[i])

shiftedData = np.numarray(data1.cumsum())
shiftedData[3:] = shiftedData[3:] - shiftedData[:3]

print(shiftedData)
puzzleData = data1.copy()


exit


print(puzzleData)
dataLength = len(puzzleData)
print(dataLength)
prev = puzzleData[0]
ascendingCount = 0

for i in range(1,dataLength):
    if int(puzzleData[i]) > int(prev):
        print(puzzleData[i] + " is ascending from " + prev)
        ascendingCount += 1
    else:
        print(puzzleData[i] + " is descending from " + prev)
    prev = puzzleData[i]

print(ascendingCount)