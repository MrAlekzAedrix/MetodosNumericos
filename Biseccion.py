import math


def f(x):
    y = x - (math.sin(x))
    return y

print("Root finder 'x-sin(x)' ")
xa = -2
xb = 2
err = 0.0001
xr = (xa+xb)/2.0
i = 1

while abs(f(xr)) > err:
    i = i+1
    xr = (xa+xb)/2.0
    if f(xa) * f(xr) > 0:
        xa = xr
    else:
        xb = xr
print("Number of iteration: ", i)
print("Root: ", xr)

