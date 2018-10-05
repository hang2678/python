# demo10_08.py
def param(func):
    def wrapper():
        return '<p>' + str(func()) + '</p>'
    return wrapper

@param
def outname():
    return 'pyhton'

@param
def outage():
    return 29

print(outname())
print(outage())