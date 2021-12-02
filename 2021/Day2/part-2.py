file = open("2021\Day2\data.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    

file.close()

x = 0
y = 0
a = 0

for i in range(len(lines)):

    number = int(lines[i][len(lines[i]) - 1])

    if lines[i].startswith("forward"):
        x += number
        y += number*a
    elif lines[i].startswith("up"):
        a -= number
    elif lines[i].startswith("down"):
        a += number

print (x*y)
