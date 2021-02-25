import json
import urllib.request
from collections import defaultdict

def TestTags(api_req,api_target,context):
	# TestTags(api_URL_req,api_URL_test,get function context)
	#
	# pulls the tags (and interfaces) expected from api_req's target interfaces
	# then compares data from api_target and check if resulting tags match 
	
	apisource = urllib.request.urlopen(api_req).read()
	apidata = json.loads(apisource)
	
	print("aquiring interfacelist from api_req...")
	if_source = apidata['paths'].keys()
	interfaces = []
	for x in if_source:
		interfaces.append(x)
	print("success! the source api interfacelist is: ")
	print(interfaces)

	print("aquiring taglist from api_req...")
	tagssource = apidata['paths'][interfaces[0]]['get']['responses']['200']['content']['application/json']['examples']['0']['value'] #can use this for more test cases later
	tags = []
	for x in tagssource:
		tags.append(x)

	print("success! the source api taglist is: ")
	print(tags)
	print("testing compability with api_target data results...")

	source = urllib.request.urlopen(api_target+context).read()
	data = json.loads(source)
	for i in range(len(tags)):
		print("testing tag " + tags[i]+"...",end="")
		if tags[i] not in data:
			raise ValueError(tags[i] + " is not in the resulting data!")
		print("OK")
	print("all tags from api source match in data from target api. compability OK")

def TestParams(api_req,api_target):
	apisource = urllib.request.urlopen(api_req).read()
	apidata = json.loads(apisource)
	
	params = apidata['paths']['/']['get']['parameters'] #can use this for more test cases later
	print(params)
	if (params=='string'):
		print('expected input is string, testing api_target')
		source = urllib.request.urlopen(api_target+context).read()
		data = json.loads(source)
		print(data)

# example test: take expected tags from interface / in api1 and see if api3 results match
api1_doc = 'http://api.swaggerhub.com/apis/SoS_Temperature/API3/0.0.1'
api3_url = 'http://127.0.0.1:8080/'

TestTags(api1_doc,api3_url,'?city=Oslo')
#TestParams(api1_doc,api3_url)