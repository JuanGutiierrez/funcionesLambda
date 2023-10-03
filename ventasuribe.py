ventas=[
    {"id":"afc001", "nombre": "Pedro", "costo":350000},
    {"id":"afc030", "nombre": "Ana", "costo":150000},
    {"id":"afc021", "nombre": "Luis", "costo":1100000},
    {"id":"afc050", "nombre": "Flor", "costo":250000},
    {"id":"afc777", "nombre": "Mateo", "costo":800000},
    {"id":"afc777", "nombre": "Lina", "costo":720000}
]

#Que los ID esten en mayuscula
#Obtener Compras superiores a 60000
#Ordenar esas compras superiores de menor a mayor (afc320----linea costo: 1200000)

#Fucion para convertir en mayuscula
convertirMayusculas=lambda texto:texto.upper()
for venta in ventas:
    venta["id"]=convertirMayusculas(venta["id"])

ventasAltas=[venta for venta in ventas if venta["costo"]>600000]

ventasOrdenadas= sorted(ventasAltas, key=lambda venta:venta["costo"])

for venta in ventasOrdenadas:
    print (f"{venta['id']} ---- {venta['nombre']} ---- {venta['costo']}")