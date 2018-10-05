# demo10_11.py

exec('value = 10')
print(value)
#python_src = input('코드를 입력하세요->')
#exec("for i in range(5):print(i, end=', ')")
#exec(python_src)
code = compile("""
for i in range(10):
    print(i, end=', ')
print()
    """, '<string>', 'exec')

for i in range(10):
    exec(code)


