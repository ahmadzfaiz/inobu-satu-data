import React, { Component } from 'react';

class MyClass extends Component {
  render() {
    return (
      <div>
        <h1 className="bg-primary text-white text-center">
          I am a {this.props.job}
        </h1>
        <button className="btn btn-primary" onClick={this.props.click}>
          Click my job
        </button>
      </div>
    );
  }
}

export default MyClass;
