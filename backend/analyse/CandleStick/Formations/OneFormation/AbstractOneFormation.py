from abc import ABC, abstractmethod
import numpy as np
from sklearn.linear_model import LinearRegression
from backend.analyse.candleStick.creator import Creator
from backend.analyse.candleStick.limitValues import TREND, FORMATION_ACCORDANCE, PREVIOUS_COURSES_NUM

class AbstractOneFormation(ABC):
    def __init__(self, data: list):
        self.candleStickCreator = Creator()

        self.data = data
        self.limitValueTrend = TREND

    # Write test to check if sum of all percentages is 1
    # This is a case where a ML algorithm can be predict how a optimal template from each candlestick can look like
    @abstractmethod
    def _getTemplate(self) -> dict:
        pass

    @abstractmethod
    def _getPreviousDevelopmentRequirement(self, gradient) -> bool:
        pass

    @abstractmethod
    def _getPreviousCloseRequirement(self, previousClose: float, dayOpen: float) -> bool:
        pass

    def __getPreviousCourses(self, index: int) -> list:
        print(index)
        previousCourses = []
        previousIndex = 1

        while previousIndex <= PREVIOUS_COURSES_NUM:
            previousCourses.append(self.data[index - previousIndex]['close'])
            previousIndex += 1

        return previousCourses

    def __getGradientFromLinearRegression(self, previousCourses: list) -> float:
        # Automatise number vector
        numberVector = np.array([5, 4, 3, 2, 1]).reshape((-1, 1))
        coursesVector = np.array(previousCourses)

        model = LinearRegression().fit(numberVector, coursesVector)
        gradient = model.coef_ / previousCourses[0]
    
        return gradient[0]

    def __isFormationAccordant(self, index: int) -> float:
        template = self._getTemplate()
        dayCourse = self.data[index]
        relativeCandleStickCriteria = self.candleStickCreator.getRelativeCandleStickCriteria(dayCourse)

        dayCourseVector = np.fromiter(relativeCandleStickCriteria.values(), dtype=float)
        templateVector = np.fromiter(template.values(), dtype=float)
        correlationCoeffiecent = np.corrcoef(dayCourseVector, templateVector)

        return correlationCoeffiecent[0, 1] > FORMATION_ACCORDANCE

    def __isPreviousDevelopmentAccordant(self, index: int) -> bool:
        previousCourses = self.__getPreviousCourses(index)
        gradient = self.__getGradientFromLinearRegression(previousCourses)
        developmentRequirement = self._getPreviousDevelopmentRequirement(gradient)

        return developmentRequirement

    def __isComparisonToPreviousDay(self, index: int) -> bool:
        previousClose = self.data[index - 1]['close']
        dayOpen = self.data[index]['open']
        comparisonToPreviousDay = self._getPreviousCloseRequirement(previousClose, dayOpen)

        return comparisonToPreviousDay

    def isCandleStick(self, index: int) -> dict:
        if index <= PREVIOUS_COURSES_NUM - 1:
            return {
                'previousDevelopment': False,
                'formation': False,
                'previousClose': False
            }

        previousDevelopmentAccordance = self.__isPreviousDevelopmentAccordant(index)
        formationAccordance = self.__isFormationAccordant(index)
        previousClose = self.__isComparisonToPreviousDay(index)

        return {
            'previousDevelopment': previousDevelopmentAccordance,
            'formation': formationAccordance,
            'previousClose': previousClose
        }
