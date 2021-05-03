import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Chart from 'react-apexcharts'
import { ApexOptions } from 'apexcharts'
import { Candlestick } from '../../../interfaces/Candlestick'
import { CardContent, makeStyles, Typography } from '@material-ui/core'
import Box from '../UI/Box'
import { Annotation } from 'highcharts'
import { Recognition } from '../../../interfaces/Recognition'

const useStyles = makeStyles(() => ({
    nav: {
        display: 'flex',
        justifyContent: 'center',
    },
    header: {
        margin: '1rem'
    }
}))

const CandleStickChart: React.FC = () => {
    const classes = useStyles()

    const [options, setOptions] = useState<ApexOptions>({
        chart: {
            id: "candlestick-bar",
            toolbar: {
                tools: {
                    download: false,
                }
            },
            zoom: {
                enabled: true,
            }
        },
        xaxis: {
            categories: []
        },
        annotations: {
            xaxis: [
                {
                    x: '2017-11-14',
                    borderColor: '#775DD0',
                    label: {
                        style: {
                            color: '#fff',
                            background: "#775DD0"
                        },
                        text: 'Inverted Hammer',
                    }
                }
            ]
        }
    })

    const [series, setSeries] = useState([{
        data: [],
    }])

    const [recognitions, setRecognitions] = useState([])

    useEffect(() => {
        axios.get('http://localhost:8000/api/historical/dax')
            .then(response => response.data)
            .then(data => data.map((candlestick: Candlestick) => ({
                x: candlestick.date,
                y: [candlestick.open, candlestick.high, candlestick.low, candlestick.close]
            })))
            .then(candlesticks => setSeries([{data: candlesticks}]))

        axios.get('http://localhost:8000/api/historical/dax/recognition')
            .then(response => setRecognitions(response.data))
            .then(() => setOptions({
                annotations: {
                    xaxis: recognitions.map((recognition: Recognition) => ({
                        x: recognition.date,
                        borderColor: '#775DD0',
                        label: {
                            style: {
                                color: '#fff',
                                background: "#775DD0"
                            },
                            text: recognition.name,
                        }
                    }))
                }
            }))
    }, []);

    return (
        <Box>
            <div className={classes.nav}>
                <Typography className={classes.header} variant={'h4'}>Dax</Typography>
            </div>
            <CardContent>
                <Chart
                    series={series}
                    options={options}
                    type={'candlestick'}
                />
            </CardContent>
        </Box>
    )
}

export default CandleStickChart
