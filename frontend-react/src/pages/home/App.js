import { useNavigate } from 'react-router-dom';
import './App.css';

function App() {
  const navigate = useNavigate();

  const LoginNavigate = () => {
    navigate('/login');
  };

  return (
    <div className="App">
      <div className="row App-header g-0">
        <div className="col-11">
          <br />
          <button className="btn btn-primary float-end" onClick={LoginNavigate}>
            Login
          </button>
          <br />
        </div>
        <div className="col-1"></div>
      </div>
      <div className="row App-break g-0"></div>
      <div className="row App-body g-0">
        <div className="col">
          <img
            src="https://inobu.org/wp-content/uploads/2020/02/INOBU-FINAL-768x255.png"
            width="500"
          ></img>
          <br />
          <br />
          <h2>Selamat Datang di</h2>
          <h1 style={{ fontSize: '6rem' }}>Inobu Satu Data</h1>
          <br />
          <br />
          <p>
            Aplikasi berbasis web untuk penyimpanan dan manajemen data di
            Yayasan Inobu
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
