from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flasgger import *
from flask_cors import CORS, cross_origin
# import json to load JSON data to a python dictionary
import json
import requests

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


class API2(Resource):
    @cross_origin()
    def get(self):
        """API2
       Make F to C
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
                            "temp": "1.00",
                            "country": "SE",
                            "name": "Lulea"
                     }
                 """

        city = str(request.args.get('city'))  ## /?city=stockholm
        source = urllib.request.urlopen('http://127.0.0.1:8080/?city=' + city).read()
        list_of_data = json.loads(source)
        print(list_of_data)
        tempinc = ((list_of_data['main']['temp']) - 273.15)
        temp = ("%.2f" % tempinc)
        data = {"name": (str(list_of_data['name'])),
                "country": (str(list_of_data['sys']['country'])),
                "temp": str(temp)}
        return data


    def post(self):
        """send Data to API1
       ---
       responses:
         200:
           description: successful sending the weather
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
                            "temp": "1.00",
                            "country": "SE",
                            "name": "Lulea"
                     }
                 """
        return


api.add_resource(API2, '/')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)
