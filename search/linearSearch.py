from timeit import default_timer as timer

start = timer()

data = [24, 25, 30, 46, 87, 44, 82, 21, 95, 52, 45, 73, 71, 26, 92, 97, 41, 80, 9, 98]

#toFind = int(input("Value to find: "))

toFind = 97

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

end = timer()
time = end-start

if isFound:
    print(f"{toFind} was found at index {index} in {time} seconds")
else:
    print(f"{toFind} was not found")