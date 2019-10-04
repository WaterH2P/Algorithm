
from io import BytesIO

# 操作二进制数据
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())