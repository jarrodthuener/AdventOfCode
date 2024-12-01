from pathlib import Path
from pprint import pprint

USE_SAMPLE_DATA = True

FILE_PATH = Path(__file__).resolve()
DATA_DAY = FILE_PATH.name.split('_')[1].split(".")[0]
DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / f"day{DATA_DAY}.txt"


with open(DATA_FILE, 'r') as file:
    input_data = file.read().split("Split From Here")
    if USE_SAMPLE_DATA:
        data = input_data[0]
    else:
        data = input_data[1]


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
starting_coor = None

data_array = to_array(data,'.')
# print(data_array)

def find_neighbors(origin_coor):
    '''Returns set of neighboring coordinates [top, bottom, left, right]'''
    set_diffs = [(-1,0), (1,0), (0,-1), (0,1)]
    row_num = origin_coor[0]
    col_num = origin_coor[1]
    return [(item[0] + origin_coor[0], item[1] + origin_coor[1]) for item in set_diffs]

def find_character(coordinates, matrix):
    return matrix[coordinates[0]][coordinates[1]]

def check_valid_step(origin_coor=(), dest_coor=(), dest_char=None):
    pass

# find the starting coordinates
for row_idx, row in enumerate(data_array):
    for col_idx, cell in enumerate(row):
        if cell == 'S':
            starting_coor = (row_idx, col_idx)


next_moves = find_neighbors(starting_coor)



# while next_moves:
#     new_moves = []
#     for move in range(len(next_moves)):
#         char = find_character(next_moves[move],data_array)
#         if move = 0 and char in ('|', '7', 'F'):
#             # update new moves to new coordinates
#
#             # add to steps
#         if move = 1 and char in ('|', 'L', 'J'):





# hold moves in list of
# Pull next moves
# test to see if they are valid and update matrix only update values if valid
# increase step counter
# move to next steps




row, col = starting_coor
# print(find_neighbors(starting_coor))
# print(data_array[row][col])

# pprint(data_array)
# pretty_print(data_array)