# weather_info.py (날씨 정보 조회)
import pymysql  # import sqlite3
from weather import Weather

# sqllite3.connect('파일명.db')
conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                     db='test_python', charset='utf8') 
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = 'SELECT * FROM weather WHERE location=\'서울\' ORDER BY fc_date'
cursor.execute(sql)
data_list = cursor.fetchall()
print('날짜\t날씨\t최저온도\t최고온도')
print('-' * 50)
for data in data_list:
    weather = Weather(data['idx'], data['location'], 
                    str(data['fc_date']), data['description'], 
                    str(data['temp_min']), str(data['temp_max']))
    print(weather)

conn.close()
cursor.close()