from backend.analyse.courses.fetcher import Fetcher
from backend.analyse.courses.chartGetter import ChartGetter
from backend.analyse.courses.chartTransformer import ChartTransformer

class ChartRepository():
    def __init__(self):
            self.fetcher = Fetcher()
            self.chartTransformer = ChartTransformer()

    def getHistoricalDax(self):
        fetchedData = self.fetcher.getChart('dax')
        chartGetter = ChartGetter(fetchedData)

        return self.chartTransformer.transform(chartGetter.timeStamps(), chartGetter.openCourses(), chartGetter.closeCourses(), chartGetter.highCourses(), chartGetter.lowCourses())