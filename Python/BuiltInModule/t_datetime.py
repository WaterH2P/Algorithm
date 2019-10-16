from datetime import datetime, timedelta

now = datetime.now()
print(now)

dt = datetime(2015, 8, 8, 8, 8, 8)
print(dt)

# datetime => timestamp
dtt = dt.timestamp()
print(dtt)

# timestamp => datetime
t = datetime.fromtimestamp(dtt)
print(t)

# str => datetime
cday = datetime.strptime('2015-8-8 08:08:08', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime => str
dt2 = datetime.now().strftime('%a, %b %d %H:%M')
print(dt2)

# datetime 加减
now = datetime.now()
print( now )
print( now + timedelta(hours=10) )
print( now - timedelta(days=10) )
print( now + timedelta(hours=10, days=10) )