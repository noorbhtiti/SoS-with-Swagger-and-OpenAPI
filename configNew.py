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
    def __init__(self, apiArr, api1DescAddress):
        self.requestError = False
        self.typeError = False
        self.semanticError = False
        self.uniError = False
        self.a1 = apiArr[0]
        self.a2 = apiArr[1]
        self.a3 = apiArr[2]
        self.api1DescAddress = api1DescAddress
        

    def testRequest(self, api1Address):
        
        app = Flask(__name__)

        with app.app_context():
            with app.test_request_context('http://127.0.0.1:5000/?city=lulea'):
                try:
                    self.a1.get(self)
                except urllib.error.URLError:
                    if(api1.request.args.get('city') == str):
                        self.typeError = True
                    else:    
                        self.requestError = True
                    
                    print("requestError: ", self.requestError, "typeError: ", self.typeError)

    def tagSearch(self, api1DescAddress):
        taglist = [['in'], ['name'], ['type'], ['example']]

        source = urllib.request.urlopen(api1DescAddress).read()
        data = json.loads(source)

        for x in range(len(taglist)):
            param = data['paths']['/']['get']['parameters'][0][taglist[x][0]]
            taglist[x].append(param)
        
        print(taglist)
        

def main():
    exec('api1')
    exec('api2')
    exec('api3')
    
    apiArr = [api1.API1, api2.API2, api3.API3]

    api1Address = 'http://127.0.0.1:5000'
    api1DescAddress = 'http://api.swaggerhub.com/apis/SoS_Temperature/API1/0.0.1'
    
    t = Testing(apiArr, api1DescAddress)

    t.testRequest(api1Address)
    t.tagSearch(api1DescAddress)

if __name__ == "__main__":
    main()