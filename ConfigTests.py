import json
import urllib.request

def TestTags(city,tags):
	# TestTags(string,array)
	#
	# iterates through tags in array and see if the tags match pulled data
	# if tag is not found on surface level in json it tests explicit nested tags
	source = urllib.request.urlopen('http://127.0.0.1:8080/?city=' + city).read()
	data = json.loads(source)
	for i in range(len(tags)):
		print("testing tag " + tags[i]+"...")
		if tags[i] not in data:
			if tags[i] not in data['main']:
				if tags[i] not in data['sys']:
					raise ValueError(tags[i] + " is not in the resulting data!")
	print("All tags match in data. Compability OK")


# example
taglist = ['name','timezone','temp']
TestTags('Oslo',taglist)