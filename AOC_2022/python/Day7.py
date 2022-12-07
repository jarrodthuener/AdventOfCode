from get_data import get_data
from collections import Counter
import itertools
# split the data.txt file into sampleData and fullData sets (split by "Split From Here")
sampleData,fullData = get_data(7)

# ----below is the rest of the code to solve for the day's problem.----
# the two functions part1solution() and part2solution() will be called at the end for each set of data to retrieve the answer

def day7(s, part2=False):
  stack, sizes = [], []
  for line in s:
    if line == '$ cd ..':
      size = stack.pop()
      sizes.append(size)
      stack[-1] += size
    elif line.startswith('$ cd '):
      stack.append(0)
    elif line[0].isdigit():
      stack[-1] += int(line.split()[0])
  sizes.extend(itertools.accumulate(stack[::-1]))
  return (sum(s for s in sizes if s <= 100_000) if not part2 else
          min(s for s in sizes if s >= max(sizes) - 40_000_000))

# print(sampleData)
print(day7(fullData))


def part1solution(puzzleData):
    """
    Objective:

    Steps to be taken to solve the problem:

    """
    buffer = puzzleData[0]
    distinctChars = 4
    negOffset = distinctChars-1

    for i in range(negOffset,len(buffer)):
        if len(Counter(buffer[i-negOffset:i+1]).keys()) == distinctChars:
            return i+1



#Run the sampleData
print("Part 1 sample data answer: "+ str(part1solution(sampleData)))

#Run the fullData
print("Part 1 full data answer: "+ str(part1solution(fullData)))


def part2solution(puzzleData):
    """
    Objective:

    Steps to be taken to solve the problem:

    """
    buffer = puzzleData[0]
    distinctChars = 14
    negOffset = distinctChars-1

    for i in range(negOffset,len(buffer)):
        if len(Counter(buffer[i-negOffset:i+1]).keys()) == distinctChars:
            return i+1


#Run the sampleData
print("Part 2 sample data answer: "+ str(part2solution(sampleData)))

#Run the fullData
print("Part 2 full data answer: "+ str(part2solution(fullData)))