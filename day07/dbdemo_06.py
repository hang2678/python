# dbdemo_06.py (using function)
import sqlite3

# Python DB API
con = sqlite3.connect('user.db')
cursor = con.cursor()   

def selectData():
    sql1 = "SELECT * FROM tblAddr"
    cursor.execute(sql1)
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('이름:%s, 전화번호:%s, 주소:%s' % row)
    
def updateData():
    updateSql = "UPDATE tblAddr SET addr='서울' WHERE name='홍길동'"
    cursor.execute(updateSql)
    con.commit()
    print('수정 성공')

def insertData():
    cursor.execute("INSERT INTO tblAddr VALUES('홍길동','031-301-9999','인천')")
    con.commit()
    print(" 데이터 추가 성공")

# def updateData(isInsert):
#     if isInsert == True:
#         sql = "INSERT"
#     else:
#         sql = "UPDATE"

#     cursor.execute(sql)
#     con.commit()
#     print(isInsert, " 성공!")
    
def closeConnection():
    cursor.close()
    con.close()

def main():
    selectData()
    updateData()
    selectData()
    closeConnection()

main()