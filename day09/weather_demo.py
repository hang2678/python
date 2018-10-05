# weather_demo.py
import pymysql  # import sqlite3
from bs4 import BeautifulSoup
from urllib import request
from weather import Weather

# sqllite3.connect('파일명.db')
conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                     db='test_python', charset='utf8') 
cursor = conn.cursor(pymysql.cursors.DictCursor)
print("### 1. DB 연결 완료 ###")

target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, 'html.parser')
print("### 2. 날씨정보 취득 완료 ###")

for location in soup.select('location'): # select, select_one 원하는 값 추출
    if location.select_one('city').string == '서울':
        data = location.select('data')
        #print('도시:', location.select_one('city').string)
        city = location.select_one('city').string

        # 0) 기존 데이터 삭제 (같은 날짜의 데이터만)
        delSql = """
            delete from weather
            where fc_date between date(%s) and date(%s)
        """
        cursor.execute(delSql, (data[0].select_one('tmef').string, 
                                data[len(data) - 1].select_one('tmef').string))
        
        print("### 3. 기존 날씨정보 삭제 완료 ###")
        for d in data: # 13 10/5 ~ 10/12 
            # 1) Weather 객체 생성 (13개) -> DB저장
            weather = Weather(1, city, d.select_one('tmef').string,
                              d.select_one('wf').string, d.select_one('tmn').string,
                              d.select_one('tmx').string)
            sql = """
               INSERT INTO weather(location, fc_date, description, temp_min, temp_max)
               VALUES(%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (weather.location, weather.fc_date, 
                                weather.description, weather.temp_min, weather.temp_max))
            
        conn.commit()
        print('### 4. {0} 데이터 저장 완료 ###'.format(city))
        break

cursor.close()
conn.close()    


