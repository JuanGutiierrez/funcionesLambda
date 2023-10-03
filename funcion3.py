#Emule las operaciones basicas a elección del usuario

#Funcion sumar
sumar = lambda n1,n2: n1+n2

#Funcion resta
restar = lambda n1,n2: n1-n2

#Funcion multiplicar
multiplicar = lambda n1,n2: n1*n2

#Funcion dividir
dividir = lambda n1,n2: n1/n2

#Menu para elegir la operacion

print ("Menu")
print ("Opcion 1: Sumar")
print ("Opcion 2: Restar")
print ("Opcion 3: Multiplicar")
print ("Opcion 4: Dividir")

opcion=0

while (opcion != 0):
    opcion = int(input("dijite la opcion deseada: "))
    
    if opcion == 1:
        sumar(5,10)
    elif opcion == 2:
        restar(10,5)
    elif opcion == 3:
        multiplicar(2,4)
    elif opcion == 4:
        dividir(8,2)
