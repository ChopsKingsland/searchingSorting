from binarySearch import binarySearch
from linearSearch import linearSearch
from timeit import default_timer as timer

data = [24, 25, 30, 46, 87, 44, 82, 21, 95,
        52, 45, 73, 71, 26, 92, 97, 41, 80, 9, 98]

start = timer()
binarySearch(data)
end=timer()

bina = end-start


start = timer()
binarySearch()
end=timer()

bina = end-start


