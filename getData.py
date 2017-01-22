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
def getPossiblePlaces(data,maxFee,maxDist):
    "All possible places within the boundary"
    possible = []
    for place in data:
        if 'id' not in place:
            continue
        
        if place['entrancefee'] <= maxFee and haversine(getMyLoc(),(float(place['longitude']),float(place['latitude']))) <= maxDist:
            possible.append(place['name'] + ", " + place['county'] + " county")
    return possible
def getMyLoc():
    "returns user's current location in (longitude, latitude)"
    f = urlopen('http://freegeoip.net/json/')
    json_string = str(f.read())
    json_string = json_string[2:-3]
    f.close()
    location = eval(json_string)
    return (location['longitude'],location['latitude'])
def haversine(ll1, ll2):
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
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
