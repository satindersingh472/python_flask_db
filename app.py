from distutils.log import debug
from dbhelpers import conn_exe_close
from flask import Flask
import json

app = Flask(__name__)

def display_cars(cars):
        cars_available = []
        for car in cars:
            cars_available.append(car)
        return cars_available
        


@app.get('/all_cars')
def all_cars():
    results = conn_exe_close('call all_cars()',[])
    if(type(results) == list):
        result = display_cars(results)
        cars_json = json.dumps(result, default=str)
        return cars_json
    else:
        return 'Sorry, there was an error. please try again'

app.run(debug=True)