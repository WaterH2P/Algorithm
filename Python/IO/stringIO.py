from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f2 = StringIO('Hello\nWorld\nSB')
while True:
    s = f2.readline()
    if s == '' :
        break
    print(s.strip())