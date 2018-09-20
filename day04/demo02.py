news = """Eying China's voracious demand, 
Cheniere Energy, ExxonMobil (XOM) and 
other American energy companies are racing to build 
more than two dozen expensive facilities to export 
liquefied natural gas, which is super-cooled natural gas 
that can be transported by ship.
"""

alphabet = {}  # dict()
for char in news:
    if char.isalpha() == False:  # char = .'
        continue
    char = char.lower()  # A -> a
    if char not in alphabet:  # True, False
        alphabet[char] = 1  # eye -> {'e':1, 'y':1, }
    else:
        alphabet[char] += 1  # alphabet[char] = alphabet[char] + 1

for c in range(ord('a'), ord('z') + 1):
    print(chr(c), '=', alphabet.get(chr(c), 0))


# print(alphabet)
# 오름차순 정렬 (A -> Z)
# keyList = list(alphabet.keys())
# keyList.sort()
# for key in keyList:
#     num = alphabet[key]
#     print(key, '=', num)
