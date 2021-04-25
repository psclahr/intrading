import axios from 'axios'
import './App.css';

function App() {
    const fetchSomeData = () => {
        axios.get('http://localhost:8000/api/historical/dax').then(response => console.log(response))
        axios.get('http://localhost:8000/api/historical/dax/recognition').then(response => console.log(response))
    }

    fetchSomeData()

    return (
        <div className="App">
        <header className="App-header">
            React App
        </header>
        </div>
    );
}

export default App;
