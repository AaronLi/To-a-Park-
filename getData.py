from math import radians, cos, sin, asin, sqrt
from urllib.request import urlopen
import json
def getData(f):
    "f is the opened file"
    getdata = []
    #ali is the entire file
    ali = f.read().decode().split("<entry>")

    for entry in ali:#looking for
        linedata = {}

        for line in entry.split("\n") :
            if line[:4] == "<id>":
                continue
            data = line.strip(">").split(">")
            if len(data) == 1 or len(data) > 2:
                continue
            data2 = []
            for k in data:
                data2 = data2 + k.split("<")
            if data2[-1][3:] != "__id":
                 linedata[data2[-1][3:]] = data2[-2].strip()
        getdata.append(linedata)
    return getdata
def getPossiblePlaces(data,fee,maxDist):
    "All possible places within the boundary"
    possible = []
    myloc = getMyLoc()
    for place in data:
        if 'id' not in place:
            continue
        if 'longitude' not in place:
            continue
        if 'latitude' not in place:
            continue
        if (float(place['entrancefee']) <= 0 or fee) and haversine(myloc,(float(place['longitude']),float(place['latitude']))) <= maxDist:
            possible.append(place)
    return possible
def getClosestPlace(mydicts,ideald):
    closest = 100000000000
    best = {}
    myloc = getMyLoc()
    for place in mydicts:
        if 'id' not in place:
            continue

        dist = abs(haversine(myloc,(float(place['longitude']),float(place['latitude'])))-ideald)
        if ideald*0.666 < dist < closest and dist < ideald*1.5:
            best = place
            closest = dist
    return best
def getMyLoc():
    "returns user's current location in (longitude, latitude)"
    f = urlopen('http://freegeoip.net/json/')
    json_string = str(f.read())
    json_string = json_string[2:-3]
    f.close()
    location = eval(json_string)
    return (location['longitude'],location['latitude'])
def haversine(ll1, ll2, miles=False):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1,lat1 = ll1
    lon2,lat2 = ll2
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 if miles else 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
def convert(val,unit):
    "convert all values to metres"
    reallength = val
    if unit.lower() in ["kilometers","miles","yards","feet"]:
        #convert to metres
        if unit.lower() == "kilometers":
            reallength = val*1000
        if unit.lower() == "miles":
            reallength = val*1609.344
        if unit.lower() == "yards":
            reallength = val*0.9144
        if unit.lower() == "feet":
            reallength = val*0.3048
    return reallength
def unconvert(val,unit):
    "converts kilometers into unit"
    reallength = val
    if unit.lower() in ["meters","miles","yards","feet"]:
        if unit.lower() == "meters":
            reallength *= 1000
        if unit.lower() == "miles":
            reallength /= 1.6
        if unit.lower() == "yards":
            reallength /= 0.9144*1000
        if unit.lower() == "feet":
            reallength /= 0.3048*1000
    return reallength
