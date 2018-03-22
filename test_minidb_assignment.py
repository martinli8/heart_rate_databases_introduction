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
    u1 = models.User(testEmail, age, heart_rate,
                     [datetime.datetime.now(), datetime.datetime.now()])
    u1.save()

    testUserData1 = {
        "All heart rate measurements": heart_rate
    }

    assert testUserData1 == print_user(testEmail)

def test_create_user():
    testUser = "testUserEmail@email.com"
    age = 47
    heart_rate = 95
    timestamp = datetime.datetime(2018, 3, 22, 13, 39, 4, 847000)
    create_user(testUser,age,heart_rate,timestamp)

    user = models.User.objects.raw({"_id": "testUserEmail@email.com"}).first()

    assert user.email == testUser
    assert user.age == age
    assert user.heart_rate == [95]
    assert user.heart_rate_times == [datetime.datetime(2018,
                                    3, 22, 13, 39, 4, 847000)]

def test_append_data():
    testUser = "testUserEmail1@email.com"
    age = 47
    heart_rate = 95
    timestamp = datetime.datetime(2018, 3, 22, 13, 39, 4, 847000)
    heart_rate_append = 97
    timestamp_append = datetime.datetime(2018, 3, 22, 14, 49, 5, 947000)
    create_user(testUser,age,heart_rate,timestamp)
    add_heart_rate(testUser,heart_rate_append,timestamp_append)
    user = models.User.objects.raw({"_id": "testUserEmail1@email.com"}).first()

    assert user.email == testUser
    assert user.age == age
    assert user.heart_rate == [95,97]
    assert user.heart_rate_times == [datetime.datetime(2018, 3, 22, 13, 39, 4, 847000),
                                     datetime.datetime(2018, 3, 22, 14, 49, 5, 947000)]

# def test_average_hr
