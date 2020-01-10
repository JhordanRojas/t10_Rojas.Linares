from Rojas import libreria

def agregar_cliente():
    cliente=libreria.pedir_nombre("Ingrese el nombre del cliente: ")
    numero=str(libreria.pedir_cel("Ingrese el celular del cliente: "))
    content=cliente+"-"+numero+"\n"
    libreria.guardar_datos("clientes.txt",content,"a")

def most_cliente():
    verro=libreria.obtener_datos("clientes.txt")
    if (verro != ""):
        print(verro)
    else:
        print("sin datos")


oppcn=0
limit=3
while (oppcn != limit):
    print("##########################")
    print("#     CLIENTES  MENU     #")
    print("##########################")
    print("# 1. Agregar cliente     #")
    print("# 2. Clientes agregados  #")
    print("# 3. Salir               #")
    print("##########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_cliente()

    if (oppcn == 2):
        most_cliente()


print("fin del programa")

