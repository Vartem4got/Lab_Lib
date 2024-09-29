

import math


def cosec(x):
    return 1 / math.cosec(x)

def log_(x):
    return x + math.log(x**(1/7))

def log_I0(x):
    return math.log10(math.exp(x) + 4)

a = 4
b = 6
h = 0.2

x = a

while x <= b:
    if x < 4.5:
        result = cosec(x**2)
    elif 4.5 <= x < 5:
        result = function1(x)
    else:
        result = function2(x)
    
    print(f"x = {x:.2f}, f(x) = {result:.4f}")
    x += h
