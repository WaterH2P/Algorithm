import re, random

# 使用 Python 的 r 前缀，就不用考虑转义的问题
regex = r'\d+'
n = '2cle'
if re.match(regex, n) :
    print('ok')
else :
    print('failed')

re_split = r'[\s\,]+'
string = 'a b   c,   d'
print( re.split(re_split, string) )

# 分组
re_group = r'^(\d{3})-(\d{3,8})$'
tel = '010-12345'
m = re.match(re_group, tel)
# group(0) 是原始字符串
print(m.group(0), m.group(2), m.group(2))

# 预编译正则表达式
re_tel = re.compile(re_group)
print( re_tel.match(tel).groups() )