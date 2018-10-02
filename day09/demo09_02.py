class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    # def __eq__(self, other):
    #     return self.age == other.age and self.name == other.name
   
kim = Human(29, 'KIM')
lee = Human(29, 'KIM')
park = Human(29, 'PARK')
hong = kim
hong.name = 'HONG'

print(kim == lee)
print(kim == park)
print(kim == hong)
print(kim.name)