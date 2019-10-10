list = [5, 4, 9,18,11, 7]

def FindIndexofSmallest(list, last):
    currlist = list[0:last]
    return currlist.index((min(currlist)))

def Swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def Sort(list):
    n = len(list)
    for last in range(1, n-1):
        smallest = FindIndexofSmallest(list, last)
        Swap(list, smallest, last-1)
    return list

sortedlist = Sort(list)
print(sortedlist)