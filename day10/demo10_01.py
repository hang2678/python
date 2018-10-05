# 10_01.py
nums = [11, 22, 33]
print(nums[0], nums[1], nums[2])
for n in nums:
    print(n)
print('-' * 20)

it = iter(nums) # index -> next()
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    
    print(num)
