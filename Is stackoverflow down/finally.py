import requests
from flask import Flask
import json
app = Flask(__name__)


@app.route("/")
def index():
    check = requests.get("https://stackoverflow.com")
    stat = check.status_code
    return f'<link type="text/css" rel="stylesheet" href="static/styles.css"><title>Stackoverflow status</title><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Stack_Overflow_icon.svg/769px-Stack_Overflow_icon.svg.png" width="500px" height="500px"><p>Stackoverflow Status is</p><h1>{stat}</h1>'
