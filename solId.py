from abc import abstractclassmethod, abstractmethod


class Pajaro ():
    name = "x"
    def __init__(self, nombre):
        self.name = nombre

    @abstractmethod
    def hacer_sonido(self)->str:
        pass

class Pajaro_vuela (Pajaro):
    @abstractmethod
    def volar (self):
        pass

class Pajaro_nada(Pajaro):
    @abstractmethod
    def nadar(self):
        pass

class cuervo(Pajaro_vuela):
    raza = "y"
    def __init__(self, especie):
        self.raza = especie
    def volar(self):
        print("{} esta volando alto y rápido.".format(self.raza))
    def hacer_sonido(self) -> str:
        return "caw"

pajaro2 = cuervo("El cuervo")
pajaro2.volar()

class pato(Pajaro_nada, Pajaro_vuela):
    def volar(self):
        print("{} esta volando pero no muy alto".format(self.name))
    def nadar(self):
        print("{} nada en el lago y hace quack".format(self.name))
    def hacer_sonido(self)-> str:
        return "quack"

pajaro1 = pato("El ave")
pajaro1.volar()
pajaro1.nadar()
pajaro1.hacer_sonido()