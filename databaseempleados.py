empleados=[
    {"codigo": 105, "salario":2000000,"nombre":"Fernando Fernandez"},
    {"codigo": 107, "salario":7000000,"nombre":"Maria Ramirez"},
    {"codigo": 110, "salario":2500000,"nombre":"Zakarias Flores"},
    {"codigo": 155, "salario":5000000,"nombre":"Isabela Mesa"},
    {"codigo": 125, "salario":200000,"nombre":"Carolina Vidal"},
    {"codigo": 177, "salario":3000000,"nombre":"Ana Maria Cortes"},
    {"codigo": 100, "salario":20000000,"nombre":"Esperanza Gomez"},
    {"codigo": 15, "salario":8000000,"nombre":"Diomedez Dias"},
    {"codigo": 144, "salario":2000000000,"nombre":"Albareto Uribe"},
    {"codigo": 1, "salario":1000000,"nombre":"Camilo Figaro"}
]

#Filtrar los empleados con salarios mayores de 2.5'
empleadosAltosSalarios = [empleado for empleado in empleados if empleado["salario"]>2500000]

#Se organice por codigo de menor a mayor

empleadosAltosSalarios =sorted(empleadosAltosSalarios, key=lambda empleado:empleado['codigo'])

for empleado in empleadosAltosSalarios:
    print (f"Codigo: {empleado['codigo']} ---- Nombre: {empleado['nombre']}")