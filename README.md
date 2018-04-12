# heart_rate_databases_starter


[![Build Status](https://travis-ci.org/martinli8/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/martinli8/heart_rate_databases_introduction)


This is a heart rate database where a user can store various heart rate by using a web server, by establishing a Username with an email, and also a specific heart rate. If the user does not exist already, a new user will be created. If a user already exists, the data will be appended to existing data. Furthermore, one can also ask for the average heart rate, as well as printing the user data with all the heart rates, as well as checking the heart rate across a specific interval. If obtaining HR measurements across a certain interval, whether or not the user is tachycardic will also be displayed.

To get started with how to use this, you need to get the mongo db program running first. Simply run
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```

on your local machine.

eyes: if you are running your mongodb database on a virtual machine, you need to replace the `connect` URI string in `main.py`. Replace `localhost` with a VM address, like so:

```
connect("mongodb://vcm-0000.vm.duke.edu:27017/heart_rate_app") # open up connection to db
```

once your database is running and your connection string is set, you can run the webserver by running `basic.py` after activating your `virtualenv` and installing all the dependencies listed in `requirements.txt`.

```
FLASK_APP=basic.py flask run
```
