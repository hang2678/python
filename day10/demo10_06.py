# demo10_06.py
def inner():
    print('결과입니다.')

def outer(func):
    def wrapper():
        print('-' * 15)
        func()
        print('-' * 15)

    return wrapper

my_inner = outer(inner)
my_inner()