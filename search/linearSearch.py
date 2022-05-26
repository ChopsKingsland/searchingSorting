from timeit import default_timer as timer

start = timer()

data = [24, 25, 30, 46, 87, 44, 82, 21, 95, 52, 45, 73, 71, 26, 92, 97, 41, 80, 9, 98]


toFind = 97


def linearSearch(data, toFind):
    for i in range(len(data)):
        if data[i] == toFind:
            return i
    return False

isFound = linearSearch(data, toFind)

end = timer()
time = end-start

if isFound != False:
    print(f"{toFind} was found at index {isFound} in {time} seconds")
else:
    print(f"{toFind} was not found")