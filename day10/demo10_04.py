# demo10_04.py
# def add(a, b):
#     print(a + b)

# plus = add
# plus(10, 20)


def calc(op, a, b):
    op(a, b)

def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

calc(add, 10, 20)
calc(subtract, 20, 5)