from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello():
    #speech_text = "Hello %s" % firstname
    #return statement(speech_text).simple_card('Hello', speech_text)
    return statement("Minya so short")

if __name__ == '__main__':
    app.run()
