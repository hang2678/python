import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                     db='test_python', charset='utf8') 
#cursor = conn.cursor()  # array base cusor(list) -> dictionary (key, value)
cursor = conn.cursor(pymysql.cursors.DictCursor)

def displaySungjuk(searchUser):
    # DB에서 데이터 조회 
    rows = selectList(searchUser)
    for row in rows:
        print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(
            row['name'],row['kor'],row['eng'],row['mat'],row['total'],row['average']))
           
def selectList(searchUser):
    if len(searchUser) == 0:
        # 전체 사용자
        selectSql = """
        SELECT 
            idx, name, kor, eng, mat, (kor+eng+mat) as total, (kor+eng+mat)/3 as average
        FROM sungjuk 
        ORDER BY total DESC
        """
        cursor.execute(selectSql)
    else:
        # 개별 사용자 검색
        selectSql = """
        SELECT 
            idx, name, kor, eng, mat, (kor+eng+mat) as total, (kor+eng+mat)/3 as average
        FROM sungjuk WHERE name=%s
        ORDER BY total DESC
        """
        cursor.execute(selectSql, searchUser)
    
    rows = cursor.fetchall()
    return rows

def addData(data):  #['홍길동','100','200','300']
    insertSql = """INSERT INTO sungjuk(name, kor, eng, mat, reg_date)
                    VALUES(%s, %s, %s, %s, NOW())"""

    cursor.exete(insertSql, (data[0], data[1], data[2], data[3]))
    conn.commit()
    print('## 사용자 정보 추가 성공!')
    
def closeConnection():
    cursor.close()
    conn.close()

def main():
    while True:
        print("## 현재 등록자 수:")
        # 1. 입력값이 숫자(1~4) 인지 확인
        try:
            cmd = int(input('1) 성적입력 2) 성적출력 3) 성적조회 4) 종료 (1~4) ->'))
        except:
            print("** 명령어는 1~4 사이의 숫자를 입력해야 합니다. **")
            continue

        if cmd == 1:
            # 2. 이름 뒤에 3개의 과목인지, ','로 구분되어 있는지 
            # 3. 각 과목의 점수는 0~100 
            while True:
                try:
                    userData = input('성적을 입력하세요. (이름,국어,영어,수학) -> ')        
                    data = userData.split(',') # len(data) = 4
                    if len(data) != 4: #NG
                        raise Exception
                    else: #OK
                        try:
                            kor = int(data[1])
                            eng = int(data[2])
                            mat = int(data[3])

                            if kor < 0 or kor > 100:
                                raise Exception
                            if eng < 0 or eng > 100:
                                raise Exception
                            if mat < 0 or mat > 100:
                                raise Exception
                        except:
                            raise Exception        
                except Exception as ex:
                    print("** 성적데이터를 정확하게 입력해 주세요. **")
                    continue
                else:       # if ~ else
                    print(data) #['홍길동', '100', '90', '70'], data[1:]
                    # DB에 저장
                    addData(data)
                    break
        elif cmd == 2:
            print('####################################################')
            print('이름\t국어\t영어\t수학\t총점\t평균')
            print('####################################################')
            displaySungjuk('')
        elif cmd == 3:
            # 정보 조회 -> 출력 
            searchUser = input("검색할 학생이름을 입력하세요->")
            # DB 검색
            displaySungjuk(searchUser)
        elif cmd == 4:
            closeConnection()
            quit()            
        else:
            print("잘못된 명령어 입니다. 다시 입력해 주세요.")
            continue

        print()

main()