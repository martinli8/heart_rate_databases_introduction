from flask import Flask, jsonify, request
app = Flask(__name__)
from main import add_heart_rate
from main import create_user
from main import print_user
import datetime


@app.route("/api/heart_rate", methods=["POST"])
def userCreation():
    r = request.get_json()

    user_email = r["user_email"]
    user_age = r["user_age"]
    heart_rate = r["heart_rate"]

    try:
        add_heart_rate(user_email, heart_rate, time=datetime.datetime.now())
    except:
        create_user(user_email, user_age, heart_rate, time=datetime.datetime.now())
        return 'User is created'
    return 'User overlap detected, data is appended'

@app.route("/api/heart_rate/<user_email>", methods = ["GET"])
def getInfo(user_email):
    userJson = print_user(user_email)
    return jsonify(userJson)
