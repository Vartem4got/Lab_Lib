
import math


def cal_seria(x, d):
    sum_seria = 0  
    k = 1  
    term = float('inf')  
    
    while abs(term) >= d:  
        term = (1 / k) * math.tan(x / (2 ** k))  
        sum_seria += term  
        k += 1
    
    return sum_seria

a = 3
b = 4
h = 0.1
d = 0.001

x = a

while x <= b:
    seria_val = cal_seria(x, d)
    print(f"x = {x:.2f}, S(x) = {seria_val:.6f}")
    x += h