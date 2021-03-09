import json
import urllib.request
import urllib.request

from flask import *

import api1
import api2
import api3


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


# def recursive(key, data, wantedTag):
# for key in data:
#    print(data[key])
#    print(len(data[key]))
#    if(len(data[key] != 0)



def func1(data, wantedTag):
    for key,value in data.items():
        
       # print (value)
        
        print (str(key)+'->'+str(value))
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


def func2(data, wantedTag, taglist):
    #global taglist2
    for key,value in data.items():
        if(str(key) == wantedTag):
            
            if(taglist[0] == str(wantedTag)):
                taglist.append(str(value))
                return
        #print (str(key)+'->'+str(value))
        if type(value) == type(dict()):
            func2(value, wantedTag, taglist)
            
        elif type(value) == type(list()):

            for val in value:

                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func2(val, wantedTag, taglist)

#taglist = [['in'], ['name'], ['type'], ['example'], ['temp']]


def func3(data, wantedTag):
    global taglist
    print("hallå")
    for key,value in data.items():
        print(key)
        if(str(key) == wantedTag):
            return True
            break
            
        else:
            for val in value:
                func3(val, wantedTag)
            

        


def tagSearch2(apiDescAddress, taglist2):
    
    source = urllib.request.urlopen(apiDescAddress).read()
    data = json.loads(source)
    func2(data, taglist2[0], taglist2)
    if(len(taglist2) > 1):
        return True
    else:
        return False

    

def main():
    exec('api1')
    exec('api2')
    exec('api3')

    apiArr = [api1.API1, api2.API2, api3.API3]

    api1Address = 'http://127.0.0.1:8080'
    api2DescAddress = 'https://api.swaggerhub.com/apis/SoS_Temperature/Api2/0.0.2'

    taglist2 = ['pressure']
    #taglist = tagSearch2(api1DescAddress, taglist)
    print(tagSearch2(api1Address, taglist2))

    
    print(taglist2)
   # t = Testing(apiArr, api1DescAddress)

# t = Testing(apiArr, api1DescAddress)

# t.testRequest(api1Address)

if __name__ == "__main__":
    main()
