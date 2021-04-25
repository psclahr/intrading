from backend.analyse.candleStick.formations.oneFormation.abstractOneFormation import AbstractOneFormation
from backend.analyse.enums.CandleStickComparison import CandleStickComparison

class ShootingStar(AbstractOneFormation):
    def _getTemplate(self) -> dict:
        return {
            CandleStickComparison.BODY_SIZE_PERCENTAGE.value: 0.15,
            CandleStickComparison.UPPER_WICK_PERCENTAGE.value: 0.80,
            CandleStickComparison.LOWER_WICK_PERCENTAGE.value: 0.05
        }

    def _getPreviousDevelopmentRequirement(self, gradient) -> bool:
        return self.limitValueTrend <= gradient

    def _getPreviousCloseRequirement(self, previousClose: float, dayOpen: float) -> bool:
        return previousClose < dayOpen