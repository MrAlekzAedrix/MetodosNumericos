print('Welcome!') #Mensaje de bienvenida

n = int(input('Please enter a number: ')) #Ingreso de número

while n <1 : #Bucle de error
    print('The value you entered is less than 0, you have to enter a positive value') #Ciclo de repetición por numero negativo
    n = int(input('Please enter a number: ')) #Ingreso de número

if n == 2 :
    print (n)
else :
    for i in range(2, n):
        prime = True
        for j in range(2, i):
            if i%j == 0:
                prime = False
        if prime is True :
            print(i)
input ('Press ENTER to finish')