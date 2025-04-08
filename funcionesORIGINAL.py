from principal import *
from configuracion import *
import random
import math
from extras import *
# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    misProductos=open("productos.txt","r")
    los_productos=[]
    productos=misProductos.readlines()
    for producto in productos:
        datos = []
        elemento = ""
        for caracter in producto:
            if caracter == ',':
                datos.append(elemento)
                elemento = ""
            else:
                elemento += caracter
        datos.append(elemento)# Agrega el último elemento
        for i in range(1, len(datos)):# Convierte los elementos 1 y 2 a enteros
            datos[i] = int(datos[i])
        los_productos.append(datos)
    misProductos.close()
    return los_productos

#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
    elProducto=random.choice(lista_productos)
    calidadPrecio=random.randint(1,2)
    precioAzar=elProducto[calidadPrecio]
    if precioAzar==elProducto[1]:
        producto=[elProducto[0],"(economico)",precioAzar]
        return producto
    else:
        producto=[elProducto[0],"(premium)",precioAzar]
        return producto

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    validar=False
    while validar==False:
        producto = buscar_producto(lista_productos)
        validar=esUnPrecioValido(producto[2],lista_productos,margen)
    return producto

#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
def esUnPrecioValido(precio, lista_productos, margen):
    cont=0
    for i in range(len(lista_productos)):
        elProducto=lista_productos[i]
        if abs(precio-elProducto[1])<=margen or abs(precio-elProducto[2])<=margen:
            cont=cont+1
    if cont>=3:
        return True
    else:
        return False

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen,acierto_sound,error_sound):
    precio_principal = producto_principal[2]
    precio_candidato = producto_candidato[2]

    if abs(precio_principal - precio_candidato) <= margen:
        acierto_sound.play()
        return precio_candidato
    else:
        error_sound.play()
        return 0

def misSimilares(cantidad, producto, lista_productos, margen):
    similitud = []
    lista_productos_copia = lista_productos.copy()#copy es un método en Python que se utiliza para crear una copia superficial de una lista. Crea una nueva lista
    random.shuffle(lista_productos_copia)#shuffle es una función de la biblioteca random de Python que se utiliza para mezclar al azar los elementos de una lista.
    for miPosibleSimilar in lista_productos_copia:#Al crear una nueva lista, no interfiero en la dada
        if len(similitud) == cantidad:
            break
        nombres_similitud = [prod[0] for prod in similitud]
        if miPosibleSimilar[0] != producto[0] and abs(producto[2]-miPosibleSimilar[1])<=margen and miPosibleSimilar[0] not in nombres_similitud:
            producto_similar=[miPosibleSimilar[0],"(economico)",miPosibleSimilar[1]]
            similitud.append(producto_similar)
        elif miPosibleSimilar[0] != producto[0] and abs(producto[2]-miPosibleSimilar[2])<=margen and miPosibleSimilar[0] not in nombres_similitud:
            producto_similar=[miPosibleSimilar[0],"(premium)",miPosibleSimilar[2]]
            similitud.append(producto_similar)
    return similitud

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(producto, lista_productos, margen):
    productos_seleccionados = [producto]
    similares = misSimilares(2, producto, lista_productos, margen)
    azar = noSimilares(3, producto, lista_productos, margen, similares)
    productosAleatorios = (similares + azar)
    random.shuffle(productosAleatorios)
    productos_seleccionados += productosAleatorios
    return productos_seleccionados

def noSimilares(cantidad, producto, lista_productos, margen, similares):
    productosAzar = []
    intentos = 0
    while len(productosAzar) < cantidad:
        azarProductos = buscar_producto(lista_productos)
        if azarProductos[0] != producto[0] and azarProductos not in productosAzar and azarProductos not in similares:
            productosAzar.append(azarProductos)
        intentos += 1
    return productosAzar