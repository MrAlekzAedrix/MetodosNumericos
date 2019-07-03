def f(x):
    return x ** 4 - 10 * (x ** 3) + 3 * (x ** 2) + x + 23

def df(x):
    return 4 * (x ** 3) - 30 * (x ** 2) + 6 * x + 1


i=1
err=0.0001

while i<err:
    i=i+1
    x1= x - (f(x)/df(x))
    if abs(x-x1) < err:
        print("Root: ", x1)
    x=x1