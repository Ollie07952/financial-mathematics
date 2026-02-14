def logReturns(tickers,period):
    """
    Calculates daily log returns for each given ticker over the given period.
    --
    :arg tickers: str; ticker list as a single str of the form "ABC DEFG XYZ ..."
    :arg period: str; the period of returns to analyse; one of: [1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max]
    --
    :returns logs: dataframe; daily log returns for each ticker over the given period
    """
    import yfinance as yf
    import numpy as np

    closes = yf.download(tickers, period = period, auto_adjust = True, progress = False)["Close"]
    logs = np.log(closes/closes.shift(1))
    logs.columns.name = "Ticker"
    return logs


def vol(tickers,period,k = 30):
    """
    Calculates rolling and stationary annualised volatility for each given ticker
    --
    :arg tickers: str; ticker list as a single str of the form "ABC DEFG XYZ ..."
    :arg period: str; the period of returns to analyse; one of: [1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max]
    :arg k: int; the history of the rolling volatility, in days. i.e. size of the rolling volatility window.
                 NOTE: k MUST NOT BE GREATER IN LENGTH THAN CHOSEN PERIOD
    --
    :returns roll: dataframe; rolling (annualised) volatility with history k for each ticker
    :returns ann: series; annualised volatility of each ticker over the given period
    """
    import numpy as np

    logs = logReturns(tickers, period)
    roll = logs.rolling(window = k).std()*np.sqrt(252)
    ann = logs.std(ddof = 1, axis = 0)*np.sqrt(252)
    roll.columns.name = "Ticker"
    ann.name = "Annualised Vol."
    ann.index.name = "Ticker"
    return roll, ann


def maxDraw(tickers,period):
    """
    Calculates the maximum drawdown for each given ticker over the given period
    --
    :arg tickers: str; ticker list as a single str of the form "ABC DEFG XYZ ..."
    :arg period: str; the period of returns to analyse; one of: [1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max]
    --
    :returns max_draws: dataframe; value of the maximum drawdown and corresponding percent return of this drawdown for each ticker over the given period
    """
    import yfinance as yf
    from pandas import DataFrame

    closes = yf.download(tickers, period=period, auto_adjust=True, progress=False)["Close"]
    runmax = closes.cummax()
    abs_d, perc_d = (runmax-closes).max(), ((runmax-closes)/runmax).max()
    drawdowns = DataFrame({"Absolute":abs_d, "Percentage":perc_d}).transpose()
    drawdowns.columns.name = "Ticker"
    return drawdowns
