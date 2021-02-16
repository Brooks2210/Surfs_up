# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello world'
# Add these dependencies to the top of your app.py file.
import datetime as dt
import numpy as np
import pandas as pd
# Add the SQLAlchemy dependencies after the other dependencies you already imported in app.py.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# add the code to import the dependencies that we need for Flask
from flask import Flask, jsonify
# Access the SQLite database.
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
# Add the following code to reflect the database:
Base.prepare(engine, reflect=True)
# We'll create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station
# create a session link from Python to our database with the following code:
session = Session(engine)
# To define our Flask app, add the following line of code. 
# This will create a Flask application called "app."
app = Flask(__name__)
# We can define the welcome route using the code below:
@app.route('/')
# Now our root, or welcome route, is set up. The next step is to add the routing information 
# for each of the other routes. For this we'll create a function, and our return statement 
# will have f-strings as a reference to all of the other routes. This will ensure our 
# investors know where to go to view the results of our data.

# First, create a function welcome() with a return statement. 
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this 
# module into our return statement. We'll use f-strings to display them for our investors:

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")    
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)