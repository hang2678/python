# person.py
class School:
    def __init__(self):
        print('학교를 추가합니다.')

    def set_classroom(self):
        print('교실을 배정합니다.')
    
    def execute_test(self):
        print('시험을 봅니다.')

class Person:
    def __init__(self):
        print('사람 데이터를 추가합니다.')

    def go2school(self):
        print('학교를 갑니다.')
    
    def lunch(self):
        print('점심을 먹습니다.(12:00~13:00)')

    def go2home(self):
        print('집에 돌아 갑니다.')

    def holiday(self):
        print('휴일에는 학교에 가지 않습니다.')    

class Student(School, Person):
    def __init__(self):
        print('학생 데이터를 추가합니다.')
        super().__init__()

    def study(self):
        print('공부를 합니다.')
    def go2home(self):
        print("오후 3시에 돌아갑니다.")
    
class Teacher(Person, School):
    def __init__(self):
        print('선생님 데이터를 추가합니다.')
        super().__init__()

    def teach(self):
        print('학생을 가르칩니다.')
    def go2home(self):
        print("오후 6시에 돌아갑니다.")
    def holiday(self):
        print("휴일에도 학교에 가야합니다.")
    
# Student, Teacher 인스턴스 생성 후 
# 개별 메소드 호출
student1 = Student()
teacher1 = Teacher()
print("*** 학생의 하루 일과")
student1.set_classroom()
student1.go2school()
student1.study()
student1.lunch()
student1.study()
student1.execute_test()
student1.go2home()
student1.holiday()

print("*** 선생님의 하루 일과")
teacher1.go2school()
teacher1.teach()
teacher1.lunch()
teacher1.teach()
teacher1.go2home()
teacher1.holiday()