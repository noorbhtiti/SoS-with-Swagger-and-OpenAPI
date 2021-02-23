import json
import urllib.request


def TestTags(city, tags, api):
    # TestTags(string,array,URL)
    #
    # iterates through tags in array and see if the tags match pulled data
    # if tag is not found on surface level in json it tests explicit nested tags
    source = urllib.request.urlopen(api + '?city=' + city).read()
    data = json.loads(source)
    for i in range(len(tags)):
        print("testing tag " + tags[i] + "...")
        if tags[i] not in data:
            if "main" in data and tags[i] not in data['main']:
                if 'sys' in data and tags[i] not in data['sys']:
                    raise ValueError(tags[i] + " is not in the resulting data!")
    print("All tags match in data. Compability OK")


# example
api3 = 'http://127.0.0.1:8080/'
taglist = ['name', 'timezone', 'temp']
TestTags('Oslo', taglist, api3)
