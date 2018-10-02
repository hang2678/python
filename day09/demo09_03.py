from decimal import Decimal
from fractions import *

a = Fraction(2, 3) # 2/3 
b = Fraction(4, 5) # 4/5
c = a + b # 2/3 + 4/5 = 22/15 ; 1.5 + 0.1 = 1.6
print(c)    # ??
d = c + 0.1
print(d)    # ??


# a = Fraction(1, 3) # 1/3
# b = Fraction(8, 10) # 4/5
# print(a)
# print(b)
# print(8/10) # 0.8

# f = 0.1 # 0.1 * 100 = 10
# sum = 0
# for i in range(100):
#     sum += f
# print(sum)
# print('-' * 100)

# d = Decimal('0.1')
# sum_d = 0 
# for i in range(100):
#     sum_d += d
# print(sum_d)
