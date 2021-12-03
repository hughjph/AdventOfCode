file = open("2021\Day3\data.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    

file.close()

data = {
    0: [0,0],
    1: [0,0],
    2: [0,0],
    3: [0,0],
    4: [0,0],
    5: [0,0],
    6: [0,0],
    7: [0,0],
    8: [0,0],
    9: [0,0],
    10: [0,0],
    11: [0,0],
    12: [0,0]
}



for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "0":
            data[j][0] += 1
        elif lines[i][j] == "1":
            data[j][1] += 1

gBin = ""
eBin = ""

g = 0
e = 0

for i in range(len(data)):
    if data[i][0] > data[i][1]:
        gBin += "0"
        eBin += "1"
    elif data[i][0] < data[i][1]:
        gBin += "1"
        eBin += "0"

g = int(gBin, 2)
e = int(eBin, 2)


print (g*e)
