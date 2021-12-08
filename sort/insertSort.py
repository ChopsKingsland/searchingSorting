data = [24, 25, 30, 46, 87, 44, 82, 21, 95,
        52, 45, 73, 71, 26, 92, 97, 41, 80, 9, 98]


def insertSort(data):
    for i in range(1,len(data)):
        value = data[i]
        pos = i

        while pos > 0 and data[pos-1] > value:
            data[pos] = data[pos-1]
            pos -= 1

        data[pos] = value

    return data


print(insertSort(data))
