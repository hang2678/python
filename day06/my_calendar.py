# my_calendar.py
# 1. 년도, 월 입력 받은 후 해당 달력 출력 
# 2. 일월화수목금토 순서로 출력

import datetime

def header(year, month):
    #print('\t', year, '년', month, '월')
    print('\t{0}년 {1}월'.format(year, month))
    print('-' * 30)
    print('일  월  화  수  목  금  토')
    #print('\t %s년 %s월')

def getStartPosition(year, month):
    d = datetime.date(year, month, 1)
    return d.weekday() # 월요일 -> 0

def getLastDay(year, month): # 1~12
    if month == 12:
        year = year + 1
        month = 1
    else:
        month = month + 1

    next_month = datetime.date(year, month, 1) # 2018-10-01 
    t = datetime.timedelta(days = 1)
    gap = next_month - t # (2018-10-01) - (1 day) = 2018-09-30
    
    return gap.day  # 30

def display(year, month):
    header(year, month)
    startPos = getStartPosition(year, month) # 1에 해당하는 요일이 어디인지 확인? 
    lastDay = getLastDay(year, month) # 9월 마지막날 -> 30
    # ex) 9월 -> 1일은 토요일 -> startPos = 5

    # 1~30까지 출력 + 1일 앞에 몇일의 공백이 오는지 출력
    totalDays = lastDay + (startPos + 1) # 35 
    
    d = 1
    for n in range(1, totalDays + 1): # 1 ~ 36
        if n <= ( (startPos + 1) % 7 ):
            # 1 ~ 6개 -> 공백 출력
            print('{:>2}'.format(' '), end='  ')
        else:
            # 7번째(1) ~ 마지막번째(30) -> 순서대로 출력    
            print('{:>2}'.format(d), end='  ')
            d = d + 1
        
            # 단, 전체데이터는 7번째마다 개행    
        if n % 7 == 0:
            print()

def main():
    year = int(input('연도를 입력하세요 (ex. YYYY) ->'))
    month = int(input('월을 입력하세요 (1~12) ->'))
    display(year, month)

main()