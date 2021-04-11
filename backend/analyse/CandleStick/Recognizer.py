from typing import Union
from backend.analyse.CandleStick.Formations.OneFormation.InvertedHammer import InvertedHammer
from backend.analyse.CandleStick.Formations.OneFormation.Hammer import Hammer
from backend.analyse.CandleStick.Formations.OneFormation.HangingMan import HangingMan
from backend.analyse.CandleStick.Formations.OneFormation.ShootingStar import ShootingStar
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

    def whichCandleStick(self, index: int) -> Union[dict, None]:
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
