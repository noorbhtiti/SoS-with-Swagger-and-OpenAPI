# SoS-with-Swagger-and-OpenAPI
Swagger/OpenAPI System and System of System compatibility

How To Use:

(1) Provide an JSON file describing the SoS as a .json format (see example api_template.json). You need to provide the URL's of the API's themselves, a link to their documentation and what required tags/parameters you need to check.

(2) Once you have a valid template run the file configTests.py. (might need to run in an virtual enviroment)

(3) For the GUI to work on your own originization you need to create a swaggerhub originization with multiple API's hosted on swaggerhub.com. Then you provide the name of this orginization in the file "organization_config.json". 

The result will connect the different requirements and check that they have valid data coming through according to your template.

The testing procedure is seen in the following activity diagram, and the structure of the project is shown in the class diagram.

![alt text](https://github.com/JunkZ/Project-g12/blob/master/Activity_diagram.png?raw=true)
![test2](https://github.com/JunkZ/Project-g12/blob/master/Class_diagram.png?raw=true)
