import sys

def get_data(day):
    """
    Returns test and real data in list format.
    Raw data should be maintained as:
        [test data]
        Split From Here
        [actual data]
    """
    file_name = f"../data/day{day}.txt"

    with open(file_name) as fp:
        data = fp.read().strip().split("Split From Here")
        data = [d.strip().split("\n") for d in data]
        return data

