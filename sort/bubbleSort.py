data = [24, 25, 30, 46, 87, 44, 82, 21, 95, 52, 45, 73, 71, 26, 92, 97, 41, 80, 9, 98]

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def bubbleSort(data):
    for i in range(len(data)):

        for a in range(len(data)-i-1):
            if a > len(data):
                continue
            else:
                if data[a] > data[a+1]:
                    data = swapPositions(data, a, a+1)

    return data


print(bubbleSort(data))