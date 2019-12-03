import os

from flask import Flask, session, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

""" # Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
 """
@app.route("/")
def index():
    """ #Session close
    session.pop('user', None) """
    return render_template("index.html")

@socketio.on("send message")
def message(data):
    individual_message=data["individual_message"]
    emit("messages", {"individual_message": individual_message}, broadcast=True)

