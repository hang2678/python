# filedemo_01.py
f = open('my_test.txt', "rt")
# rows = f.readlines()
# for row in rows:
#     print(row, end = '')
# f.close()
# for line in f:
#     print(line, end='')    
# f.close()
f.seek(12, 0)
text = f.read()
f.close()
print(text)