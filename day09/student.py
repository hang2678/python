# student.py
class Student:
    def __init__(self, name, kor, eng, mat, total, avg):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__total = total
        self.__avg = avg
    
    @property # getter
    def name(self):
        return self.__name
    @name.setter # setter
    def name(self, n):
        self.__name = n
        
    @property # getter
    def kor(self):
        return self.__kor
    @kor.setter # setter
    def kor(self, kor):
        self.__kor = kor

    @property # getter
    def eng(self):
        return self.__eng
    @eng.setter # setter
    def eng(self, eng):
        self.__eng = eng

    @property # getter
    def mat(self):
        return self.__mat
    @mat.setter # setter
    def mat(self, mat):
        self.__mat = mat

    @property # getter
    def total(self):
        return self.__total
    @total.setter # setter
    def total(self, total):
        self.__total = total

    @property # getter
    def average(self):
        return self.__avg
    @average.setter # setter
    def average(self, average):
        self.__avg = average

    def __str__(self):
        return self.__name + "\t" + \
                str(self.__kor) + "\t" + \
                str(self.__eng) + "\t" + \
                str(self.__mat) + "\t" + \
                str(self.__total) + "\t" + \
                str(self.__avg)
    
    def __eq__(self, other):
        # 사용자 이름과 총점이 같으면 -> TRUE
        return self.__name == other.__name and self.__total == other.__total
    
#-----------------
if __name__ == '__main__':
    student1 = Student('HONG', 90, 80, 70, (90+80+70), (90+80+70)/3)
    print(student1)
    
    student2 = Student('HONG', 100, 90, 50, (100+90+50), (100+90+50)/3)
    print(student2)
    print(student1 == student2) #FALSE 
    print(student1 != student2) #overloading -> 함수 재정의
    
