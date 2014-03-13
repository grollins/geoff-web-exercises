from numpy import linspace
from numpy.random import normal, choice
from scipy.optimize import minimize

def f(x, params):
    m, b = params
    return m * x + b

def noise(x):
    return normal(loc=0.0, scale=2.0, size=len(x))

def generate_data():
    # divide the range 0 to 100 into 1000 increments
    x = linspace(0, 100, 1000)
    # to make things more realistic, throw away some of the x values
    selected_indices = choice(len(x), int(len(x)/5.), replace=False)
    x = x[selected_indices]
    # y equals our function plus a noise term
    y = f(x, params=(0.256, 5.318)) + noise(x)
    return x, y

def fit_data(x, y):
    # minimize the residual sum of squares
    fit_func = lambda params: sum((y - f(x, params))**2)
    results = minimize(fit_func, [2.0, 2.0], method='BFGS')
    print results
    return results.x
