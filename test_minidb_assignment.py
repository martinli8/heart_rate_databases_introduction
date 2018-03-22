from main import *
import pytest


def test_print_user():
    testEmail = "thisIsATest@gmail.com"
    age = 21
    heart_rate = [120, 121]
    u = models.User(testEmail, age, heart_rate,
                    [datetime.datetime.now(), datetime.datetime.now()])
    u.save()

    testUserData = {
        "All heart rate measurements": heart_rate
    }

    assert testUserData == print_user(testEmail)

    testEmail = "thisIsATest@gmail.com"
    age = 21
    heart_rate = [124, 129]
    u = models.User(testEmail, age, heart_rate,
                    [datetime.datetime.now(), datetime.datetime.now()])
    u.save()

    testUserData = {
        "All heart rate measurements": heart_rate
    }

    assert testUserData == print_user(testEmail)

    
