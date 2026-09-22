# LIBRARIES
from flask import Flask
from flask import render_template

# MY LIBRARIES
from module import dbLogic
from module import dbConfig

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 5000

# GLAVNI ROUTE APLIKACIJE

@app.route("/", methods = ["GET", "POST"])
def index():
    data = {
        "uspeh" : False
    }
    data["uspeh"] = dbLogic.getAll()
    return render_template("index.html", podatki = data)


# ZAGON APLIKACIJE
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)