from pathlib import Path

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


# ----------Write Code Below------------------------------------------------------------------------------------------

data_array = to_array(data,' ')
print(data_array)
def check_list_all_zeros(list):
    pass


def find_forward_number(data):
    new_array = [data]
    result_array = []
    for pos in range(len(data)):
        if pos != 0:
            result_array.append(int(data[pos]) - int(data[pos-1]))

    if check_list_all_zeros(result_array):
        pass



find_forward_number(data_array[0])