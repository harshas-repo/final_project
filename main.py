import random as ra
import simpy
import math

# config
n_nodes = 5


# node class
class node:
    def __init__(self, nodes):
        nodes.self = nodes
    # set default or random bearing for the location
    # function that sets node location
    # fucntion that returns node location


# location class
class location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


def distBtw(lat1, lon1, lat2, lon2):
    earthRadiusKm = 6371

    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * \
        math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earthRadiusKm * c


# def distBtw(lat1, lng1, lat2, lng2):
    # earthRadius = 3958.75
    # dLat = math.radians(lat2-lat1)
    # dLng = math.radians(lng2-lng1)
    # a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * \
    # math.cos(math.radians(lat2)) * math.sin(dLng/2) * math.sin(dLng/2)
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # dist = earthRadius * c
    # return dist


loc1 = location(13.026101239125405,
                80.01504296085217)
loc2 = location(13.035804392956667,
                80.0462244773235)
print(loc1.lat, loc1.lon, loc2.lat, loc2.lon)
print(distBtw(loc1.lat, loc1.lon, loc2.lat, loc2.lon))
