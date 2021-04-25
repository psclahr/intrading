import csv
import numpy as np
from backend.analyse.candleStick.limitValues import FUTURE_COURSES_NUM

class Predicter:
    def __init__(self, data: list):
        self.data = data

    def __getFutureCourses(self, index: int) -> list:
        futureCourses = []
        futureIndex = 1

        while futureIndex <= FUTURE_COURSES_NUM:
            futureCourses.append(self.data[index + futureIndex]['close'])
            futureIndex += 1

        return futureCourses

    def __getRelativeReturnForFutureCourse(self, index: int) -> list:
        dayClose = self.data[index]['close']
        futureCourses = self.__getFutureCourses(index)

        return list(map(lambda futureCourse: futureCourse / dayClose - 1, futureCourses))

    @staticmethod
    def __getMedianPredictionsFromMatrix(matrix: list) -> list:
        medianPredictions = []
        index = 0

        while index <= FUTURE_COURSES_NUM - 1:
            medianPredictions.append(np.median(matrix[:,index]))
            index += 1

        return medianPredictions

    def predict(self, recognitions: list):
        futureReturnsForAllRecognitions = list(map(self.__getRelativeReturnForFutureCourse, recognitions))

        matrix = np.vstack([futureReturnsForAllRecognitions])

        return Predicter.__getMedianPredictionsFromMatrix(matrix)
