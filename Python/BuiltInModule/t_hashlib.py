import hashlib, hmac

# 128 bit
md5 = hashlib.md5()
md5.update('how to use python hashlib'.encode('utf-8'))
md5.update('i am h2p'.encode('utf-8'))
print(md5.hexdigest())

# 160 bit
sha1 = hashlib.sha1()
sha1.update('how to use python hashlib'.encode('utf-8'))
sha1.update('i am h2p'.encode('utf-8'))
print(sha1.hexdigest())

# 传入的 key 和 message 都是 bytes 类型
message = b'hello world'
key = b'h2p'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())