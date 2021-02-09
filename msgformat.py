"""
|----------+---------------+----------+-----------+------------|
| DevID    | Date And Time | location | Hop Count | RSSI Value |
|----------+---------------+----------+-----------+------------|
| 11 Bytes | 8 Bytes       | 12 Bytes | 1 Byte    | 3 Byte     |
|----------+---------------+----------+-----------+------------|

TOTAL = 35 Bytes ( DevID is switched from IPv6 to custom format mentioned below)
"""
from datetime import datetime as dt
from baseconv import base36 as bs


def fordat():
    date = str(dt.now().date())
    date = date.split('-')
    date.reverse()
    date = ''.join(date[:2]) + date[2][2:]
    time = str(dt.now().time())
    time = time.split(':')
    time = ''.join(time[:2]) + time[2][:2]
    print(date)
    print(time)
    return date+time


temp = fordat()
print(len(temp))
print(bs.encode(temp))
print(len(bs.encode(temp)))
li = "2001:0db8:85a3:0000:0000:8a2e:0370:7334".split(':')
binli = []
for i in li:
    binli.append(bs.encode(int(i, 16)))
print(binli)
print(':'.join(binli))
print(len(':'.join(binli)))
worst_case = []
for i in range(8):
    worst_case.append(bs.encode(int("ffff", 16)))

print(':'.join(worst_case))
print(len(':'.join(worst_case)))
# print(len(bs.encode(li)))
