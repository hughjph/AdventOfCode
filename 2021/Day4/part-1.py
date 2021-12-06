file = open("2021\Day4\data.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    

file.close()

print(lines[0])

lines = lines.pop(0)

data = [

]

x = 2
while x < 601:
    sheet = {

    }
    for i in range(5):
        row = lines[i+x].split(" ")
        sheet.update({"row" + i : "row"})
    data.append(sheet)
