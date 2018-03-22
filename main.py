from pymodm import connect
import models
import datetime
from pymodm import MongoModel,fields
connect("mongodb://localhost:27017/heart_rate_app")  # open up connection to db

def add_heart_rate(email, heart_rate, time):
    """
    Appends a heart_rate measurement at a specified time to the user specified by
    email. It is assumed that the user specified by email exists already.
    :param email: str email of the user
    :param heart_rate: number heart_rate measurement of the user
    :param time: the datetime of the heart_rate measurement
    """
    user = models.User.objects.raw({"_id": email}).first()  # Get the first user where _id=email
    user.heart_rate.append(heart_rate)  # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time)  # append the current time to the user's list of heart rate times
    user.save()  # save the user to the database


def create_user(email, age, heart_rate, time):
    import models
    """
    Creates a user with the specified email and age. If the user already exists in the DB this WILL
    overwrite that user. It also adds the specified heart_rate to the user
    :param email: str email of the new user
    :param age: number age of the new user
    :param heart_rate: number initial heart_rate of this new user
    :param time: datetime of the initial heart rate measurement
    """
    # primaryKeySearch = {
    #     "_id":email
    #     }
    # myGuy = models.User.objects.raw({"_id":email})
    #     raise ValueError("Already have an existing user with primary key")
    # if db.User.find(primaryKeySearch).limit(1) == True:
    #     raise ValueError("Already have an existing user with primary key")
    u = models.User(email, age, [], [])  # create a new User instance
    u.heart_rate.append(heart_rate)  # add initial heart rate
    u.heart_rate_times.append(time)  # add initial heart rate time
    u.save()  # save the user to the database


def print_user(email):
    """
    Prints the user with the specified email
    :param email: str email of the user of interest
    :return:
    """
    user = models.User.objects.raw({"_id": email}).first()  # Get the first user where _id=email
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)
    userData = {
    "All heart rate measurements": user.heart_rate,
    # "heart_rate_times": user.heart_rate_times
    }
    return userData
if __name__ == "__main__":
    create_user(email="suyash@suyashkumar.com", age=24, heart_rate=60, time=datetime.datetime.now())  # we should only do this once, otherwise will overwrite existing user
    add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    print_user("suyash@suyashkumar.com")
