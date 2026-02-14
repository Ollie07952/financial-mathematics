def gbm(s0,mu,sigma,paths,t_days):
    """
    Simulates geometric Brownian motion
    --
    :arg s0: float/int; starting stock price
    :arg mu: float; drift (annual return)
    :arg sigma: float; annualised volatility
    :arg paths: int; the number of different paths to simulate
    :arg t_days: int; the number of trading days to simulate
    --
    :return walks: array(s); array(s) of stock price(s) over the entire period
    """
    import numpy as np
    rng = np.random.default_rng()

    normals = rng.standard_normal(size = (paths,t_days)) #Note: standard normal is not optimal; true distribution exhibits greater kurtosis (fat-tails) and positive skew.
    steps = np.exp((mu-0.5*np.square(sigma))*(1/252) + sigma*np.sqrt(1/252)*normals)
    steps = np.concatenate((np.full(shape = (paths,1), fill_value = s0), steps), axis = 1)
    walks = np.cumprod(steps, axis = 1)
    return walks

def binomial(s0,p,u,d,paths,N):
    """
    Simulates an N-period binomial asset-pricing model
    --
    :arg s0: float/int; starting stock price
    :arg p: probability of an upward move (heads)
    :arg u: price multipler for an upward move; S_{1}(H) = uS_{0}
    :arg d: price multiplier for a downward move; S_{1}(T) = dS_{0}
    :arg paths: int; the number of different paths to simulate
    :arg N: int; the number of periods to simulate
    --
    :return walks: array(s); array(s) of stock price(s) over the entire period
    """
    import numpy as np

    rng = np.random.default_rng()
    binomials = rng.binomial(1, p, size = (paths,N)) #1 = Heads, 0 = Tails
    steps = np.where(binomials == 1, u, d)
    steps = np.concatenate((np.full(shape = (paths,1), fill_value = s0), steps), axis = 1)
    walks = np.cumprod(steps, axis = 1)
    return walks
