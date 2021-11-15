class mercedes:
    Precio = 10000
    Modelo = "x"
    def __init__(self, Costo, CModelo):
        self.Precio = Costo
        self.Modelo = CModelo
    def merced(self):
        print("la marca del coche es mercedes benz el precio del vehiculo es {}$".format(self.Precio), "y el modelo es {}.".format(self.Modelo))
Cliente = mercedes(100000, "G-wagon 2021")
Cliente.merced()

class mazda:
    Precio = 10000
    Modelo = "x"
    def __init__(self, Costo, CModelo):
        self.Precio = Costo
        self.Modelo = CModelo
    def maz(self):
        print("la marca del coche es mazda el precio del vehiculo es {}$".format(self.Precio), "y el modelo es {}.".format(self.Modelo))
Cliente = mazda(1000, "323 Coupe 1998")
Cliente.maz()

class MClaren:
    Precio = 10000
    Modelo = "x"
    def __init__(self, Costo, CModelo):
        self.Precio = Costo
        self.Modelo = CModelo
    def mc(self):
        print("la marca del coche es mercedes benz el precio del vehiculo es {}$".format(self.Precio), "y el modelo es {}.".format(self.Modelo))
Cliente = MClaren(1000000, "720s 2022")
Cliente.mc()