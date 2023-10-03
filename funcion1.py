def sumar(numeroUno, numeroDos):
    return numeroUno + numeroDos

#Funcion lambda
sumarAlternativo = lambda numeroUno, numeroDos:(numeroUno + numeroDos)

#Llamando las funciones
resultado=sumar (5,10)
resultadoLambda=sumarAlternativo(20,10)

print(resultado)
print(resultadoLambda)