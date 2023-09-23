from .animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorPiel = "", venenoso = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        Animal.Anfibios += 1

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre = "", edad = 0, genero = ""):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre = "", edad = 0, genero = ""):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso



