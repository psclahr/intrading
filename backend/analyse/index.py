from backend.analyse.bootstrap import bootstrap
from backend.analyse.Courses.dax.fetch import historicalDax
from backend.analyse.Courses.dax.fetch import historicalEuroDollar
from backend.analyse.Courses.dax.fetch import historicalBitcoinDollar
from backend.analyse.Courses.Chart import Chart
from backend.analyse.Courses.Transformer import Transformer
from backend.analyse.helper.visualize import visualizeData
from backend.analyse.CandleStick.Recognizer import Recognizer
from backend.analyse.CandleStick.Predicter import Predicter

import os

def start():
    bootstrap()

    fetchedData = historicalDax()

    chart = Chart(fetchedData)
    transformer = Transformer()

    data = transformer.transform(chart.timeStamps(), chart.openCourses(), chart.closeCourses(), chart.highCourses(), chart.lowCourses())

    visualizeData(data)

    filteredData = list(filter(lambda day: day['open'] is not None , data))

    candleStickRecognizer = Recognizer(filteredData)

    candleSticks = {}

    for index, day in enumerate(filteredData):
        result = candleStickRecognizer.whichCandleStick(index)

        if result is not None:
            name = result['name']
            index = result['index']

            if name in candleSticks:
                candleSticks[name].append(index)
            else:
                candleSticks[name] = [index]

    predicter = Predicter(filteredData)

    predictions = {}

    for candleStickName in candleSticks:
        prediction = predicter.predict(candleSticks[candleStickName])

        predictions[candleStickName] = prediction

    return predictions
