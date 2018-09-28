# mysqldemo_01.py (connection)
import pymysql

# 1. Connection to mysql (remote) -> url, user, password
conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                     db='test_python', charset='utf8') 
cursor = conn.cursor()

# INSERT member(idx, id, pwd, name, reg_date)
# ('admin', '1234', 'Administrator', NOW())
# insertSql = """INSERT INTO member(id, pwd, name, reg_date) VALUES(
#     'admin', '1234', 'Administrator's', NOW()
# )"""
# hp'computer
insertSql = 'INSERT INTO member(id, pwd, name, reg_date) VALUES(%s, %s, %s, NOW())'
cursor.execute(insertSql, ('user1', '1111', 'TEST\'s USER'))

conn.commit()

# SELECT
selectSql = 'SELECT * FROM member'
cursor.execute(selectSql)
data = cursor.fetchall()

for row in data:
    print(row)

conn.close()