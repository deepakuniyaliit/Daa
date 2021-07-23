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

        if(linearSearch(array,size, key))>0:
            print('Present', comparisions)
            comparisions = 0
        else:
            print('Not Present', comparisions)
            comparisions = 0

def linearSearch(array, size, key):
    global comparisions
    for i in range(0, size):
        if (array[i] == key):
            comparisions = comparisions + 1
            return i
        comparisions = comparisions + 1
    return -1

if __name__ == '__main__':
    readFile()