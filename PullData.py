from pathlib import Path
from datetime import date
from aocd.models import Puzzle

# Configuration
BASE_DIR = Path(__file__).resolve().parent
START_YEAR = 2015
CURRENT_YEAR = date.today().year
CURRENT_DAY = date.today().day if date.today().month == 12 else -1  # December days only


def get_data_path(year, day):
    return BASE_DIR / f"AOC_{year}" / "data" / f"day{day:1}.txt"

def ensure_directories(year):
    year_dir = BASE_DIR / f"AOC_{year}"
    data_dir = year_dir / "data"
    year_dir.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)
    return data_dir

def fetch_and_save_data(year, day):
    try:
        # # Fetch data from AOC
        puzzle = Puzzle(year, day)
        example_data = puzzle.example_data
        full_data = puzzle.input_data

        # format data with example data on top and full data below
        formatted_data = f"{example_data}\nSplit From Here\n{full_data}"

        # Save the file
        file_path = get_data_path(year, day)

        # output file
        with open(file_path, "w") as file:
            file.write(formatted_data)

        print(f"Data saved for Year {year}, Day {day}")
    except Exception as e:
        print(f"Failed to fetch data for Year {year}, Day {day}: {e}")

def main():
    for year in range(START_YEAR, CURRENT_YEAR + 1):
        ensure_directories(year)
        pass
        for day in range(1, 26):  # AOC runs from Day 1 to Day 25
            if year == CURRENT_YEAR and day > CURRENT_DAY:
                break  # Skip future days in the current year
            file_path = get_data_path(year, day)
            if not file_path.exists():
                print(f"Missing data for Year {year}, Day {day}. Fetching...")
                fetch_and_save_data(year, day)

if __name__ == "__main__":
    main()
