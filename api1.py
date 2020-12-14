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


@app.route("/<city>")
def api1(city):
    # city = str(request.args.get('city'))
    source = urllib.request.urlopen('http://127.0.0.1:5050/' + city).read()
    temp = json.loads(source)
    slut = {"temp":str(temp)}
    return slut


if __name__ == '__main__':
    app.run(debug=True)
