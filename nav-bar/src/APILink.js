
import React from 'react';

const APILink = props => {
    let name = "Api1"
    let apiLink = "http://127.0.0.1:5000/apispec_1.json"

    function handleClick() {
      props.updateDefinitionLink(apiLink)
    }

  return (  
    <div className="api-link" onClick={() => handleClick()}>
      {name}
    </div>
  )
}

export default APILink;