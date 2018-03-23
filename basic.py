import datetime
import models
from flask import Flask, jsonify, request
from main import *
app = Flask(__name__)


@app.route("/api/heart_rate", methods=["POST"])
def userCreation():
    r = request.get_json()
    try:
        user_email = r["user_email"]
        user_age = r["user_age"]
        heart_rate = r["heart_rate"]
    except:
        return 'Input data error! Make sure you have the correct fields', 400
    if not isinstance(user_email, str):
        return "Email input is not a string", 400
    if not isinstance(user_age, int):
        return "User age is not an int", 400
    if heart_rate is str:
        return "Heart rate is a str! Please input a numerical", 400

    try:
        add_heart_rate(user_email, heart_rate, time=datetime.datetime.now())
    except:
        create_user(user_email, user_age, heart_rate,
                    time=datetime.datetime.now())
        return 'User is created'
    return 'User already exists, data is appended'


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getInfo(user_email):
    userJson = print_user(user_email)
    return jsonify(userJson)


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def averageHR(user_email):
    hrAvg = average_HR_Calc(user_email)
    averageHRJson = {
        "Average HR": hrAvg
    }
    return jsonify(averageHRJson)


@app.route("/api/heart_rate/interval_average", methods=['POST'])
def interval_average():
    r = request.get_json()

    try:
        user_email = r["user_email"]
        time = r["heart_rate_average_since"]
    except:
        return 'Input data error! Make sure you have the correct fields', 400
    if not isinstance(user_email, str):
        return "Email input is not a string", 400
    try:
        datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
    except:
        return "invalid input time format!", 400

    try:
        hrAvg = interval_HR_calc(user_email, time)
        tachycardiaStatus = check_tachycardia(user_email, hrAvg)
        averageHrJson = {
            "average hr since specified time": hrAvg,
            "Tachycardia status": tachycardiaStatus
        }
        return jsonify(averageHrJson)
    except:
        print("No user exists or no data points after that time!")
        return "No user exists or no data points after that time", 400

    return 'you goofed, likely error in input data'
