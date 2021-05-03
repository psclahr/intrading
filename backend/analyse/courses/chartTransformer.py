from datetime import datetime
from backend.analyse.enums.Course import Course

class ChartTransformer():
    def __init__(self):
        self.courses = [] 

    def __addProp(self, values: list, typo: str):
        for index, value in enumerate(values[:-1]):
            self.courses[index] = {
                **self.courses[index],
                typo: value
            }

    def __addTimeStamp(self, timeStamps: list):
        for timestamp in timeStamps[:-1]:
            self.courses.append({
                Course.DATE.value : datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
            })

    def __addOpenCourse(self, openCourses: list):
        self.__addProp(openCourses, Course.OPEN.value)

    def __addCloseCourse(self, closeCourses: list):
        self.__addProp(closeCourses, Course.CLOSE.value)

    def __addHighCourse(self, highCourses: list):
        self.__addProp(highCourses, Course.HIGH.value)

    def __addLowCourse(self, lowCourses: list):
        self.__addProp(lowCourses, Course.LOW.value)

    def transform(self, timestamps: list, openCourses: list, closeCourses: list, highCourses: list, lowCourses: list):
        self.__addTimeStamp(timestamps)
        self.__addOpenCourse(openCourses)
        self.__addCloseCourse(closeCourses)
        self.__addHighCourse(highCourses)
        self.__addLowCourse(lowCourses)

        return self.courses