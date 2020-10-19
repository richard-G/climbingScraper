from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))

# https://stackoverflow.com/questions/39139165/running-simple-python-script-continuously-on-heroku
