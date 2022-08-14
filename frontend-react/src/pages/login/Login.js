import './Login.css';
import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import LoginAPI from './LoginAPI';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useCookies(['mytoken']);
  let navigate = useNavigate();

  useEffect(() => {
    if (token['mytoken']) {
      navigate('/articles');
    }
  }, [token]);

  const loginButton = () => {
    LoginAPI.AddUser({ username, password })
      .then((resp) => setToken('mytoken', resp.token))
      .catch((error) => console.log(error));
  };

  return (
    <div className="Login-header">
      <br />
      <h1 className="Login">Please Login</h1>
      <div className="row g-0">
        <div className="col-1"></div>
        <div className="col-md-10">
          <div className="mb-3">
            <label htmlFor="username" className="form-label">
              Username
            </label>
            <input
              type="text"
              className="form-control"
              id="username"
              placeholder="Please enter username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            ></input>
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">
              Password
            </label>
            <input
              type="password"
              className="form-control"
              id="password"
              placeholder="Please enter password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            ></input>
          </div>
          <button className="btn btn-primary" onClick={loginButton}>
            Login
          </button>
        </div>
        <div className="col-1"></div>
      </div>
    </div>
  );
}

export default Login;
