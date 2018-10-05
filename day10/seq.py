# seq.py
class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        # index가 초과가 되면 오류 발생 -> StopIteration
        if self.index >= len(self.data):
            raise StopIteration

        return self.data[self.index:self.index + 1]
# APPLE,BANANA,ORANGE,PYHTON,JAVA,DJANGO,
data = Seq("APPLE BANANA ORANGE PYHTON JAVA DJANGO")
for k in data:
    print(k, end=',')