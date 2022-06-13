#Clase que modela los atrihutos de las armas y los valores que afectan
class Atributo:

    # En primer lugar, el inicializador de la clase
    def __init__(self, id, nombre, descripcion, afectacionValor, afectacionDanio, afectacionTipoDanio, afectacionPeso, armasIncompatibles, atributosIncompatibles):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.afectacionValor = afectacionValor
        self.afectacionDanio = afectacionDanio
        self.afectacionTipoDanio = afectacionTipoDanio
        self.afectacionPeso = afectacionPeso
        self.armasIncompatibles = armasIncompatibles
        self.atributosIncompatibles = atributosIncompatibles

    # Imprime los datos del atributo
    def printAtributo(self):
        print("- Nombre: ", self.nombre)
        print("- Descripcion: ", self.descripcion ) 
        print("- Afectación al daño: ", self.afectacionDanio if (self.afectacionDanio!=0) or (self.afectacionDanio!="0") else 'ninguna')
        print("- Afectación al tipo daño: ", self.afectacionTipoDanio if self.afectacionTipoDanio!="-" else 'ninguna')
        print("- Afectación al costo: ", self.afectacionValor if (self.afectacionValor!=0) or (self.afectacionValor!="0") else 'ninguna')
        print("- Afectación al peso: ", self.afectacionPeso if (self.afectacionValor!=0) or (self.afectacionPeso!="0") else 'ninguna')