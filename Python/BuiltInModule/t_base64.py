import base64

# 对二进制数据进行处理，每 3 个字节一组，一共是 3x8=24bit，划为 4 组，每组正好 6bit
# 这样我们得到 4 个数字作为索引，然后查表，获得相应的 4 个字符，就是编码后的字符串
print( base64.b64encode(b'binary\x00string') )
print( base64.b64decode(b'YmluYXJ5AHN0cmluZw==') )

print( 'a'*3 )