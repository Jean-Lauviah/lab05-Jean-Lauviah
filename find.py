# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.
# What do i have to do within this section of the code.

import argparse


def main():
    parser = argparse.ArgumentParser( description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args()

    with open(args.filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            clean_line = line.rstrip("\n")

            # Check for a match depending on whether -i is set
            if args.ignore_case:
                match = args.pattern.lower() in clean_line.lower()
            else:
                match = args.pattern in clean_line

            # Print using the original clean_line if it matches
            if match:
                print(f"{line_num}: {clean_line}")

if __name__ == "__main__":
    main()
