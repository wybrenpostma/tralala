from webbrowser import get
from flask import Flask
from bestand1 import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/2")
def hello_world2():
    a = 1
    b = 2
    return f'hello, addition is {a+b}</p>'

@app.route("/twee/<getal>")
def hello_world3(getal):
    var1 = int(getal)
    var2 = var1 + var1
    return f'Dit is een hele andere {str(var2)} functie</p>'

@app.route("/vierde")
def hello_world4():
    return heleanderemethode()

