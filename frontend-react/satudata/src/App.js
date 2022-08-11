import './App.css';
import Name from './Components/Name';
import Example from './Components/Example';
import Example2 from './Components/Example2';
import Form from './Components/Form';

function App() {
  return (
    <div className="container">
      <Name />
      <Example nama={['Python', 'Java', 'JavaScript', 'C++']} />
      <Example2 nama={['React', 'Django']} />
      <Form />
    </div>
  );
}

export default App;
