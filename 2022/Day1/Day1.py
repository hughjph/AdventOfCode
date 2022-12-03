import argparse
import sys


def read_data(args):

    calorie_data = []

    current_val = 0

    for line in args.datafile:
        if line != "\n":
            current_val += int(line.splitlines()[0])
        else:
            calorie_data.append(current_val)
            current_val = 0
    return calorie_data


def get_highest(data):
    highest = 0
    for value in data:
        if value >= highest:
            highest = value

    return highest

def get_top_three(data):
    first = 0
    second = 0
    third = 0

    for value in data:
        if value >= first:
            third = second
            second = first
            first = value
        elif value >= second:
            third = second
            second = value
        elif value >= third:
            third = value

    return f"{first}, {second}, {third}. Total: {first + second + third}"


parser = argparse.ArgumentParser(description="Returns elf with the highest amount of calories")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Text file of calories info")

if __name__ == '__main__':
    args = parser.parse_args()
    data = read_data(args)
    print(f"Part 1: {get_highest(data)}")
    print(f"Part 2: {get_top_three(data)}")
