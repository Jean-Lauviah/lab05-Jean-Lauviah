# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa
#
# The argument parser is finished for you. Complete the TODO.

import argparse
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()

    # TODO: open args.filename and read it with csv.reader. The first row is the
    #   header. Find the position of args.column within the header, then print every
    #   data row (its values joined by commas) whose value in that column equals
    #   args.value.

    try:
        with open(args.filename, "r", newline="") as file:
            reader = csv.reader(file)

            # Read the header row to find the index of args.column
            header = next(reader)
            column_index = header.index(args.column)

            # Check each data row and print matches joined by commas
            for row in reader:
                if row and row[column_index] == args.value:
                    print(",".join(row))

    except FileNotFoundError:
        print(f"Error: The file '{args.filename}' was not found.")
    except ValueError:
        print(f"Error: Column '{args.column}' was not found in the CSV header.")


if __name__ == "__main__":
    main()
