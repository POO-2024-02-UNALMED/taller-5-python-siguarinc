from gestion import Zona

class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.total_animales += 1

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona = zona

    @staticmethod
    def getTotalAnimales():
        return Animal.total_animales

    @staticmethod
    def setTotalAnimales(total):
        Animal.total_animales = total

    @staticmethod
    def totalPorTipo():
        # Suponiendo que existen las clases Mamifero, Ave, Reptil, Pez y Anfibio
        return (f"Mamiferos: {Mamifero.cantidadMamiferos()}\n"
                f"Aves: {Ave.cantidadAves()}\n"
                f"Reptiles: {Reptil.cantidadReptiles()}\n"
                f"Peces: {Pez.cantidadPeces()}\n"
                f"Anfibios: {Anfibio.cantidadAnfibios()}")

    def __str__(self):
        if self.zona is None:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                    f"habito en {self.habitat} y mi género es {self.genero}")
        else:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                    f"habito en {self.habitat} y mi género es {self.genero}, "
                    f"la zona en la que me ubico es {self.zona}, en el {self.zona.getZoo()}")

    def movimiento(self):
        return "desplazarse"
    
class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def getListado():
        return Anfibio.listado

    @staticmethod
    def setListado(lista):
        Anfibio.listado = lista

    def getColorPiel(self):
        return self.colorPiel

    def setColorPiel(self, colorPiel):
        self.colorPiel = colorPiel

    def isVenenoso(self):
        return self.venenoso

    def setVenenoso(self, venenoso):
        self.venenoso = venenoso

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas
        Ave.listado.append(self)

    @staticmethod
    def getListado():
        return Ave.listado

    @staticmethod
    def setListado(lista):
        Ave.listado = lista

    def getColorPlumas(self):
        return self.colorPlumas

    def setColorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas

    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

    def movimiento(self):
        return "volar"

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @staticmethod
    def getListado():
        return Mamifero.listado

    @staticmethod
    def setListado(lista):
        Mamifero.listado = lista

    def isPelaje(self):
        return self.pelaje

    def setPelaje(self, pelaje):
        self.pelaje = pelaje

    def getPatas(self):
        return self.patas

    def setPatas(self, patas):
        self.patas = patas

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    @staticmethod
    def getListado():
        return Pez.listado

    @staticmethod
    def setListado(lista):
        Pez.listado = lista

    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self.cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self.cantidadAletas = cantidadAletas

    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def movimiento(self):
        return "nadar"

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)

    @staticmethod
    def getListado():
        return Reptil.listado

    @staticmethod
    def setListado(lista):
        Reptil.listado = lista

    def getColorEscamas(self):
        return self.colorEscamas

    def setColorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def getLargoCola(self):
        return self.largoCola

    def setLargoCola(self, largoCola):
        self.largoCola = largoCola

    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)

    def movimiento(self):
        return "reptar"