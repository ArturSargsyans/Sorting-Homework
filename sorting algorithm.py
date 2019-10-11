list = [10, 8, 9, 7, 23, 1]

def FindIndexofLargest(list, last):
    currlist = list[0:last]
    return currlist.index((max(currlist)))

def Swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def Sort(list):
    n = len(list)
    for last in range(n-1, 1, -1):
        largest = FindIndexofLargest(list, last)
        Swap(list, largest, last)
    return list

sortedlist = Sort(list)
print(sortedlist)
