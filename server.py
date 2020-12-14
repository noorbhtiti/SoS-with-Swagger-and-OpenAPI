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


class getByCity(Resource):
    def get(self):
        city = str(request.args.get('city'))
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + apikey).read()
        list_of_data = json.loads(source)
        tempinc = ((list_of_data['main']['temp']) - 273.15)
        temp = ("%.2f" % tempinc)
        # data for variable list_of_data
        data = {
            "name": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(temp) + 'c',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        return data


api.add_resource(getByCity, '/')

if __name__ == '__main__':
    app.run(debug=True)