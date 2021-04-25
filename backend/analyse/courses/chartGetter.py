class ChartGetter:
    def __init__(self, data: list):
        self.data = data

    # Getters for actual Chart
    def __getActualFirstResult(self) -> dict:
        return self.data['quoteResponse']['result'][0]

    def actualHigh(self) -> float:
        result = self.__getActualFirstResult()

        return result['regularMarketDayHigh']

    def actualLow(self) -> float:
        result = self.__getActualFirstResult()

        return result['regularMarketDayLow']

    # Getters for historical Chart
    def __getHistoricalFirstResult(self) -> dict:
        return self.data['chart']['result'][0]

    def __getHistoricalFirstQuote(self) ->dict:
        result = self.__getHistoricalFirstResult()

        return result['indicators']['quote'][0]

    def __getQuotes(self, typo: str) -> list:
        quote = self.__getHistoricalFirstQuote()

        return quote[typo]

    def timeStamps(self) -> list:
        result = self.__getHistoricalFirstResult()

        return result['timestamp']

    def openCourses(self) -> list:
        return self.__getQuotes('open')

    def closeCourses(self) -> list:
        return self.__getQuotes('close')

    def highCourses(self) -> list:
        return self.__getQuotes('high')

    def lowCourses(self) -> list:
        return self.__getQuotes('low')
