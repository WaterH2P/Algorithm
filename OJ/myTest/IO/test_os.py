
import os
# Window : nt
# Linux、Unix、MacOS : posix
print(os.name)

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 路经合成
pwd = os.path.abspath('.')
path = os.path.join(pwd, 'test')
print(path)
os.rmdir(path)
os.mkdir(path)

filePath = os.path.join(pwd, 'test', 'test.txt')
print(os.path.split(filePath))
print(os.path.splitext(filePath))

# 显示当前目录所有文件夹
dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirs)

# 显示当前目录所有 .py 文件
pys = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x) == '.py']
print(pys)