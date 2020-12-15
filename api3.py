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
        city = str(request.args.get('city')) ## /?city=stockholm
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + apikey).read()
        list_of_data = json.loads(source)
        return list_of_data


api.add_resource(API3, '/')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
