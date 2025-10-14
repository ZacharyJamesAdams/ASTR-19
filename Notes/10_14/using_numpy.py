import numpy as np

x, y = 1.0, 2.0

def f(x):
    return float(x)**2

def df(x):
    return float(x)*2

def d(op, x: float, delta: float):
    return (op(x+delta)-op(x))/delta

X = [i for i in range(-3,4)]


x = 2
for delta in range(5):
    delta = 1.0*10.**delta
    a = df(x)
    b = d(f,x,delta)
    print(f'df({x}) = {a} d(f({x})) = {b}')
    print(f'err = {100.0*(b-a)/a:.4f} %')