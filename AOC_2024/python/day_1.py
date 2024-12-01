from pathlib import Path
import re

USE_SAMPLE_DATA = False

FILE_PATH = Path(__file__).resolve()
DATA_DAY = FILE_PATH.name.split('_')[1].split(".")[0]
DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / f"day{DATA_DAY}.txt"


with open(DATA_FILE, 'r') as file:
    input_data = file.read().split("Split From Here")
    if USE_SAMPLE_DATA:
        data = input_data[0].strip()
    else:
        data = input_data[1].strip()


def to_array(textblock, delimiter=None):
    parsed_data = textblock.split('\n')
    if delimiter in (',',' '):
        parsed_data = [row.split(delimiter) for row in parsed_data]
    elif delimiter == '.':
        parsed_data = [list(row) for row in parsed_data]
    return parsed_data

def pretty_print(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# ----------Write Code Below------------------------------------------------------------------------------------------
lines = data.splitlines()

# split into two lists
list_1, list_2 = zip(*(map(int, re.split(r'\s+',line)) for line in lines))

# turn the tuples into lists
list_1, list_2 = list(list_1), list(list_2)

# sort both lists
list_1.sort()
list_2.sort()

# Part 1
total_diff = 0
for i in range(len(list_1)):
    total_diff += abs(list_1[i] - list_2[i])

print(f'The answer for part 1 is: {total_diff}')

# part 2
total_sum = 0
for i in list_1:
    # find counts in right list to multiply
    total_sum += i * list_2.count(i)

print(f'The answer for part 2 is: {total_sum}')
