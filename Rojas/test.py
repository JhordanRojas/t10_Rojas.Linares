from Rojas import libreria

#validar cadena
assert(libreria.validar_cadena("abcde")==True)
assert(libreria.validar_cadena(1325)==False)
assert(libreria.validar_cadena("03246")==True)
assert(libreria.validar_cadena("ax645")==True)
assert(libreria.validar_cadena("213.1")==True)
print("validar cadena >> Ok")

#validar entero
assert(libreria.validar_entero(155)==True)
assert(libreria.validar_entero(163.21)==False)
assert(libreria.validar_entero("354")==False)
assert(libreria.validar_entero(True)==True)
assert(libreria.validar_entero(3550)==True)
print("validar entero >> Ok")

#validar rango
assert(libreria.validar_rango(5,1,8)==True)
assert(libreria.validar_rango(12,12,14)==True)
assert(libreria.validar_rango(10,45,48)==False)
assert(libreria.validar_rango(15,5,10)==False)
print("validar rango >> OK")

#validar nombre
assert(libreria.validar_nombre("juan")==True)
assert(libreria.validar_nombre("ae")==False)
assert(libreria.validar_nombre(True)==False)
assert(libreria.validar_nombre(564)==False)
assert(libreria.validar_nombre("a545s")==False)
print("validar nombre >> Ok")

assert(libreria.validar_dni("71083546")==True)
assert(libreria.validar_dni("08154672")==True)
assert(libreria.validar_dni("16482973")==True)
assert(libreria.validar_dni("6546546")==False)
assert(libreria.validar_dni("1656541a")==False)
assert(libreria.validar_dni(701849531)==False)
print("validar dni >> Ok")



assert(libreria.validar_idioma("frances")==True)
assert(libreria.validar_idioma("ingles")==True)
assert(libreria.validar_idioma("aleman")==True)
assert(libreria.validar_idioma("quechua")==True)
assert(libreria.validar_idioma("chino")==True)
assert(libreria.validar_idioma("japones")==False)
assert(libreria.validar_idioma("gallego")==False)
assert(libreria.validar_idioma("peru")==False)
print("validar idioma >> Ok")



assert(libreria.validar_empresa("apple")==True)
assert(libreria.validar_empresa("samsung")==True)
assert(libreria.validar_empresa("oppo")==True)
assert(libreria.validar_empresa("iphone")==False)
assert(libreria.validar_empresa("xiaomi")==True)
assert(libreria.validar_empresa("16354")==False)
assert(libreria.validar_empresa("merces")==False)
print("validar empresa >> Ok")


assert(libreria.validar_marca("nike")==True)
assert(libreria.validar_marca("adidas")==True)
assert(libreria.validar_marca("reebok")==True)
assert(libreria.validar_marca("gixi")==False)
assert(libreria.validar_marca("blackk")==False)
assert(libreria.validar_marca("23455")==False)
print("validar marca >> Ok")

assert(libreria.validar_color("blanco")==True)
assert(libreria.validar_color("marron")==True)
assert(libreria.validar_color("rojo")==True)
assert(libreria.validar_color("amarillo")==True)
assert(libreria.validar_color("black")==False)
assert(libreria.validar_color("5465")==False)
assert(libreria.validar_color("oranje")==False)
print("validar color >> Ok")


assert(libreria.validar_clase("trabajador")==False)
assert(libreria.validar_clase("aportante")==True)
assert(libreria.validar_clase("deudor")==True)
assert(libreria.validar_clase("aportante")==True)
assert(libreria.validar_clase(True)==False)
assert(libreria.validar_clase(5646)==False)
print("validar clase >> Ok")
