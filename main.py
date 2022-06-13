#Importaciones
from numpy import NaN
from arma import Arma
from atributo import Atributo
import pandas as pd
from random import randint
import time

#Esta clase maneja el generador

#Listas de todas las armas y todos los atributos
ARMAS = []
ATRIBUTOS = []

#Este metodo trae las armas del archivo de excel y las convierte en dataframe
def tomarDatosArmas():
    df = pd.read_excel('Armas.xlsx', sheet_name="Sheet1")
    df.head(5)
    return df

#Este metodo trae los atributos del archivo de excel y las convierte en dataframe
def tomarDatosAtributos():
    df = pd.read_excel('Atributos.xlsx', sheet_name="Sheet1")
    df.head(5)
    return df

#Este método crea las armas a partir del dataframe y las mete en la lista con todas las armas
def crearArmas(dataFrame):
    for index  in dataFrame.index:
        #Valores del arma
        nombre = dataFrame["nombre"][index]
        coste = dataFrame["Coste"][index]
        danio = dataFrame["Daño"][index]
        tipoDanio = dataFrame["Tipo Daño"][index]
        peso = dataFrame["Peso"][index]
        propiedades = dataFrame["Propiedades"][index]

        #Crear el arma
        arma = Arma(index, nombre , coste, danio, tipoDanio, peso, propiedades)

        #Ingresar el arma en la lista de armas
        ARMAS.append(arma)


#Este método crea los atributos a partir del dataframe y las mete en la lista con todos los atributos
def crearAtributos(dataFrame):
    for index  in dataFrame.index:
        #Valores del atributo
        nombre = dataFrame["nombre"][index]
        descripcion = dataFrame["descripcion"][index]
        afValor = dataFrame["af valor"][index]
        afDanio = dataFrame["af danio"][index]
        afTipoDanio = dataFrame["af tipo danio"][index]
        afPeso = dataFrame["af peso"][index]

        armasIncompatibles = []
        strArmas = str(dataFrame["armasIncompatibles"][index])
        armasIncompatibles = strArmas.split(",")

        atributosIncompatibles = []
        strAtributos = str(dataFrame["atributosIncompatibles"][index])
        atributosIncompatibles = strAtributos.split(",")

        #Crear el atributo
        atributo = Atributo(index, nombre, descripcion, afValor, afDanio, afTipoDanio, afPeso, armasIncompatibles, atributosIncompatibles)

        #Ingresar el arma en la lista de armas
        ATRIBUTOS.append(atributo)

#Dar atributos
def darAtributo(opcion, arma):
    randAtr = 0
    #Valor al azar de id de arma
    if int(opcion) == 1:
        randAtr = randint(0,99)
    
    #atributo
    atributo = ATRIBUTOS[randAtr]

    #Verificacion compatibilidad
    armasIncompatibles = atributo.armasIncompatibles
    if "nan" not in armasIncompatibles:
        [int(x) for x in armasIncompatibles]
    else:
        armasIncompatibles = []
    
    listaAtr = arma.atributos
    atributosIncompatibles = atributo.atributosIncompatibles
    if "nan" not in atributosIncompatibles:
        [int(x) for x in atributosIncompatibles]
    else:
        atributosIncompatibles = []

    #Si los atributos no son compatibles
    if (arma.id-1 in armasIncompatibles) or (atributo.id-1 in listaAtr) or (atributo.id-1 in atributosIncompatibles):
        return None
    #Si los atributos si son compatibles
    else:
        arma.agregarAtributo(atributo)
        arma.aplicarAtributo(int(atributo.afectacionDanio), str(atributo.afectacionTipoDanio), int(atributo.afectacionValor), str(atributo.afectacionPeso))
        return atributo


# Aqui se corre todo el código
if __name__ == '__main__':

    #Carga de las armas y atributos
    print(" ")
    print("Bienvenido, cargando datos...")
    print("---------------------")
    dfArmas = tomarDatosArmas()
    dfAtributos = tomarDatosAtributos()
    crearArmas(dfArmas)
    crearAtributos(dfAtributos)
    print("Todas las armas y atributos han sido cargados correctamente")
    print("---------------------")


    #Creación del arma
    print("CREACIÓN ARMA")
    print("1. Cualquier tipo de arma")
    tiposArmas = input("Qué desea hacer? ")
    print("---------------------")
    rand = 0
    
    #Valor al azar de id de arma
    if int(tiposArmas) == 1:
        rand = randint(0,36)
    
    armaElegida = ARMAS[rand]
    print(" ")
    print("Datos de tu arma")
    armaElegida.printArma()
    print("---------------------")


    #Manejo de los atributos
    print(" ")
    print("APLICACION ATRIBUTOS")
    print("1. Cualquier tipo de atributos")
    tiposAtributos = input("Qué desea hacer? ")
    print("---------------------")

    for i in range(3):
        atributo = darAtributo(tiposAtributos, armaElegida)
        while atributo == None:
            atributo = darAtributo(tiposAtributos, armaElegida)
        print(" ")
        print("---------------------")
        atributo.printAtributo()
        time.sleep(2)

    print(" ")
    print("ARMA FINAL")
    armaElegida.printArma()
        
