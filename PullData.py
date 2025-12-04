from pathlib import Path
from datetime import date
from aocd import get_data
from aocd.models import Puzzle

from dotenv import load_dotenv
load_dotenv(override=True)

import os
os.environ["AOC_SESSION"] = os.getenv('AOC_SESSION')

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
        puzzle = Puzzle(year, day)
        print(puzzle.prose0_path)

        # --- NEW EXAMPLE HANDLING ---
        examples = puzzle.examples   # list of Example objects
        if examples:
            # join all example inputs, separated by a blank line
            example_text = "\n\n".join(
                eg.input_data.strip() for eg in examples if eg.input_data
            )
        else:
            example_text = ""

        full_data = puzzle.input_data

        # Format output: examples first, then split, then full input
        formatted_data = f"{example_text}\nSplit From Here\n{full_data}"

        # Save to disk
        file_path = get_data_path(year, day)
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
