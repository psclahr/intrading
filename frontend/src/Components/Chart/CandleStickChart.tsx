import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Chart from 'react-apexcharts'
import { ApexOptions } from 'apexcharts'
import { Candlestick } from '../../../interfaces/Candlestick'

const CandleStickChart: React.FC = () => {
    const [options, setOptions] = useState<ApexOptions>({
        chart: {
            id: "candlestick-bar"
        },
        xaxis: {
            categories: []
        }
    })

    const [series, setSeries] = useState([{data: []}])

    useEffect(() => {
        axios.get('http://localhost:8000/api/historical/dax')
            .then(response => response.data)
            .then(data => data.map((candlestick: Candlestick) => [candlestick.date, candlestick.open, candlestick.high, candlestick.low, candlestick.close]))
            .then(candlesticks => setSeries([{data: candlesticks}]))
    }, []);

    return (
        <Chart
            series={series}
            options={options}
            type={'candlestick'}
            width={'1000px'}
        />
    )
}

export default CandleStickChart
