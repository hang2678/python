# sungjuk.py
# 이름, 국, 수, 영, 과 * 10
class Student:
    # 생성자 메소드
    def __init__(self, name, kor, mat, eng, sci):
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng
        self.sci = sci

    def get_sum(self): # self.name, self.kor, self.eng, self.mat
        return self.kor + self.mat + self.eng + self.sci

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return '{0}\t{1}\t{2}'.format(self.name, self.get_sum(), self.get_average())

    def study(self):
        print('공부를 합니다.')

class Teacher:
    def teach(self):
        print('학생을 가르칩니다.')

students = [
    Student('HONG', 90, 80, 70, 60),
    Student('PARK', 95, 65, 72, 80),
    Student('LEE', 96, 100, 75, 70),
    Student('CHO', 97, 70, 78, 90)
]

for student in students:
    print(student.to_string())

print(isinstance(students[0], Student))

classroom = [Student('HONG', 90, 80, 70, 60), 
             Student('HONG', 90, 80, 70, 60), 
             Teacher(), 
             Teacher(), 
             Student('HONG', 90, 80, 70, 60)]
for person in classroom:
    #print(person) # student.study(), teacher.teach()
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
    else:
        print('실행할 수 없습니다.')
