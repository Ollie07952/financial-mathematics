def var(tickers, period, q = 95):
    """
    Calculates daily q% Value-at-Risk, that is the q-th percentile of daily-log returns
    --
    :arg tickers: str; ticker list as a single str of the form "ABC DEFG XYZ ..."
    :arg period: str; the period of returns to analyse; one of: [1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max]
    :arg q: int or float; Value-at-Risk percentage (VaR), default: 95%
    --
    :returns var: float; Value-at-Risk based off q parameter
    """
    import numpy as np

    logs = logReturns(tickers, period).iloc[1:,:]
    var = np.percentile(logs, axis = 0, q = 100-q)
    return var
