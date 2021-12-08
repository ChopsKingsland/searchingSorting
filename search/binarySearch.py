import time
from timeit import default_timer as timer

start = timer()
data = [24, 25, 30, 46, 87, 44, 82, 21, 95, 52, 45, 73, 71, 26, 92, 97, 41, 80, 9, 98]
sortedData = data

#toFind = int(input("Value to find: "))

toFind = 97

found = False
index = 0

low = 0
high = len(sortedData) - 1
mid = 0

while low <= high:
    mid = round((high + low)/2)
   #if is middle item
    if sortedData[mid] == toFind:
        found = True
        index = mid
        high = low - 1
    elif sortedData[mid] < toFind:
        low = mid + 1
    else:
        high = mid + 1

end = timer()
time = end-start

if found:
    print(f"{toFind} has been found at index {index} in {time} seconds")
else:
    primt(f"{toFind} is not in the list")