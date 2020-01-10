
    print("Datos del trabajador guardados")

def leerTrabajador():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("######## MENU #######")
    print("1. Agregar Trabajador")
    print("2. Leer Trabajador")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarTrabajador()
    if (opc == 2):
        leerTrabajador()

#fin_menu
print("Fin del programa")

