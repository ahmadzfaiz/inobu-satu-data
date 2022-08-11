import React, { Component } from 'react';

class Name extends Component {
  constructor() {
    super();
    this.state = {
      name: 'Ahmad Zaenun Faiz',
    };
  }

  clickedMe = () => {
    this.setState({
      name:
        this.state.name === 'Ahmad Zaenun Faiz'
          ? 'Cokorda Wisnu Wiratama'
          : 'Ahmad Zaenun Faiz',
    });
  };

  render() {
    return (
      <div>
        <h1 className="bg-primary text-white text-center">{this.state.name}</h1>
        <button className="btn btn-success" onClick={this.clickedMe}>
          Change Me
        </button>
      </div>
    );
  }
}

export default Name;
