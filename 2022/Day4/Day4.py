import argparse
import sys


def read_data(args):
    first_set = []
    second_set = []

    for line in args.datafile:
        first, second = line.split(',')
        first_set.append(first)
        second_set.append(second.splitlines()[0])

    return first_set, second_set


def calculate_overlaps(first_set, second_set):
    overlaps = 0

    for i in range(len(first_set)):
        first_start, first_end = first_set[i].split('-')
        second_start, second_end = second_set[i].split('-')

        first_start = int(first_start)
        first_end = int(first_end)
        second_start = int(second_start)
        second_end = int(second_end)

        if (first_start <= second_start and first_end >= second_end) or (first_start >= second_start and first_end <= second_end):
            overlaps += 1

    return overlaps


def calculate_overlaps_pt2(first_set, second_set):

    overlaps = 0

    for i in range(len(first_set)):
        first_start, first_end = first_set[i].split('-')
        second_start, second_end = second_set[i].split('-')

        first_start = int(first_start)
        first_end = int(first_end)
        second_start = int(second_start)
        second_end = int(second_end)

        if (first_end >= second_start and first_start <= second_start) or (second_end >= first_start and second_start <= first_start):
            overlaps += 1


    return overlaps

parser = argparse.ArgumentParser(description="...")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Data for the challenge")

if __name__ == '__main__':
    args = parser.parse_args()
    first, second = read_data(args)
    overlaps = calculate_overlaps(first, second)
    print(f"Number of overlaps: {overlaps}")
    overlapspt2 = calculate_overlaps_pt2(first, second)
    print(f"Number of overlaps for part 2: {overlapspt2}")
