import random

Start = 9
Stop = 99
limit = 20

RandomListOfIntegers = [random.randint(Start, Stop) for iter in range(limit)]

print(RandomListOfIntegers)