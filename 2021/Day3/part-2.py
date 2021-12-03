file = open("2021\Day3\data.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    
file.close()

lineArray = lines.copy()

def getmost(data):
    oxygenGenRating = ""
    for j in range(12):
        zeros = 0
        ones = 0
        for i in range(len(data)):
            if data[i][j] == "0":
                zeros+=1
            elif data[i][j] == "1":
                ones+=1
        
        mostcommon = ("0", "1")[zeros > ones]
        
        removeindex = []

        if len(data) == 1:
            break

        for i in range(len(data)):
            if data[i][j] != mostcommon:
                
                removeindex.append(i)
        
        
        removeindex = removeindex[::-1]

        for i in range(len(removeindex)):
            data.pop(removeindex[i])


    oxygenGenRating = data[0]
    return oxygenGenRating

def getleast(data):
    
    co2ScrubberRating = ""

    for j in range(12):
        zeros = 0
        ones = 0
        for i in range(len(data)):
            if data[i][j] == "0":
                zeros+=1
            elif data[i][j] == "1":
                ones+=1
        
        leastcommon = ("0", "1")[zeros <= ones]
       
        removeindex = []

        if(len(data)==1):
            break

        for i in range(len(data)):
            if data[i][j] != leastcommon:
                removeindex.append(i)
        
        if(len(removeindex) == len(data)):
            break
        removeindex = removeindex[::-1]

        for i in range(len(removeindex)):
            data.pop(removeindex[i])

    co2ScrubberRating = data[0]
    return co2ScrubberRating




newScrub = int(getmost(lines), 2)
print(newScrub)

newOxygen = int(getleast(lineArray), 2)

print(newOxygen)

print(newOxygen * newScrub)
