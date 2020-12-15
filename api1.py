from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flasgger import *
# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

app = Flask(__name__)
api = Api(app)
swag = Swagger(app)

app.config['SWAGGER'] = {
    'title': 'Flasgger RESTful',
    'uiversion': 2
}

apikey = 'e8e4ff8f8290aee90e6800ec0eeb245f'


class API3(Resource):
    def get(self):
        """test
       It works also with swag_from, schemas and spec_dict
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
                            "temp":"1.00"
                     }
                 """

        city = str(request.args.get('city'))  ## /?city=stockholm
        source = urllib.request.urlopen('http://127.0.0.1:5050/?city=' + city).read()
        list_of_data = json.loads(source)
        print(list_of_data)
        tempinc = {"temp": str(list_of_data)}
        return tempinc


api.add_resource(API3, '/')

if __name__ == '__main__':
    app.run(debug=True)
