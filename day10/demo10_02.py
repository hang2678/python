# seq.py
class Seq:
    # start = 0
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        # self.index += 2
        # if self.index >= len(self.data):
        #     raise StopIteration
        # return self.data[self.index : self.index + 2]
        elements = self.data.split()  # len -> 6
        if self.index >= len(elements):
            raise StopIteration

        result = elements[self.index]
        self.index += 1

        return result
        
# APPLE,BANANA,ORANGE,PYHTON,JAVA,DJANGO,
# data = Seq("AABBCCDDEEFFGGHHII")
data = Seq("APPLE BANANA ORANGE PYHTON JAVA DJANGO")
for k in data:
    print(k, end=',')
