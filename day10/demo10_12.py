# demo10_12.py
outer_code = open('compile_src.py').read()
code = compile(outer_code, 'compile_src.py', 'exec')
exec(code)