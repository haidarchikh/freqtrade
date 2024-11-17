import talib.abstract as ta
from pandas import DataFrame

from freqtrade.strategy.interface import IStrategy


class SampleStrategy(IStrategy):
    minimal_roi = {
        "0": 0.1  # Take profit at 10% gain
    }

    stoploss = -0.15  # Stop loss at 5% loss
    timeframe = "3m"  # 3 minutes candles

    can_short = True  # Enable shorting

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["sma10"] = ta.SMA(dataframe["close"], timeperiod=10)
        dataframe["sma30"] = ta.SMA(dataframe["close"], timeperiod=30)
        dataframe["rsi"] = ta.RSI(dataframe["close"], timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Long Entry
        dataframe.loc[
            (
                (dataframe["sma10"] > dataframe["sma30"])  # SMA crossover
                & (dataframe["rsi"] > 50)  # RSI above 50
                & (dataframe["volume"] > 0)  # Ensure there's volume
            ),
            "enter_long",
        ] = 1

        # Short Entry
        dataframe.loc[
            (
                (dataframe["sma10"] < dataframe["sma30"])  # SMA crossover
                & (dataframe["rsi"] < 50)  # RSI below 50
                & (dataframe["volume"] > 0)  # Ensure there's volume
            ),
            "enter_short",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Long Exit
        dataframe.loc[
            (
                (dataframe["close"] < dataframe["sma10"])  # Price below SMA
                | (dataframe["rsi"] < 40)  # RSI below 40
            ),
            "exit_long",
        ] = 1

        # Short Exit
        dataframe.loc[
            (
                (dataframe["close"] > dataframe["sma10"])  # Price above SMA
                | (dataframe["rsi"] > 60)  # RSI above 60
            ),
            "exit_short",
        ] = 1

        return dataframe
