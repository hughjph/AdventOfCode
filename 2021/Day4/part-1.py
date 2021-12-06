file = open("2021\Day4\data.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    

file.close()

print(lines[0])

numbers = lines[0].split(",")

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
    x+=6

print(data[10])

for i in range(len(numbers)):
    number = numbers[i]
    for j in range(len(data)):
        for k in range(5):
            

