import React, { Component } from 'react';
import './App.css'
import SwaggerUI from 'swagger-ui';
import Config from './organization_config.json'; //not needed???
import Sidebar from './Sidebar.js'
import '../node_modules/swagger-ui/dist/swagger-ui.css'

class App extends Component {
  constructor(props) {
    super(props);
    let apis = ['Swagger Petstore', 'Simple Inventory API', 'Test REST API'];
    this.state = {
      organizationConfig: null,
      definitionList: null,
      definitionLink: "http://127.0.0.1:5000/apispec_1.json",
    }
    this.swaggerhub = this.swaggerhub.bind(this)
    this.getOrganizationData = this.getOrganizationData.bind(this)
  }

  componentDidMount() {
    SwaggerUI({
      domNode: document.getElementById("api-data"),
      url: this.state.definitionLink
    })
  }

  render() {
    return (
      <div className="App">
        <Sidebar 
          organizationConfig={this.state.organizationConfig}
          definitionList={this.state.definitionList}
          getOrganizationData={this.getOrganizationData}
        />
        <div id="api-data" />
      </div>
    );
  }
 
	swaggerhub(inputMethod, inputResource, inputParams) { //NOT NEEDED??? pull from swaggerhub
	  let url = ""
	  if (inputParams) {
		  url = "https://api.swaggerhub.com/apis/" + inputResource + "?" + inputParams
	  } else {
		  url = "https://api.swaggerhub.com/apis/" + inputResource
	  }
	  
	  return fetch(url, {
		  method: inputMethod
	  }).then(response => {
		if (response.ok) {
		  return response.json()
		} throw new Error('There was an issue requesting the API')
	  }).then(json => {
		  return json
	  })
  }
  getOrganizationData(organization) { //NOT NEEDED? Formatation for swaggerhub
    let inputParams = "page=0&limit=20&sort=NAME&order=ASC"
    let inputResource = organization;
  
    this.swaggerhub('GET', inputResource, inputParams).then(response => {
      this.setState({
        definitionList: response.apis
      })
    })
  }
  componentWillMount() { //for config mount?? NOT NEEDED???
    this.setState({
      organizationConfig:  Config.orgData,
    })
  }

  updateDefinitionLink(newLink) { //For api links
    this.setState({
      definitionLink: newLink
    })
  }
}

export default App;