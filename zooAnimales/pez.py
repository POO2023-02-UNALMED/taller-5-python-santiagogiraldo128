from .animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorEscamas = "", cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)
        Animal.Peces += 1

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre = "", edad = 0, genero = ""):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo" , 6)
        cls.salmones += 1
        return salmon
    
    @classmethod
    def crearBacalao(cls, nombre = "", edad = 0, genero = ""):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris" , 6)
        cls.bacalaos += 1
        return bacalao
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

