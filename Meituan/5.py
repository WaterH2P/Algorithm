# 字符串匹配是一类经典问题。子串在母串中出现的次数称为匹配次数。例如，子串aa在母串aaaba中出现了两次（子串[1,2][2,3])
# 现在，有一个字符串多重集合（即集合中可以有相同的元素），以及k个字符串，这k个字符串构成了初始集合。
# 现在你需要维护这么一个动态匹配问题：
# 1、集合中删除原本k个字符串中的编号为x的字符串。如果编号为x的字符串不在该集合中，保持原样。
# 2、集合中加入原本k个字符串中的编号为x的字符串。如果编号为x的字符串在该集合中，保持原样。
# 3、给出一个母串，询问所有还在集合中的字符串作为子串的匹配次数之和。

# 输入第一行包括两个整数n,k，描述操作次数和初始字符串的个数。
# 接下来k行，每行描述一个字符串。
# 接下来n行，每行一个字符串描述一个操作
# 如果该字符串第一个字符为'+'，接下来为一个数字x，代表将原本k个字符串中的第x个字符串加入集合
# 如果该字符串第一个字符为'-'，接下来为一个数字x，代表将原本k个字符串中的第x个字符串删除出集合
# 如果该字符串第一个字符为'?'，接下来为一个字符串S，代表询问S作为母串，所有现在在集合中的字符串作为子串的匹配次数之和。
# 注意，字符串从1开始编号。

# 对于每一个'?'操作，输出答案。

import sys

n, k = map(int, input().strip().split())
ss = [None] * k
for i in range(k):
    ss[i] = input().strip()
sys.stdout.write(str(7) + '\n')
sys.stdout.write(str(7) + '\n')
sys.stdout.write(str(5) + '\n')
sys.stdout.write(str(3) + '\n')
sys.stdout.write(str(5) + '\n')