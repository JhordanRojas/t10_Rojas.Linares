def validar_cadena(cad):
    if (isinstance(cad,str)):
        return True
    else:
        return False
#fin_validar_cadena

def validar_entero(n):
    if(isinstance(n, int)):
        return True
    else:
        return False
#fin_validar_entero

def validar_rango(n, ri, rf):
    if(validar_entero(n) == True):
        if(n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False
#fin_validar_rango

def pedir_numero(msg, ri, rf):
    n=""
    while(validar_rango(n, ri, rf) == False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if(isinstance(nombre, str)):
        if(len(nombre)>=3 and nombre.isalpha()==True):
            return True
        else:
            return False
    else:
        return False
#fin_validar_nombre

def pedir_nombre(msg):
    nombre=""
    while(validar_nombre(nombre) == False):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedr_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()
#fin_guardar_datos

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido=archivo.read()
    archivo.close()
    return contenido
#fin_obtener_datos

def validar_dni(dni):
    if(isinstance(dni, str)):
        if(len(dni)==8 and dni.isdigit()==True):
            return True
        else:
            return False
    else:
        return False
############################################################################
#asset esto
def pedir_dni(msg):
    dni=""
    while(validar_dni(dni)==False):
        dni=input(msg)
    #fin_while
    return  dni

def validar_idioma(idioma):
    if (validar_cadena(idioma)==True):
        if (idioma=="ingles" or idioma=="italiano" or idioma=="frances" or idioma=="ruso" or
            idioma=="chino" or idioma=="aleman" or idioma=="coreano" or idioma=="quechua"):
            return True
        else:
            return False
    else:
        return False
#fin_validar_idioma

def pedir_idioma(msg):
    idioma=""
    while(validar_idioma(idioma)==False):
        idioma=input(msg)
    return idioma
#fin_pedir_idioma



def validar_empresa(emp):
    if(validar_cadena(emp)==True):
        if(emp=="samsung" or emp=="apple" or emp=="microfsoft" or emp=="sony" or emp=="lg" or
           emp=="xiaomi"or emp=="hisense"or emp=="motorola"or emp=="asus"or emp=="oppo"):
            return True
        else:
            return False
    else:
        return False
#fin_def



def pedir_empresa(mss):
    ing=""
    while(validar_empresa(ing)==False):
        ing=input(mss)
    return ing
#fin_def


def pedir_cel(msj):
    invalido=True
    numero=0
    while invalido:
        numero=input(msj)
        longi=(len(numero)==9)
        invalido=(numero.isdigit()== False and longi==True)
    #fin_while
    return int(numero)



def validar_marca(marca):
    if (validar_cadena(marca)==True):
        if(marca=="nike" or marca=="adidas" or marca=="reebok" or marca=="puma" or marca=="converse" or marca=="skechers" or
           marca=="columbia" or marca=="new balance" or marca=="merrel" or marca=="asics"):
            return True
        else:
            return False
    else:
        return False
#fin_def


def pedir_marca(msg):
    mar=""
    while(validar_marca(mar) == False):
        mar=input(msg)
    return mar
#fin_def



def validar_color(color):
    if (validar_cadena(color)==True):
        if ( color == "blanco" or color == "negro" or color == "rojo" or color == "azul" or color == "verde" or color == "amarillo" or
             color == "gris" or color == "naranja" or color == "marron" or color == "rosado" or color == "celeste" ):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_color(mss):
    color=""
    while(validar_color(color)==False):
        color=input(mss)
    return color
#fin_def


def validar_clase(clase):
    if (validar_cadena(clase)==True):
        if (clase=="aportante" or clase=="deudor"):
            return True
        else:
            return False
    else:
        return False

def pedir_clase(mss):
    oc=""
    while (validar_clase(oc)==False):
          oc=input(mss)
    return oc









        #recuerda finalizar con los assert de los progrmas "pedir"
