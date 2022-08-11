import React from 'react';

function Hello(props) {
  function clickMe() {
    alert('I was born in 18 August 1995');
  }

  return (
    <div>
      <h1>
        My Name is {props.firstName} {props.middleName} {props.lastName}
      </h1>
      <button className="btn btn-success" onClick={clickMe}>
        Click Me
      </button>
    </div>
  );
}

export default Hello;
