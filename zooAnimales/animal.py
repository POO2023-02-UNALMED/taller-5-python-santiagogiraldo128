class Animal():
    _totalAnimales = 0
    Mamiferos = 0
    Aves = 0
    Reptiles = 0
    Peces = 0
    Anfibios = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = "", zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    
    @classmethod
    def totalPorTipo(cls):
            return "Mamiferos : "+str(cls.Mamiferos)+"\n" + "Aves : "+str(cls.Aves)+"\n" + "Reptiles : "+str(cls.Reptiles)+"\n" + "Peces : "+str(cls.Peces)+"\n" + "Anfibios : "+str(cls.Anfibios)


    def toString(self):
        cadena = "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
        if self._zona != None:
            cadena = cadena + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona



    
