# demo10_05.py
def calcsum(n):
    def add(a, b):
        return a + b
    
    sum = 0
    for i in range(n + 1):
        sum = add(sum, i)
    return sum

print('1~10=', calcsum(10))