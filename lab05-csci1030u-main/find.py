# Part 1 - a small "find" tool (like a simplified `grep`).
# 
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.




import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")
    parser.add_argument("-i", "--ignore-case", action="store_true" , 
                        help="ingore case distirnction")

    args = parser.parse_args()
    search_pattern = args.pattern.lower() if args.ignore_case else args.pattern
    
    with open(args.filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            line_clean = line.rstrip("\n") # returns a string of the line
            
            search_line = line_clean.lower() if args.ignore_case else line_clean
            
            if search_pattern in search_line:
                print(f"{line_num}: {line_clean}")


if __name__ == "__main__":
    main()
