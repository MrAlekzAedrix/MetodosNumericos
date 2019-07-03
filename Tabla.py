#Tabla de multiplicar

print('Welcome!') #Mensaje de bienvenida

n = int(input('Please enter the number you want to see the first 10 multiples of: ')) #Ingreso de número

while n <= 0 : #Bucle de error
    print('The value you entered is less than 0, you have to enter a positive value') #Ciclo de repetición por numero negativo
    n = int(input('Please enter the number you want to see the first 10 multiples of: ')) #Ingreso de número

if n > 0 : #Evalua si n mayor que cero

   i = 1 #Número del múltiplo
   
   while i <= 10 : #Bucle de la tabla
       
       print(n, 'times', i, '=', n*i) #impresión de la tabla
       i += 1 #Aumento del múltiplo
input('Press ENTER to finish')
