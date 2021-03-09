import json
import urllib
import urllib.request
import requests
from collections import defaultdict


def TestTags(api_req, api_target, context, tags):  # TestTags(api_req,api_target,TEMPLATE)

    if (len(api_target) < 1):
        print("No target url - canceling Tag test")
        return

    source = urllib.request.urlopen(api_target + context)
    data = json.load(source)

    leng = len(tags)
    for i in range(leng):
        print("(2.", end="")
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
    print("(1) testing if target query matches required type: " + queryname, end="")
    apisource = urllib.request.urlopen(api_req).read()
    apidata = json.loads(apisource)
    params = apidata['paths']['/']['get']['parameters'][0]['type']  # can use this for more test cases later
    if (params == 'string' and (type(queryname) is str)):
        print('.. compability OK')
        return True
    return False


# def TestConnection(api):
def TestConnection2(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            print(url + " Works!")
            source = urllib.request.urlopen(url).read()
            try:
                data = json.loads(source)
                print("It is Json")
            except:
                return print("Not Json!")
        else:
            print("Server " + url + " is down")
            return
    except:
        print("Fel")


def Testall():
    # read file
    # TestConnection()
    with open('api_template.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    # print(obj['apis'])
    for x in obj['apis']:
        print("CURRENT API: " + x)
        # TestConnection(obj['apis'][x]['url'])
        # TestParams(obj['apis'][x]['from'],obj['apis'][x]['from_url'],obj['apis'][x]['req_query_type'])
        # TestTags(obj['apis'][x]['from'], obj['apis'][x]['from_url'], '?city=Oslo', obj['apis'][x]['req_tags'])

    # loop do testtag for each api


# example test: Load from template,
# no from_url in api3 since need api key for "https://api.openweathermap.org/data/2.5/weather/"


# Testall()
# TestTags(api1_doc, api3_url, '?city=Oslo')
# TestTags(api1_doc,api3_url,TEMPLATE)
url1 = "http://127.0.0.1:5000/"
TestConnection2(url1)
