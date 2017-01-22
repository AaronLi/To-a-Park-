from flask import Flask
from flask_ask import Ask, statement, question
from getData import *
from urllib.request import urlopen
import random
url = urlopen("https://data.michigan.gov/OData.svc/aiht-57sm")
tripInfo = getData(url)
app = Flask(__name__)
ask = Ask(app, '/')

#@ask.intent('HelloIntent')
#def hello():
    #speech_text = "Hello %s" % firstname
    #return statement(speech_text).simple_card('Hello', speech_text)
 #     return statement("Minya so short")
@ask.intent('RandomTrip')
def randTrip():
    return statement("")
@ask.intent('RandomTripDist', convert ={'MaxDist':float})
def randTripDist(MaxDist,Units):
    return statement(str(MaxDist)+" "+str(Units))
#@ask.intent('
if __name__ == '__main__':
    app.run()
