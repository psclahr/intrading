import React from 'react'
import CandleStickChart from './Components/Chart/CandleStickChart'
import Wrapper from './Components/Wrapper/index'
import './App.css';

const App: React.FC = () => {
    return (
        <div className={'App'}>
            <Wrapper>
                <CandleStickChart/>
            </Wrapper>
        </div>
    )
}

export default App
