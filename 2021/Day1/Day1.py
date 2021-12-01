file = open("Day1\Day1Data.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    lines[i] = int(lines[i])
    
print(lines)

number_increased = 0

#Part 1

for i in range(2, len(lines)):
    if lines[i]>lines[i-1]:
        number_increased += 1
    



print("Part 1")
print(number_increased)

#Part 2
number_increased = 0
previous_sum = 0

for i in range(2, len(lines)):
    if (lines[i]+lines[i-1]+lines[i-2])>previous_sum:
        number_increased += 1
    previous_sum = lines[i]+lines[i-1]+lines[i-2]

print("Part 2")
print(number_increased-1)
