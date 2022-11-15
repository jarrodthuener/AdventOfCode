# import numpy as np

def get_data(day=2):
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


horizontalPos = 0
depth = 0
aim = 0

print(puzzleData)
dataLength = len(puzzleData)
# print(dataLength)

for i in range(dataLength):
    direction = puzzleData[i].split(" ")[0]
    quantity = int(puzzleData[i].split(" ")[1])
    if direction == "forward":
        horizontalPos += quantity
        depth += aim * quantity
        print("horizontal position = "+str(horizontalPos))
        print("depth = "+str(depth))
    elif direction == "down":
        aim += quantity
    elif direction == "up":
        aim -= quantity

print(str(horizontalPos) +" X "+ str(depth) +" = "+str(depth*horizontalPos))

