from pathlib import Path
import re
from pydoc import replace
from re import findall

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
lines = data.splitlines().copy()
# print(lines)

part1_answer = sum([int(re.findall('\d',line)[0]+re.findall('\d',line)[-1])  for line in lines])

print(f'The answer for part 1 is: {part1_answer}')

part_2_example =['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2','zoneight234','7pqrstsixteen']
# part 2

part2_lines = data.splitlines().copy()
# part2_lines = part_2_example
# print(part2_lines)

# TODO: this still produces the wrong number for some reason - off by 2

# for line in part2_lines:
replacement_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# extract string representations of numbers and numbers
extracted_list = [re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line) for line in part2_lines]

for line in extracted_list:
    print(line, ' ---- ', line[0]+line[-1])
# replace numeric words for numbers
extracted_list = [''.join([replacement_mapping.get(item, item) for item in line]) for line in extracted_list ]

# pull first and last numbers from string and summarize list
part2_answer = sum([int(re.findall('\d',line)[0]+re.findall('\d',line)[-1])  for line in extracted_list])


print(f'The answer for part 2 is: {part2_answer}')
