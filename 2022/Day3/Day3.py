import sys
import argparse
import string


def read_data(args):
    first = []
    second = []
    values = []

    for line in args.datafile:
        value = line.splitlines()

        value = value[0]
        values.append(value)
        section1 = value[:len(value)//2]
        section2 = value[len(value)//2:]

        first.append(section1)
        second.append(section2)

    return first, second, values

def calculate_badges(values):

    badges = []

    set_of_three = []

    for i in range(len(values)):
        print(set_of_three)
        if len(set_of_three) == 3:
            longest = max(set_of_three, key=len)
            for j in range(len(longest)):

                if len(set_of_three) == 3 and longest[j] in set_of_three[0] and longest[j] in set_of_three[1] and longest[j] in set_of_three[2]:
                    badges.append(longest[j])
                    break
            set_of_three = [values[i]]
        else:
            set_of_three.append(values[i])

    longest = max(set_of_three, key=len)
    for j in range(len(longest)):

        if len(set_of_three) == 3 and longest[j] in set_of_three[0] and longest[j] in set_of_three[1] and longest[j] in \
                set_of_three[2]:
            badges.append(longest[j])
            break

    print(len(badges))
    return badges



def calculate_duplicates(first, second):

    duplicates = []

    for i in range(len(first)):
        for j in range(len(first[i])):
            if first[i][j] in second[i]:
                duplicates.append(first[i][j])
                break

    return duplicates

def calculate_values(duplicates, scores):
    score = 0

    for char in duplicates:
        value = scores.index(char)
        value += 1
        score += value

    return score


parser = argparse.ArgumentParser(description="Calculating the amount of elf fuck ups")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Text file of rucksack info")

if __name__ == "__main__":
    args = parser.parse_args()
    first, second, values = read_data(args)
    duplicates = calculate_duplicates(first, second)

    scores = list(string.ascii_letters)
    score = calculate_values(duplicates, scores)

    print(f"Score: {score}")

    badges = calculate_badges(values)

    badge_score = calculate_values(badges, scores)
    print(f"Badge Score: {badge_score}")



