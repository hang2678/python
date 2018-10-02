class Shape: # Entity class -> 생성 -> DB -> init초기화
    area = 0
    # a + b => ? 
    def __add__(self, other):
        return self.area + other.area
    # < 연산자 재정의 : __lt__ (area 비교)
    def __lt__(self, other):
        return self.area < other.area

a = Shape()
a.area = 10
b = Shape()
b.area = 20

print(a < b)
