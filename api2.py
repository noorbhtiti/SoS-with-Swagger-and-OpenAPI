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


class API2(Resource):
    def get(self):
        city = str(request.args.get('city'))  ## /?city=stockholm
        source = urllib.request.urlopen('http://127.0.0.1:8080/?city=' + city).read()
        list_of_data = json.loads(source)
        print(list_of_data)
        tempinc = ((list_of_data['main']['temp']) - 273.15)
        temp = ("%.2f" % tempinc)
        return temp


api.add_resource(API2, '/')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)
