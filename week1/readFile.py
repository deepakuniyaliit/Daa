def readFile():
    n = int(input())
    print('No. of test cases',n)
    for i in range(n):
        size = int(input())
        array = input()
        array = array.split()
        array = [int(element) for element in array]
        key = input()
        print('size', size)
        print('elements', array)
        print('key', key)


if __name__ == '__main__':
    readFile()