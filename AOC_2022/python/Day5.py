from get_data import get_data
import pandas as pd
# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(5)

# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer

# file_name = f"../data/day5.txt"
#
# with open(file_name, 'r') as fp:
#     sampleData,fullData = fp.read().split("Split From Here")
#     stack_txt, instruction_data = sampleData.split("\n\n")
#     # print(type(stack_txt))
#     stack_txt = stack_txt.split("\n")
#     instruction_data
#     print(stack_txt)



def part1solution(puzzleData):
    """
    Objective:

    Steps to be taken to solve the problem:

    """
    puzzleData = '\n'.join(puzzleData)
    stack_txt, instruction_data = puzzleData.split('\n\n')
    stack_txt = stack_txt.split('\n')
    instruction_data = instruction_data.split('\n')


    stack_last = stack_txt.pop()
    print(stack_last)

    # print(stack_txt)
    # print(puzzleData)
    # df = pd.DataFrame(puzzleData)
    # print(df)



#Run the sampleData
print("Part 1 sample data answer: "+ str(part1solution(sampleData)))

#Run the fullData
print("Part 1 full data answer: "+ str(part1solution(fullData)))


def part2solution(puzzleData):
    """
    Objective:

    Steps to be taken to solve the problem:

    """




#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))