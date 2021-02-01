import json
import os
import lib2to3.fixes.fix_execfile
import urllib.request
import api1, api2, api3
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flasgger import *
from flask_cors import CORS, cross_origin
# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request

class Testing:
    def __init__(self):
        self.requestError = False
        self.typeError = False
        self.semanticError = False
        self.uniError = False
        

    def test(self, apiArr):
        a1 = apiArr[0]
        a2 = apiArr[1]
        a3 = apiArr[2]
        app = Flask(__name__)

        with app.app_context():
            with app.test_request_context('http://127.0.0.1:8080/?city=stockholm'):
                try:
                    a1.get(self)
                except urllib.error.URLError:
                    self.requestError = True
                    print("requestError =", self.requestError)

def main():
    
    
    exec('api1')
    exec('api2')
    exec('api3')
    
    apiArr = [api1.API1, api2.API2, api3.API3]

    t = Testing()

    t.test(apiArr)




if __name__ == "__main__":
    main()