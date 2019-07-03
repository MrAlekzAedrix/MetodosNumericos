def Factorial() :
    fac= 1.0
    n=int(input("Please enter a number to know its factorial of: "))
    for i in range(1, n+1) :
        fac = fac * i
    print("It's factorial is: ", fac)

Factorial()