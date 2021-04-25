from backend.analyse.courses.fetcher import Fetcher
from backend.analyse.courses.chartGetter import ChartGetter
from backend.analyse.courses.chartTransformer import ChartTransformer
from backend.analyse.candleStick.recognizer import Recognizer

class ChartRepository():
    def __init__(self):
            self.fetcher = Fetcher()
            self.chartTransformer = ChartTransformer()

    def __getTransformedData(self, name: str) -> dict:
        fetchedData = self.fetcher.getChart(name)
        chartGetter = ChartGetter(fetchedData)

        return self.chartTransformer.transform(chartGetter.timeStamps(), chartGetter.openCourses(), chartGetter.closeCourses(), chartGetter.highCourses(), chartGetter.lowCourses())

    def getHistoricalDax(self) -> dict:
        return self.__getTransformedData('dax')

    def getHistoricalDaxRecognition(self) -> dict:
        data = self.__getTransformedData('dax')
        filteredData = list(filter(lambda day: day['open'] is not None , data))
        recognizer = Recognizer(filteredData)

        return recognizer.recognize()