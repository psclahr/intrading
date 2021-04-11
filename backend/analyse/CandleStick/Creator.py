from backend.analyse.enums.Course import Course
from backend.analyse.enums.Balance import Balance
from backend.analyse.enums.CandleStickProp import CandleStickProp
from backend.analyse.enums.CandleStickComparison import CandleStickComparison

class Creator:
    def __init__(self):
        self.dayCourse = {}

    def __getTotalLength(self) -> float:
        return self.dayCourse[Course.HIGH.value] - self.dayCourse[Course.LOW.value]

    def __getBodySize(self) -> float:
        return self.dayCourse[Course.CLOSE.value] - self.dayCourse[Course.OPEN.value]

    def __getTransformedBodySize(self) -> float:
        bodySize = self.__getBodySize()

        return abs(bodySize)

    def __getBalance(self) -> str:
        difference = self.__getBodySize()

        return Balance.POSITIVE.value if difference > 0 else Balance.NEGATIVE.value

    def __getUpperWickLength(self) -> float:
        upperBodyValue = self.dayCourse[Course.CLOSE.value] if self.__getBalance() == Balance.POSITIVE.value else self.dayCourse[Course.OPEN.value]

        return self.dayCourse[Course.HIGH.value] - upperBodyValue

    def __getLowerWickLength(self) -> float:
        lowerBodyValue = self.dayCourse[Course.OPEN.value] if self.__getBalance() == Balance.POSITIVE.value else self.dayCourse[Course.CLOSE.value]

        return lowerBodyValue - self.dayCourse[Course.LOW.value]

    def __getAbsoluteCandleStickCriteria(self) -> dict:
        return {
            CandleStickProp.TOTAL_LENGTH.value: self.__getTotalLength(),
            CandleStickProp.BODY_SIZE.value: self.__getTransformedBodySize(),
            CandleStickProp.BALANCE.value: self.__getBalance(),
            CandleStickProp.UPPER_WICK_LENGTH.value: self.__getUpperWickLength(),
            CandleStickProp.LOWER_WICK_LENGTH.value: self.__getLowerWickLength()
        }

    def getRelativeCandleStickCriteria(self, dayCourse) -> dict:
        self.dayCourse = dayCourse
        absoluteCandleStickValues = self.__getAbsoluteCandleStickCriteria()

        bodySizePercentage = absoluteCandleStickValues[CandleStickProp.BODY_SIZE.value] / absoluteCandleStickValues[CandleStickProp.TOTAL_LENGTH.value]
        upperWickPercentage = absoluteCandleStickValues[CandleStickProp.UPPER_WICK_LENGTH.value] / absoluteCandleStickValues[CandleStickProp.TOTAL_LENGTH.value]
        lowerWickPercentage = absoluteCandleStickValues[CandleStickProp.LOWER_WICK_LENGTH.value] / absoluteCandleStickValues[CandleStickProp.TOTAL_LENGTH.value]

        return {
            CandleStickComparison.BODY_SIZE_PERCENTAGE.value: bodySizePercentage,
            CandleStickComparison.UPPER_WICK_PERCENTAGE.value: upperWickPercentage,
            CandleStickComparison.LOWER_WICK_PERCENTAGE.value: lowerWickPercentage
        }
