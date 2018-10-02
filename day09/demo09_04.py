import array

my_array = array.array('i', [33, 45, 80, 67, 9.9])
for a in my_array:
    print(a, end=',')
my_array.append(100) # 33,45,80,67,99,100
# list에서 데이터 삭제  , 1번째 데이터 삭제
print()
del my_array[0] # 45,80,67,99,100
print('my_array[1]=', my_array[1]) # 80
print('my_array[2:4]=', my_array[2:4]) # 67,99
   