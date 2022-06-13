#Importaciones necesarias
from atributo import Atributo

#Esta clase define el funcionamiento de un arma
class Arma:

    #Lista que guarda todos los daños, dado que escalan de manera diferente
    DAMAGES = [0,1,"1d4", "1d6", "1d8", "1d10", "1d12", "2d6", "1d20", "4d6"]
    damageType = "ligera"

    #En primer lugar, el inicializador de la clase
    def __init__(self, id, nombre, valor, damage, damageType,  peso, propiedades):
        self.id = id
        self.nombre = nombre
        self.valor = valor
        self.damage = damage
        self.damageType = str(damageType)
        self.peso = peso
        self.propiedades = propiedades
        self.atributos = []


    #Función que imprime los atributos del arma
    def printArma(self):
        print("- Arma: ", self.nombre)
        print("- Daño:", self.damage)
        print("- Tipo de daño:", self.damageType)
        print("- Peso:", self.peso)
        print("- Valor:", self.valor, "po")
        print("- Propiedades:", self.propiedades)

        strAtributos = []
        for atributo in self.atributos:
            strAtributos.append(atributo.nombre)
        print("- Atributos: ", str(strAtributos))
    
    #Agrega un atributo al arma
    def agregarAtributo(self, atributo):
        self.atributos.append(atributo)

    #Aplica el atributo al arma
    def aplicarAtributo(self, cambioDamage, tipoDamage, cambioValor, cambioPeso):
        
        #Para cambiar los daños
        posDanio = self.DAMAGES.index(self.damage)
        posDanio += cambioDamage

        #Por si el daño no se puede disminuir más
        if posDanio < 0:
            posDanio = 0

        #Por si el daño no se puede aumentar más
        if posDanio > 9:
            posDanio = 9
        
        self.damage = self.DAMAGES[posDanio]

        #Para cambiar el tipo de daño
        if(len(tipoDamage)>2):
            self.damageType = tipoDamage

        #Para cambiar el valor
        if cambioValor > 5 :
            self.valor += cambioValor
        elif cambioValor<=5 and cambioValor>0:
            self.valor *= cambioValor
        
        #Para cambiar el peso
        if(cambioPeso!="0"):
            self.peso = cambioPeso

    