# refer to the links attahced for more info
# https://stackoverflow.com/questions/19803604/increment-meters-to-latitude-and-longitude
# https://stackoverflow.com/questions/4308262/calculate-compass-bearing-heading-to-location-in-android

import math

# to caliculate bearing based on the current and destination location co-ordinates
# updated version


def bearing():
    startLat = math.radians(13.026101239125405)
    startLong = math.radians(80.01504296085217)
    endLat = math.radians(13.035804392956667)
    endLong = math.radians(80.0462244773235)
    dLong = endLong - startLong
    dPhi = math.log(math.tan(endLat/2.0+math.pi/4.0) /
                    math.tan(startLat/2.0+math.pi/4.0))
    if abs(dLong) > math.pi:
        if dLong > 0.0:
            dLong = -(2.0 * math.pi - dLong)
    else:
        dLong = (2.0 * math.pi + dLong)

    bearing = (math.degrees(math.atan2(dLong, dPhi)) + 360.0) % 360.0
    return bearing

# def bearing():
# lat1 = math.radians(13.026101239125405)
# long1 = math.radians(80.01504296085217)
# # 13.03578525069192,
# # apollo college co-ordinates
# # lat2 = math.radians(13.036902955382336)
# # long2 = math.radians(80.04622399073887)
# # 13.029671532500425, 80.02968502821973
# # 13.035804392956667, 80.0462244773235
# lat2 = math.radians(13.035804392956667)
# long2 = math.radians(80.0462244773235)
# longdiff = math.radians((long2 - long1))
# x = math.sin(longdiff) * math.cos(lat2)
# y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * \
# math.cos(lat2) * math.cos(longdiff)
# return math.degrees(math.atan2(x, y))


def distance():
    R = 6371000
    lat1 = math.radians(13.026101239125405)
    long1 = math.radians(80.01504296085217)
    bear = bearing()
    radbear = math.radians(72)
    print(f"bearing {bear}")
    distance = 3254  # abs(actual_distance - 6000)
    lat2 = math.asin(math.sin(lat1)*math.cos(distance / R) +
                     math.cos(lat1)*math.sin(distance/R)*math.cos(radbear))
    lon2 = long1 + math.atan2(math.sin(radbear)*math.sin(distance / R)*math.cos(lat1),
                              math.cos(distance/R)-math.sin(lat1)*math.sin(lat2))
    print(math.degrees(lat2), math.degrees(lon2))
    return


print(bearing())
distance()
