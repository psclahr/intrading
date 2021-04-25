from typing import Union
from backend.analyse.candleStick.formations.oneFormation.invertedHammer import InvertedHammer
from backend.analyse.candleStick.formations.oneFormation.hammer import Hammer
from backend.analyse.candleStick.formations.oneFormation.hangingMan import HangingMan
from backend.analyse.candleStick.formations.oneFormation.shootingStar import ShootingStar
from backend.analyse.enums.CandleStick import CandleStick

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

    def __whichCandleStick(self, index: int) -> Union[dict, None]:
        if self.__isInvertedHammer(index):
            print({'name': CandleStick.INVERTED_HAMMER.value, 'index': index, 'date': self.data[index]['date']})
            return {'name': CandleStick.INVERTED_HAMMER.value, 'index': index}

        if self.__isHammer(index):
            print({'name': CandleStick.HAMMER.value, 'index': index, 'date': self.data[index]['date']})
            return {'name': CandleStick.HAMMER.value, 'index': index}

        if self.__isHangingMan(index):
            print({'name': CandleStick.HANGING_MAN.value, 'index': index, 'date': self.data[index]['date']})
            return {'name': CandleStick.HANGING_MAN.value, 'index': index}

        if self.__isShootingStar(index):
            print({'name': CandleStick.SHOOTING_STAR.value, 'index': index, 'date': self.data[index]['date']})
            return {'name': CandleStick.SHOOTING_STAR.value, 'index': index}

        return None

    def recognize(self) -> dict:
        candleSticks = {}

        for index, day in enumerate(self.data):
            result = self.__whichCandleStick(index)

            if result is not None:
                name = result['name']
                index = result['index']

                if name in candleSticks:
                    candleSticks[name].append(index)
                else:
                    candleSticks[name] = [index]

        return candleSticks
