# dbdemo_01.py
import sqlite3

con = sqlite3.connect('user.db')
cursor = con.cursor()
cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""CREATE TABLE tblAddr(
    name CHAR(10) primary key,
    phone CHAR(15),
    addr TEXT
)""")

cursor.execute("INSERT INTO tblAddr VALUES('이도원','02-555-1234','서울')")
cursor.execute("INSERT INTO tblAddr VALUES('홍길동','031-301-9999','인천')")
print(" 데이터 추가 성공")

con.commit()

cursor.close()
con.close()
