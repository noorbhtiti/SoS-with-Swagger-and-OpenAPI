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

    def testRequest(self, api1Address):
        taglist = [['in'], ['name'], ['type'], ['example']]
        taglist = self.tagSearch(self.api1DescAddress, taglist)

        print(api1Address + '/' + taglist[0][1] + taglist[1][1] + '=' + taglist[3][1])

        app = Flask(__name__)

        with app.app_context():
            with app.test_request_context(api1Address + '/' + taglist[0][1] + taglist[1][1] + '=' + taglist[3][1]):
                try:
                    self.a1.get(self)
                except urllib.error.URLError:
                    self.requestError = True

                    print("requestError: ", self.requestError)

    def tagSearch(self, api1DescAddress, taglist):
        source = urllib.request.urlopen(api1DescAddress).read()
        data = json.loads(source)
        # print(data['paths']['/']['get']['parameters'][0])
        for x in range(len(taglist)):
            param = data['paths']['/']['get']['parameters'][0][taglist[x][0]]
            if (param == 'query'):
                taglist[x].append('?')
            else:
                taglist[x].append(param)
        return taglist


#def recursive(key, data, wantedTag):
    #for key in data:
    #    print(data[key])
    #    print(len(data[key]))
    #    if(len(data[key] != 0)
            

taglist = [['in'], ['name'], ['type'], ['example'], ['temp']]
def func1(data, wantedTag):
    for key,value in data.items():
        
       # print (value)
        
        #print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            return func1(value, wantedTag)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    return func1(val, wantedTag)


def func2(data, wantedTag):
    global taglist
    for key,value in data.items():
        if(str(key) == wantedTag):
            print("JAG ÄR HÄR")
            for i in range(len(taglist)):
                if(taglist[i][0] == str(wantedTag)):
                    taglist[i].append(str(value))
                    return
        #print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            func2(value, wantedTag)
            
        elif type(value) == type(list()):
            
            for val in value:
                
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func2(val, wantedTag)

def func3(data, wantedTag):
    for key,value in data.items():
        if(str(key) == str(wantedTag)):
            return str(value)
        if type(value) == type(dict()):
            if(str(key) == str(wantedTag)):
                return func3(value, wantedTag)
            else:
                func3(value, wantedTag)
            
        elif type(value) == type(list()):
            
            for val in value:
                
                if(str(key) == str(wantedTag)):
                        
                    return func3(val, wantedTag)
                else:
                        
                    func3(val, wantedTag)    


def tagSearch2(apiDescAddress, taglist):
    source = urllib.request.urlopen(apiDescAddress).read()
    data = json.loads(source)
    for i in range(len(taglist)):
        print((func3(data, taglist[i][0])))
 

def main():
    exec('api1')
    exec('api2')
    exec('api3')

    apiArr = [api1.API1, api2.API2, api3.API3]

    api1Address = 'http://127.0.0.1:5000'
    api2DescAddress = 'https://api.swaggerhub.com/apis/SoS_Temperature/Api2/0.0.2'

    global taglist
    #taglist = tagSearch2(api1DescAddress, taglist)
    tagSearch2(api2DescAddress, taglist)

    
    print(taglist)
   # t = Testing(apiArr, api1DescAddress)

# t = Testing(apiArr, api1DescAddress)

# t.testRequest(api1Address)

if __name__ == "__main__":
    main()
