"""
|----------+---------------+----------+-----------+--------+--------------|
| DevID    | Date And Time | location | Hop Count | GFlag  | CRC ( temp ) |
|----------+---------------+----------+-----------+--------+--------------|
| 11 Bytes | 8 Bytes       | 12 Bytes | 1 Byte    | 1 Byte | 10 Bytes     |
|----------+---------------+----------+-----------+--------+--------------|

TOTAL = 40 Bytes ( DevID is switched from IPv6 to custom format mentioned below)

DevID = Country ( 2 characters ) + State ( 2 Characters ) + Vehicle Type ( Based on no.of tyres ) 11 Bytes
[Random vehilce ID between (0, 999,999,999) is converted to base 36 to reduce the size)]

Maximum: Each category of vehicle in each state of a country can have 999,999,999 vehicles
"""

import random
import baseconv
from datetime import datetime as dt
from baseconv import base36 as bs
import zlib
crc = zlib.crc32


# encoding date and time
# NOTE: whenever the length of the date and time is smaller than the fixated length a zero is appended at front
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


# device id formultion
# NOTE: whenever the length of the device id is smaller than the fixated length a zero is appended at front
c = 0
rint = random.randint
randevid = rint(0, 999999999)
DevID = "INAP" + \
    str(random.choice([1, 2, 3, 4, 6, 8])) + bs.encode(randevid)
devid_len = len(DevID)
unencoded_msg = "INAP1" + str(randevid)

if(devid_len < 11):
    DevID = (11 - devid_len) * '0' + DevID

unencoded_msg += str(dt.now())

# lat1 and long1 encoding
# NOTE: whenever the length of the location attributes is smaller than the fixated length a zero is appended at front
lat1 = "13.026101239125405"
long1 = "80.01504296085217"
unencoded_msg += (lat1 + long1)
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
encoded_message = DevID + fordat() + enlat + enlong + '0' + '1'

# actual length and encoded_message length
print("length encoded message without CRC:", len(encoded_message))
print("encoded message without CRC:", encoded_message)

# creating and appending crc
msgcrc = str(crc(bytes(encoded_message, encoding='utf8')))
msgcrc = bs.encode(msgcrc)
crclen = len(msgcrc)
encoded_message = encoded_message + msgcrc
unencoded_msg += str(crc(bytes(unencoded_msg, encoding='utf8')))

print("Lenght of CRC:", crclen)
print("encoded message with CRC:", encoded_message)
print("Final packet with crc appended:", len(encoded_message))
print("Length of unencoded_msg:", len(unencoded_msg))
print("enlat:{}, enlong:{}".format(enlat, enlong))
# hop count limits the message transimission max 9, and GFlag 0/1 specifies whether the packet is intended for gateway or neighbouring node
print("devid_len:{}, datlen:{}, loclen:{}, hopcount:1, GFlag:1, CRClen:{}".format(
    devid_len, len(dat), len(enlong) + len(enlat), crclen))

# devid_len = length of devid
# dat = length date and time
# loclen = location_length
# crclen = CRC_length
