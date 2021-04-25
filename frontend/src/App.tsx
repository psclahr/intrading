import React from 'react'
import CandleStickChart from './Components/Chart/CandleStickChart'
import './App.css';

const App: React.FC = () => {
    return (
        <div className={'App'}>
            <header className={"App-header"}>
                <CandleStickChart />
            </header>
        </div>
    )
}

export default App
