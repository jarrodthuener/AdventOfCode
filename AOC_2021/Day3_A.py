# import numpy as np
from get_data import get_data

# def get_data(day=3):
#     """
#     Returns test and real data in list format.
#     Raw data should be maintained as:
#         [test data]
#         Split From Here
#         [actual data]
#     """
#     file_name = f"data/day{day}.txt"
#
#     with open(file_name) as fp:
#         data = fp.read().strip().split("Split From Here")
#         data = [d.strip().split("\n") for d in data]
#         return data
# get_data()

data,data1 = get_data(3)

puzzleData = data.copy()


print(puzzleData)
dataLength = len(puzzleData)
# print(dataLength)

totalSum = 0

for r in range(dataLength):
    totalSum += int(puzzleData[r])




print(totalSum)
totalSumString = list(str(totalSum))

for l in range(len(puzzleData[0])):
    if int(totalSumString[l]) > dataLength/2:
        totalSumString[l] = '1'
    else:
        totalSumString[l] = '0'

print(int(''.join(str(i) for i in totalSumString),2))




# N = len(puzzleData[0])
#
# gamma = 0
# epsilon = 0
#
# for n in range(N):
#     count1 = sum(1 for line in puzzleData if line[n] == '1')
#     count0 = len(puzzleData) - count1
#     gamma *= 2
#     epsilon *= 2
#     if count0 < count1:
#         gamma += 1
#     else:
#         epsilon += 1
#
# print(gamma * epsilon)


#
# def mostCommonDigits(array):
#     rows = len(array)
#     length = len(array[0])
#     print(rows)
#     print(length)
#     digits = ['0'*length]
#     print(digits)
#     for r in range(rows):
#         for l in range(length):
#             print(array[r][l])
#             digits[l] = str(int(digits[l]) + int(array[l]))
#             print(digits)
#
# print(mostCommonDigits(puzzleData))

# for i in range(dataLength):
#     print(puzzleData[i])
#     for r in range(len(puzzleData[i])):
#         print(puzzleData[i][r])


#     if direction == "forward":
#         horizontalPos += quantity
#         depth += aim * quantity
#         print("horizontal position = "+str(horizontalPos))
#         print("depth = "+str(depth))
#     elif direction == "down":
#         aim += quantity
#     elif direction == "up":
#         aim -= quantity
#
# print(str(horizontalPos) +" X "+ str(depth) +" = "+str(depth*horizontalPos))

