class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal.total_animales += 1

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

    @staticmethod
    def getTotalAnimales():
        return Animal.total_animales

    @staticmethod
    def setTotalAnimales(total):
        Animal.total_animales = total

    @staticmethod
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"
    def toString(self):
        if self._zona is None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi género es {self._genero}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi género es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.getZoo()}"

    def movimiento(self):
        return "desplazarse"
    
