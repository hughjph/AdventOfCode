import argparse
import sys


def read_data(args):
    choices = []
    opponents = []

    for line in args.datafile:
        opponent, choice = line.split(" ")
        choice = choice[0]
        opponent = opponent[0]

        choices.append(choice)
        opponents.append(opponent)

    return opponents, choices


def calculate_score(opponents, choices):
    running_score = 0

    for i in range(len(opponents)):
        score = 0
        opponent = opponents[i]
        choice = choices[i]

        if choice == 'X':  # Rock
            score += 1
            if opponent == 'A':  # Rock
                score += 3
            elif opponent == 'C':  # Scissors
                score += 6
        elif choice == 'Y':  # Paper
            score += 2
            if opponent == 'B':  # Paper
                score += 3
            elif opponent == 'A':  # Rock
                score += 6
        elif choice == 'Z':  # Scissors
            score += 3
            if opponent == 'C':  # Scissors
                score += 3
            elif opponent == 'B':  # Paper
                score += 6


        running_score += score

    return running_score

def calculate_score_m2(opponents, choices):
    running_score = 0
    for i in range(len(opponents)):
        score = 0
        opponent = opponents[i]
        choice = choices[i]

        if choice == 'X':  # Lose

            if opponent == 'A':  # Rock
                score += 3
            elif opponent == 'B':
                score += 1
            elif opponent == 'C':  # Scissors
                score += 2
        elif choice == 'Y':  # Draw
            score += 3
            if opponent == 'A':  # Rock
                score += 1
            elif opponent == 'B':
                score += 2
            elif opponent == 'C':  # Scissors
                score += 3
        elif choice == 'Z':  # Win
            score += 6
            if opponent == 'A':  # Rock
                score += 2
            elif opponent == 'B':
                score += 3
            elif opponent == 'C':  # Scissors
                score += 1
        print(score)

        running_score += score

    return running_score
    

parser = argparse.ArgumentParser(description="Returns elf with the highest amount of calories")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Text file of calories info")

if __name__ == '__main__':
    args = parser.parse_args()
    opponents, choices = read_data(args)
    print(f"Score: {calculate_score(opponents, choices)}")
    print(f"Part 2: {calculate_score_m2(opponents, choices)}")
