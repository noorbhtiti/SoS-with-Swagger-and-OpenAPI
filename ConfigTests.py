import json
import urllib
import urllib.request
import requests
from collections import defaultdict
from configNew import *


def TestTags(api_req, api_target, context, tags):  # TestTags(api_req,api_target,TEMPLATE)

    if (len(api_target) < 1):
        print("No target url - canceling Tag test")
        return

    source = urllib.request.urlopen(api_target + context)
    data = json.load(source)

    leng = len(tags)
    for i in range(leng):
        print("(3.", end="")
        print(i, end="")
        print(") testing tag " + tags[i] + "...", end="")
        if (tags[i] in data):
            print("FOUND " + tags[i])
            leng = leng - 1

    if (leng != 0):
        print("not all tags found, incompatible")
    else:
        print("all tags found, compatible!")

    # for i in range(len(tags)):
    #    print("testing tag " + tags[i] + "...", end="")
    #    if func2(data,tags[i]):
    #        print("FOUND "+tags[i])
    #        leng = leng - 1
    # if (leng != 0):
    #    print("not all tags found, incompatible")
    # else:
    #    print("all tags found, compatible!")


def TestTags2(api_req, api_target, context, tags):  # TestTags(api_req,api_target,TEMPLATE)

    print("success! the source api taglist is: ")
    print(tags)

    source = urllib.request.urlopen(api_target + context).read()
    data = json.loads(source)
    for i in range(len(tags)):
        print("testing tag " + tags[i] + "...", end="")
        if tags[i] not in data:
            raise ValueError(tags[i] + " is not in the resulting data!")
        print("OK")
    print("all tags from api source match in data from target api. compability OK")


def TestParams(api_req, api_target, queryname):
    if ((len(api_target) < 1)):
        print("No target url - canceling Parameter test")
        return
    if ((len(api_req) < 1)):
        print("No document url - canceling Parameter test")
        return
    print("(2) testing if target query matches required type: " + queryname, end="")
    apisource = urllib.request.urlopen(api_req).read()
    apidata = json.loads(apisource)
    params = apidata['paths']['/']['get']['parameters'][0]['type']  # can use this for more test cases later
    if (params == 'string' and (type(queryname) is str)):
        print('.. compability OK')
        return True
    return False


# def TestConnection(api):
def TestConnection2(url):
    print("(1) ", end="")
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            print(url + " Works! ",end="")
            source = urllib.request.urlopen(url).read()
            try:
                data = json.loads(source)
                print("- data is Json")
            except:
                return print("- data is not Json!")
        else:
            print("Server " + url + " is down!")
            return
    except:
        return


def Testall():
    # read file
    # TestConnection()
    with open('api_template.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    # print(obj['apis'])
    #api1Address = 'http://127.0.0.1:8080'
    #taglist2 = ['temp']
    print("\n"+"(1) IS CONNECTION TEST, (2) IS PARAM TEST, (3) IS TAG FIND")
    for x in obj['apis']:
        print("\n")
        print("TESTING API #" + x)
        TestConnection2(obj['apis'][x]['url'])  
        TestParams(obj['apis'][x]['from'],obj['apis'][x]['from_url'],obj['apis'][x]['req_query_type'])
        #TestTags(obj['apis'][x]['from'], obj['apis'][x]['from_url'], '?city=Oslo', obj['apis'][x]['req_tags'])
        i, o = 0, 0
        while(i<len(obj['apis'][x]['req_tags'])):
            print("(3.", end="")
            print(i, end="")
            print(")"+obj['apis'][x]['req_tags'][i] + " = ",end="")
            array = [obj['apis'][x]['req_tags'][i]]
            res = tagSearch2(obj['apis'][x]['url'], array)
            print(res)
            if (res == False):
                o = 1
            i=i+1
        if(o>0):
            print("not all tags found, incompatible")



# example test: Load from template,
# no from_url in api3 since need api key for "https://api.openweathermap.org/data/2.5/weather/"

#print(tagSearch2('http://127.0.0.1:5050/',['xvgwre']))
Testall()
# TestTags(api1_doc, api3_url, '?city=Oslo')
# TestTags(api1_doc,api3_url,TEMPLATE)
#url1 = "http://127.0.0.1:5000/"
#TestConnection2(url1)
