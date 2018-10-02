# weather_demo.py
# beautifulsoup4
from bs4 import BeautifulSoup
from urllib import request

# request.urlopen() 기상청 날씨정보 취득
# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup 클래스는 웹페이지 분석
soup = BeautifulSoup(target, 'html.parser')

for location in soup.select('location'): # select, select_one 원하는 값 추출
    if location.select_one('city').string == '서울':
        data = location.select('data')
        print('도시:', location.select_one('city').string)

        for d in data:
            print('날짜:', d.select_one('tmef').string, end='\t')
            print('날씨:', d.select_one('wf').string, end='\t')
            print('최저기온:', d.select_one('tmn').string, end='\t')
            print('최고기온:', d.select_one('tmx').string, end='\t')
            print()
        break
    


