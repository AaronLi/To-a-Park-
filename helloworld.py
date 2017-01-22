from flask import Flask
from flask_ask import Ask, statement
from getData import getData
from urllib.request import urlopen
url = urlopen("https://data.michigan.gov/OData.svc/aiht-57sm")
tripInfo = getData(url)
app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello():
    #speech_text = "Hello %s" % firstname
    #return statement(speech_text).simple_card('Hello', speech_text)
    return statement("Minya so short")
@ask.intent('RandomTrip')
def randTrip():
    return statement("Trip placeholder")
@ask.intent('RandomTripDist', convert={'MaxDist':int})
def randTripDist(maxDist):
    return statement(str(maxDist))
@ask.intent('RandomCalc')
def randCalc():
    return statement("Albert and Aaron don't understand the greatest of my waifus")
if __name__ == '__main__':
    app.run()
