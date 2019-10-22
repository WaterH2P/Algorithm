

# try:
#     f = open('./test_open.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# read() : 读取全部内容
# readline() : 每次读取一行内容
# readlines() : 一次读取所有内容并按行返回 list
with open('./test_open.txt', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    while(line):
        print(line)
        line = f.readline().strip()

with open('./test_open.txt', 'a', encoding='utf-8') as f:
    f.write('Hello World\n').strip()