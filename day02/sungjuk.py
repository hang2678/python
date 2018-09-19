sungjuk = {}
sungjuk['HONG'] = [100, 90, 80]
sungjuk['KANG'] = [70, 85, 99]
sungjuk['KIM'] = [45, 86, 90]
sungjuk['LEE'] = [80, 85, 81]   # 국어,영어,수학,총점,평균,석차

def displaySungjuk():
    for student in sungjuk:
        temp = sungjuk[student] #[100, 90, 80] -> list -> extend([총점,평균])
        if len(temp) < 5:
            sum = temp[0] + temp[1] + temp[2]
            avg = sum/3
            temp.extend([sum, avg]) # [100, 90, 80, 270, 90]
        
    newList = sorted(sungjuk.items(), key=lambda element:element[1][3], reverse=True)
    for student in newList:
        print(student[0], '\t', seperateGrade(student[1]))

def seperateGrade(data):
    result = ''
    for d in range(len(data) - 1):
        result += str(data[d]) + '\t'
    
    return result + ("%4f" % (data[len(data) - 1]))

while True:
    print("## 현재 등록자 수:", len(sungjuk))
    cmd = int(input('1) 성적입력 2) 성적출력 3) 성적조회 4) 종료 (1~4) ->'))
    if cmd == 1:
        userData = input('성적을 입력하세요. (이름,국어,영어,수학) ->')
        data = userData.split(',')
        print(data) #['홍길동', '100', '90', '70'], data[1:]
        sungjuk[data[0]] = [int(data[1]), int(data[2]), int(data[3])]
    elif cmd == 2:
        print('####################################################')
        print('이름\t국어\t영어\t수학\t총점\t평균')
        print('####################################################')
        displaySungjuk()
    elif cmd == 3:
        # 정보 조회 -> 출력 
        searchUser = input("검색할 학생이름을 입력하세요->")
        print(sungjuk[searchUser])
    elif cmd == 4:
        quit()
    else:
        print("잘못된 명령어 입니다. 다시 입력해 주세요.")
        continue

    print()
