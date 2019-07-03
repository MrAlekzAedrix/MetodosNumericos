def Serial() :

    n1=int(input("Please enter a number: "))
    n2=int(input("Please enter another number: "))

    if n1>n2 :
        for n2 in range(n2, n1+1) :
            print(n2)


    if n2>n1 :
        for n1 in range(n1, n2+1) :
            print(n1)



Serial()