salarios=[1160000,2500000,3200000, 6000000,500000,2000000,2800000,3500000,1200000]

#Organizar lista de mayor a menor

#Funcion lambda para organizar datos
#sorted
#Menor a mayor
datorOrdenados =sorted(salarios, key=lambda salario:salario)
print (datorOrdenados)
#Mayor a menor
datorOrdenados2 =sorted(salarios, key=lambda salario:-salario)
print (datorOrdenados2)