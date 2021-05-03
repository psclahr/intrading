from typing import Union
from backend.analyse.candleStick.formations.oneFormation.invertedHammer import InvertedHammer
from backend.analyse.candleStick.formations.oneFormation.hammer import Hammer
from backend.analyse.candleStick.formations.oneFormation.hangingMan import HangingMan
from backend.analyse.candleStick.formations.oneFormation.shootingStar import ShootingStar
from backend.analyse.enums.CandleStick import CandleStick
from backend.analyse.enums.Course import Course

class Recognizer:
    def __init__(self, data):
        self.data = data

    def __isCandleStick(self, candlestick: object, index: int) -> bool:
        isCandlestick = candlestick(self.data).isCandleStick(index)

        return not False in isCandlestick.values()

    def __isInvertedHammer(self, index: int) -> bool:
        return self.__isCandleStick(InvertedHammer, index)

    def __isHammer(self, index: int) -> bool:
        return self.__isCandleStick(Hammer, index)

    def __isHangingMan(self, index: int) -> bool:
        return self.__isCandleStick(HangingMan, index)

    def __isShootingStar(self, index: int) -> bool:
        return self.__isCandleStick(ShootingStar, index)

    def __whichCandleStick(self, index: int, day: dict) -> Union[dict, None]:
        if self.__isInvertedHammer(index):
            return {'name': CandleStick.INVERTED_HAMMER.value, 'date': day[Course.DATE.value]}

        if self.__isHammer(index):
            return {'name': CandleStick.HAMMER.value, 'date': day[Course.DATE.value]}

        if self.__isHangingMan(index):
            return {'name': CandleStick.HANGING_MAN.value, 'date': day[Course.DATE.value]}

        if self.__isShootingStar(index):
            return {'name': CandleStick.SHOOTING_STAR.value, 'date': day[Course.DATE.value]}

        return None

    def recognize(self) -> dict:
        candleSticks = []

        for index, day in enumerate(self.data):
            result = self.__whichCandleStick(index, day)

            if result is not None:
                candleSticks.append(result)

        return candleSticks
