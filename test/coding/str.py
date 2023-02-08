s = 'stroka texta'
print(s.upper())
print(s.lower())
print(s.capitalize())

path = 'D:/python/str.py'
path2 = path.replace('/', '\\')
print(path2)

r = path2.split('\\')
print(r[-1])