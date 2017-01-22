from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from getData import *
from urllib.request import urlopen
import requests
import urllib
import re
from datetime import datetime
import random
url = urlopen("https://data.michigan.gov/OData.svc/aiht-57sm")
tripInfo = getData(url)
#tripInfo = open("data.txt")
app = Flask(__name__)
ask = Ask(app, '/')
yesses = set(['yes','yeah','true','indeed','sure','ya','yeah sure','of course','affirmative','correct'])
nos = set(['no','nah','false','of course not','no thank you','negative'])
fractions = {"a half":0.5,"a quarter":0.25,"three quarters":0.75,"a third":0.3333333,"two thirds":0.6666666}

def endresult(fee,dist):
    #possibilites = getData(tripInfo)
    return (" and ").join(possiblities['name'])

@ask.intent('RandomTrip')
def randTrip():#initializing everything
    welcome = render_template("welcome")
    reprompt = render_template("reprompt")
    session.attributes['de'] = False
    session.attributes['fe'] = False
    session.attributes['d'] = 9999999
    session.attributes['f'] = None
    session.attributes['units'] = 'miles'
    return question(welcome)

##@ask.intent('RandomTripWalking')
##def randTripWalking():
##    "assumes somewhere within walking distance (2 miles)"
##    if 'de' not in session.attributes:
##        session.attributes['de'] = False
##    if 'fe' not in session.attributes:
##        sessionattributes['fe'] = False
##    if 'd' not in session.attributes:
##        session.attributes['d'] = 9999999
##    if 'f' not in session.attributes:
##        session.attributes['f'] = None
##    return question("hi")

@ask.intent('BoolIntent')
def randTripbool(Decision):
    if 'de' not in session.attributes:
        session.attributes['de'] = False
    if 'fe' not in session.attributes:
        session.attributes['fe'] = False
    if 'd' not in session.attributes:
        session.attributes['d'] = 9999999
    if 'f' not in session.attributes:
        session.attributes['f'] = None
    if 'units' not in session.attributes:
        session.attributes['units'] = "guilty crown"
    if not session.attributes['de'] and not session.attributes['fe']:
        if Decision in yesses:
            return question("Great!, How far are you willing to travel?")
        else:
            if Decision not in nos:
                print("New false word:",Decision)
            return statement("Maybe next time!")
    if session.attributes['de'] and not session.attributes['fe']:
        session.attributes['f'] = Decision in yesses
        session.attributes['fe'] = Decision in yesses
        places = getPossiblePlaces(tripInfo,session.attributes['f'],session.attributes['d']+10000)
        myLoc = getMyLoc()
        picked = getClosestPlace(places,session.attributes['d'])#dictionary of the ideal place
        parkLoc = (float(picked['longitude']),float(picked['latitude']))
        distanceToPark = haversine(myLoc,parkLoc)
        return statement("I've picked %s, it's %s.1f %s away and %s require a fee",picked['name'],distanceToPark,session.attributes['units'],"does" if picked['fee']>0 else "doesn't")
#walking distance
    session.attributes['de'] = Decision in yesses
    session.attributes['d'] = 2000
    return statement(endresult(fee,dist))

        



@ask.intent('RandomTripDistFloat',convert={'MaxDistInt':int,'MaxDistDec':int})
def randTripDistFloat(MaxDistInt,MaxDistDec,Units):
    if 'de' not in session.attributes:
        session.attributes['de'] = False
    if 'fe' not in session.attributes:
        session.attributes['fe'] = False
    if 'd' not in session.attributes:
        session.attributes['d'] = 9999999
    if 'f' not in session.attributes:
        session.attributes['f'] = None
    if 'units' not in session.attributes:
        session.attributes['units'] = Units
    MaxDist = MaxDistInt + MaxDistDec/10.0
    reallength = 0.0 + MaxDist
    if Units.lower() in ["kilometers","miles","yards","feet"]:
        #convert to metres
        if Units.lower() == "kilometers":
            reallength = MaxDist*1000
        if Units.lower() == "miles":
            reallength = MaxDist*1609.344
        if Units.lower() == "yards":
            reallength = MaxDist*0.9144
        if Units.lower() == "feet":
            reallength = MaxDist*0.3048
    session.attributes['d'] = min(reallength,session.attributes['d'])
    session.attributes['de'] = True
    if session.attributes['fe']:
        return statement(endresult(session.attributes['f'],session.attrubutes['d']))
    return question("Will you pay?")

@ask.intent('RandomTripDistFraction', convert ={'MaxDistInt':int})
def randTripDistFract(MaxDistInt,MaxDistFraction,Units):
    if 'de' not in session.attributes:
        session.attributes['de'] = False
    if 'fe' not in session.attributes:
        session.attributes['fe'] = False
    if 'd' not in session.attributes:
        session.attributes['d'] = 9999999
    if 'f' not in session.attributes:
        session.attributes['f'] = None
    if 'units' not in session.attributes:
        session.attributes['units'] = Units
    if MaxDistFraction in fractions:
        realFraction = fractions[MaxDistFraction]
    else:
        realFraction = 0

    MaxDist = MaxDistInt + realFraction
    reallength = 0.0 + MaxDist
    if Units.lower() in ["kilometers","miles","yards","feet"]:
        #convert to metres
        if Units.lower() == "kilometers":
            reallength = MaxDist*1000
        if Units.lower() == "miles":
            reallength = MaxDist*1609.344
        if Units.lower() == "yards":
            reallength = MaxDist*0.9144
        if Units.lower() == "feet":
            reallength = MaxDist*0.3048
    session.attributes['d'] = min(reallength,session.attributes['d'])
    session.attributes['de'] = True
    if session.attributes['fe']:
        return statement(endresult(session.attributes['f'],session.attrubutes['d']))
    return question("Will you pay xd?")


@ask.intent('RandomTripDist', convert ={'MaxDistInt':int})
def randTripDist(MaxDistInt,Units):
    if 'de' not in session.attributes:
        session.attributes['de'] = False
    if 'fe' not in session.attributes:
        session.attributes['fe'] = False
    if 'd' not in session.attributes:
        session.attributes['d'] = 9999999
    if 'f' not in session.attributes:
        session.attributes['f'] = None
    if 'units' not in session.attributes:
        session.attributes['units'] = Units
    reallength = 0.0 + MaxDistInt
    MaxDist = MaxDistInt
    if Units.lower() in ["kilometers","miles","yards","feet"]:
        #convert to metres
        if Units.lower() == "kilometers":
            reallength = MaxDist*1000
        if Units.lower() == "miles":
            reallength = MaxDist*1609.344
        if Units.lower() == "yards":
            reallength = MaxDist*0.9144
        if Units.lower() == "feet":
            reallength = MaxDist*0.3048
    session.attributes['d'] = min(reallength,session.attributes['d'])
    session.attributes['de'] = True
    if session.attributes['fe']:
        return statement(endresult(session.attributes['f'],session.attrubutes['d']))
    return question("Will you pay?")
    
@ask.intent('RandomTripFee')
def randTripFee(Fee):
    checkVal = Fee in yesses
    if 'de' not in session.attributes:
        session.attributes['de'] = False
    if 'fe' not in session.attributes:
        session.attributes['fe'] = False
    if 'd' not in session.attributes:
        session.attributes['d'] = 9999999
    if 'f' not in session.attributes:
        session.attributes['f'] = None
    session.attributes['fe'] = True
    session.attributes['f'] = checkVal
    if session.attributes['de']:
        return statement(endresult(session.attributes['f'],session.attributes['d']))
    return question("How far?")

if __name__ == '__main__':
    app.run()
