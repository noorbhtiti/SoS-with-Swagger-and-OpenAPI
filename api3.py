from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flasgger import *
from flask_cors import CORS, cross_origin
# import json to load JSON data to a python dictionary
import json
# :)
# urllib.request to make a request to api
import urllib.request

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
swag = Swagger(app)

app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SWAGGER'] = {
    'title': 'Flasgger RESTful',
    'uiversion': 2
}

apikey = 'e8e4ff8f8290aee90e6800ec0eeb245f'


class API3(Resource):
    @cross_origin()
    def get(self):

        """API3
       Get weather from openWeather.
       ---
       parameters:
         - in: query
           name: city
           type: string
           required: true
           schema:
             type: string
           example: lulea
       responses:
         200:
           description: successful getting the weather
           content:
             application/json:
               schema:
                 type: object
                 properties:
                   temp:
                     type: string
               examples:
                 0:
                   value:
                     {
                             "base": "stations",
                              "clouds": {
                                "all": 74
                              },
                              "cod": 200,
                              "coord": {
                                "lat": 44.9331,
                                "lon": 7.5401
                              },
                              "dt": 1611077808,
                              "id": 3172215,
                              "main": {
                                "feels_like": 272.68,
                                "humidity": 57,
                                "pressure": 1023,
                                "temp": 275.58,
                                "temp_max": 277.59,
                                "temp_min": 273.71
                              },
                              "name": "None",
                              "sys": {
                                "country": "IT",
                                "id": 2008171,
                                "sunrise": 1611039698,
                                "sunset": 1611073149,
                                "type": 3
                              },
                              "timezone": 3600,
                              "visibility": 10000,
                              "weather": [
                                {
                                  "description": "broken clouds",
                                  "icon": "04n",
                                  "id": 803,
                                  "main": "Clouds"
                                }
                              ],
                              "wind": {
                                "deg": 327,
                                "speed": 0.38
                              }
                     }
                 """

        city = str(request.args.get('city')) ## /?city=stockholm
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + apikey).read()
        list_of_data = json.loads(source)
        return list_of_data


api.add_resource(API3, '/')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
