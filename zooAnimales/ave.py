from .animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", colorPlumas = ""):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones += 1
        return halcon
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return aguila
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas