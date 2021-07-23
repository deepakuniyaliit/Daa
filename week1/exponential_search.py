comparisions = 0

def readFile():
    global comparisions
    n = int(input())

    for i in range(n):
        size = int(input())
        array = input()
        array = array.split()
        array = [int(element) for element in array]
        key = int(input())
        
        if(exponentialSearch(array,size, key))>0:
            print('Present', comparisions)
            comparisions = 0
        else:
            print('Not Present', comparisions)
            comparisions = 0

def linearSearch(array, index, n, key):
    global comparisions
    for i in range(index, n):
        if (array[i] == key):
            comparisions = comparisions + 1
            return i
        comparisions = comparisions + 1
    return -1


def binarySearch (array, left, right, key):
    global comparisions
    if right >= left:
        mid = left + (right - left) // 2
        if array[mid] == key:
            comparisions = comparisions + 1
            return mid
        elif array[mid] > key:
            comparisions = comparisions + 1
            return binarySearch(array, left, mid-1, key)
        else:
            comparisions = comparisions + 1
            return binarySearch(array, mid + 1, right, key)
    else:
        return - 1


def exponentialSearch(array, n, key):
    global comparisions
    if array[0] == key:
        comparisions = comparisions + 1
        return 0
    else:
        comparisions = comparisions + 1
    i = 1
    while i < n and array[i] <= key:
        comparisions = comparisions + 1
        i = i * 2
    return linearSearch (array, int(i/2), n, key)
    #return binarySearch(array, int(i/2), min(i, n-1), key)


if __name__ == '__main__':
    readFile()