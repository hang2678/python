# weather.py (DB.weather 테이블과 매핑되는 클래스)
class Weather:
    def __init__(self, idx, location, fc_date, description, temp_min, temp_max):
        self.idx = idx
        self.location = location
        self.fc_date = fc_date
        self.description = description
        self.temp_min = temp_min
        self.temp_max = temp_max
    
    def __str__(self):
        return self.fc_date + "\t" + \
                self.description + "\t" + \
                self.temp_min + "\t" + \
                self.temp_max

