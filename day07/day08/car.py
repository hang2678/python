# car.py
class Car:
    def __init__(self, color):
        self.color = color
        self.wheel_size = 16
        self.engine = 2000
        
    def forward(self):
        pass

    def backward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    @staticmethod
    def company_name():
        print("Samsung Multicampus and HP")

if __name__ == '__main__':
    my_car = Car(0xAAFF00)
    Car.company_name()

    my_second_car = Car(0x11FF00)
    Car.company_name()
    