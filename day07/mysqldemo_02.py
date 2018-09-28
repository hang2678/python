# mysqldemo_02.py (connection)
import pymysql

# 1. Connection to mysql (remote) -> url, user, password
conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                     db='test_python', charset='utf8') 
cursor = conn.cursor()

inputId = input('아이디를 입력해 주세요-> ')
inputPwd = input('비밀번호를 입력해 주세요-> ')

# select sql 작성 
# selectSql = 'SELECT * FROM member WHERE id=\'' + inputId \
#                 + '\' AND pwd=\'' + inputPwd + '\''
# string interpolation -> parameter placeholder
selectSql = 'SELECT * FROM member WHERE id=%s AND pwd=%s'
cursor.execute(selectSql, (inputId, inputPwd))
row = cursor.fetchone()
if row == None:
    print('로그인 실패!! ID나 PWD가 잘못 되었습니다.')
else:
    print('로그인 성공!! ', row)

cursor.close()
conn.close()
