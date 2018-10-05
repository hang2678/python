# bank.py
def authentiction(func):
    def wrapper():
        print('인증 되었습니다. ', end='')
        job = ''
        if func.__name__ == 'deposit':
            job = '입금'
        else:
            job = '출금'
        return str(func()) + '원 ' + job + '처리 되었습니다.'
    return wrapper

@authentiction
def deposit():
    return '1000'

@authentiction
def withdraw():
    return '500'

print(deposit())
print(withdraw())
