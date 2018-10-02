# human.py

class Person:
    def __init__(self, name, age): # 객체 생성시 필요한 초기화 작업
        print("call init method")
        self.name = name
        self.age = age

    def intro(self):
        print('{0} {1}살'.format(self.name, self.age))

hong1 = Person('홍길동', 40)
hong1.intro()
kang1 = Person('강감찬', 50)
kang1.intro()

