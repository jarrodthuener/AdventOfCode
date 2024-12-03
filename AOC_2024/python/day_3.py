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
data = [[int(number) for number in line.split(' ')] for line in data.splitlines()]
# part 2
print(data)


part_1_answer = safe_count
print(f'The answer for part 1 is: {part_1_answer}')



# part 2
safe_count = 0
for line in data:
    if is_line_safe(line):
        safe_count += 1
    else:
        for i in range(len(line)):
            new_list = line.copy()
            new_list.pop(i)
            if is_line_safe(new_list):
                safe_count += 1
                break

part_2_answer = safe_count

print(f'The answer for part 2 is: {part_2_answer}')
