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

        if(binarySearch(array,0, size-1, key))>0:
            print('Present', comparisions)
            comparisions = 0
        else:
            print('Not Present', comparisions)
            comparisions = 0


def binarySearch (array, left, right, key):
    global comparisions
    if left <= right:
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
        return -1


if __name__ == '__main__':
    readFile()