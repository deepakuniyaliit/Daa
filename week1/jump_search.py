import math
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
        
        if(jumpSearch(array, size, key))>0:
            print('Present', comparisions)
            comparisions = 0
        else:
            print('Not Present', comparisions)
            comparisions = 0


def jumpSearch( array, n, key):
    global comparisions
    jump = math.sqrt(n)
    steps = jump
    prev = 0
    while array[int(min(steps, n)-1)] < key:
        comparisions = comparisions + 1
        prev = steps
        steps += jump
        if prev >= n:
            return -1
    #comparisions = comparisions + 1
    while array[int(prev)] < key:
        comparisions = comparisions + 1
        prev += 1
        if prev == min(steps, n):
            return -1
        # else:
        #     comparisions = comparisions + 1
    #comparisions = comparisions + 1
    if array[int(prev)] == key:
        comparisions = comparisions + 1
        return prev
    # else:
    #     comparisions = comparisions + 1
    return -1


if __name__ == '__main__':
    readFile()