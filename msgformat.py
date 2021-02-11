"""
|----------+---------------+----------+-----------+--------------|
| DevID    | Date And Time | location | Hop Count | CRC ( temp ) |
|----------+---------------+----------+-----------+--------------|
| 11 Bytes | 8 Bytes       | 12 Bytes | 1 Byte    | 8 Bytes      |
|----------+---------------+----------+-----------+--------------|

TOTAL = 40 Bytes ( DevID is switched from IPv6 to custom format mentioned below)
"""
from datetime import datetime as dt
from baseconv import base36 as bs
from zlib import crc32 as crc

import random

rint = random.randint

DevID = "INAP" + \
    str(random.choice([1, 2, 3, 4, 6, 8])) + bs.encode(rint(0, 999999999))
devid_len = len(DevID)

if(devid_len < 11):
    DevID = (11 - devid_len) * '0' + DevID


def fordat():
    date = str(dt.now().date())
    date = date.split('-')
    date.reverse()
    date = ''.join(date[:2]) + date[2][2:]
    time = str(dt.now().time())
    time = time.split(':')
    time = ''.join(time[:2]) + time[2][:2]
    res = date + time
    l = len(res)
    if(l < 8):
        8-l*'0' + res
    return bs.encode(res)


lat1 = "13.026101239125405"
long1 = "80.01504296085217"
lat1 = lat1.split('.')
long1 = long1.split('.')
lat = lat1[0] + lat1[1][:6]
longt = long1[0] + long1[1][:6]
dat = fordat()
enlat = bs.encode(lat)
enlat_len = len(enlat)
enlat = (6 - enlat_len) * '0' + enlat if enlat_len < 6 else enlat
enlong = bs.encode(longt)
enlong_len = len(enlong)
enlong = (6 - enlong_len) * '0' + enlong if enlong_len < 6 else enlong
encoded_message = DevID + fordat() + enlat + enlong + '0'
print(len(encoded_message))
print(encoded_message)
crclen = len(str(crc(bytes(encoded_message, encoding='utf8'))))
encoded_message = encoded_message + \
    str(crc(bytes(encoded_message, encoding='utf8')))
print(encoded_message)
print(len(encoded_message))
print("enlat:{}, enlong:{}".format(enlat, enlong))
print("devid_len:{}, datlen:{}, loclen:{}, hopcount:1, CRClen:{}".format(
    devid_len, len(dat), len(enlong) + len(enlat), crclen))
print(str(crc(b'INAP2a9owjl15g3dno607r7051bn1220')))
print(str(crc(b'INAP2a9owjl15g3dno607r7051bn0020')))
# print(len(bs.encode(li)))
