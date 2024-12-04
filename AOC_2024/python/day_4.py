import time
from pathlib import Path
import re

import numpy as np
from click import pause

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
# print(data)
data = [re.findall('.',line)  for line in data.splitlines()]
data = np.array(data)





# print(data[(0,1),(1,1)], data)

def check_xmas(coordinates=(), data=None, direction='right'):
    xmas_count = 0
    coords_lookup = {'right':[(0, 0), (0, 1), (0, 2), (0, 3)],
              'down-right':[(0, 0), (1, 1), (2, 2), (3, 3)],
              'down':[(0, 0), (1, 0), (2, 0), (3, 0)],
                     'up-right':[(0,0),(-1,1),(-2,2),(-3,3)]}
    coords = coords_lookup[direction]

    set_of_coords = []
    for (y,x) in coords:
        # print(coordinates)
        if coordinates[0]+y <= data.shape[0]-1 and  coordinates[1]+x <= data.shape[1]-1:
            set_of_coords.append((coordinates[0]+y,coordinates[1]+x))

    # coordinates_to_check = [[(coordinates[0]+y,coordinates[1]+x) for (y,x) in line] for line in coords]
    text = ''.join([str(data[(coor)]) for coor in set_of_coords])
    # print(text)
    # time.sleep(2)
    if text in ('XMAS','SAMX'):
        xmas_count += 1
    # print('newLine To check')
    return(xmas_count)

total_xmas_count = 0
# print(data.shape)
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        total_xmas_count += check_xmas((row,col), data,'right')
        total_xmas_count += check_xmas((row, col), data, 'down-right')
        total_xmas_count += check_xmas((row, col), data, 'down')
        total_xmas_count += check_xmas((row, col), data, 'up-right')
# print(total_xmas_count)
# print(check_xmas((3,4),data))


# x_coor = np.where(data == 'X')
# print(data.diagonal(0))


part_1_answer = total_xmas_count
print(f'The answer for part 1 is: {part_1_answer}')



# part 2

# part_2_answer = safe_count
#
# print(f'The answer for part 2 is: {part_2_answer}')
