# dbdemo_02.py (SELECT)
import sqlite3

con = sqlite3.connect('user.db')
cursor = con.cursor()

# DML - CRUD (insert, select, update, delete)
# SELECT * FROM tblAddr WHERE name='이도원'
#sql1 = 'SELECT * FROM tblAddr WHERE name=\'이도원\''
sql1 = "SELECT * FROM tblAddr"
cursor.execute(sql1)

# fetchall(), fetchone(), fetchmany()
# table = cursor.fetchall()
# for row in table:
while True:
    row = cursor.fetchone()
    if row == None:
        break
    print('이름:%s, 전화번호:%s, 주소:%s' % row)
    
print('------------- execute update -----------')
updateSql = "UPDATE tblAddr SET addr='서울' WHERE name='홍길동'"
cursor.execute(updateSql)
con.commit()

print('수정 성공')

cursor.close()
con.close()
