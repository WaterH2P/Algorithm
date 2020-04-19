# 有一个很经典的问题是，当前时间是aa:bb,请问若干分钟后是什么时间？我们今天的问题是一个相反的问题。
# 已知现在的时刻是星期x的yy:zz时刻，请问n分钟前是周几，时间是多少。
# 例如现在是周三，02:10,则200分钟之前，应该是周二，22:50。
# 输入包含三行
# 第一行一个正整数x，表示今天是周x。(1<=x<=7)
# 第二行是一个24小时制的时间表示，时和分均含前导0，例如，1时1分表示为01:01。保证时间格式是合法的。
# 第三行是一个正整数n，表示要求的是n分钟之前的时间。(1<=n<=10^9)

import sys

x = int(input().strip())
h, m = map(int, input().strip().split(':'))
n = int(input().strip())

dm, hm = 1440, 60
wd = 7

x -= n // dm // 7
if x <= 0: x += 7

leftm = n % dm
tdm = h * 60 + m
if leftm == tdm:
    leftm -= tdm
    h, m = 0, 0
elif leftm > tdm:
    leftm -= (tdm + 1)
    x -= 1
    h, m = 23, 59

while leftm > 0:
    if h == 0 and m == 0:
        h, m = 23, 59
    if leftm >= 60:
        leftm -= 60
        h -= 1
    elif leftm > m:
        leftm -= (m + 1)
        h -= 1
        m = 59
    else:
        m -= leftm
        leftm -= leftm
        
if x <= 0: x += 7

sys.stdout.write(str(x) + '\n')
if h < 10: h = '0' + str(h)
if m < 10: m = '0' + str(m)
output = str(h) + ':' + str(m) + '\n'
sys.stdout.write(output)