import React, { Component } from 'react';

class Form extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: '',
      password: '',
    };
  }

  usernameChange = (e) => {
    this.setState({
      username: e.target.value,
    });
  };

  passwordChange = (e) => {
    this.setState({
      password: e.target.value,
    });
  };

  render() {
    return (
      <div className="container">
        <input
          type="text"
          placeholder="Insert Your Username"
          className="form-control"
          value={this.state.username}
          onChange={this.usernameChange}
        ></input>
        <input
          type="password"
          placeholder="Insert Your Password"
          className="form-control"
          value={this.state.password}
          onChange={this.passwordChange}
        ></input>
        <button className="btn btn-primary">Submit</button>
      </div>
    );
  }
}

export default Form;
