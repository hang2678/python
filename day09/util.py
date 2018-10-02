# util.py
INCH = 2.54

def calcsum(n):
    sum = 0
    for i in range(n + 1): # n=10
        sum += i
    return sum

if __name__ == '__main__':
    print('__name__(util)=' + __name__)
    print('인치=', INCH)
    print('합계=', calcsum(10))
        