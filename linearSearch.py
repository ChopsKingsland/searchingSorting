data = [3,232,99,6,9276,1,0]

toFind = int(input("Value to find: "))

isFound = False
i = 0
index = 0

for i in range(len(data)):
    if isFound:
        continue
    else:
        if data[i] == toFind:
            isFound = True
            index = i

if isFound:
    print(f"{toFind} was found at index {index}")
else:
    print(f"{toFind} was not found")