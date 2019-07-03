#Mayoría de edad

print('Welcome! This is a legal age verification program, please enter your age: ') #Bienvenida

age = int(input('')) #Introducción de edad

if age > 0 and age < 18: #Condición si es mayor que 0 y menor que 18
    print("You're underage") #Es menor de edad
    
if age > 18 : #Condición si es mayor de 18
    print('You have the legal age in some states') #Es mayor de edad
    
if age<=0 : #Condición si es menor o igual a 0
    print('The age you entered is an invalid number') #Mensaje de erros


input('Press ENTER to finish') #Pausa