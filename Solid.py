
class chevrolet:
    caballos = 100
    sillas = 2
    Puertas = 3
    combustible = 0
    modelo = "spark"
    def __init__(self, combRest, modeloChevy):
        self.combustible = combRest
        self.modelo = modeloChevy
    def movimiento(self):
        print("El coche {} está en movimiento".format(self.modelo))
        print("Quedan {} litros de combustible".format(self.combustible))    

Chevy1 = chevrolet(60, "Aveo")
Chevy2 = chevrolet(100, "optra")

Chevy1.movimiento()
Chevy2.movimiento()



class precio_chevy:
    Presupuestob_cliente = 1000
    modelo = "x"
    costo = 1000
    def __init__(self, presupuesto_cliente, modelo_cliente, costo_modelo):
        self.Presupuestob_cliente = presupuesto_cliente
        self.modelo = modelo_cliente
        self.costo = costo_modelo
    def precio(self):
        print("El modelo {}".format(self.modelo),"tiene un costo de {}$".format(self.costo), "y su presupuesto es de {}$".format(self.Presupuestob_cliente))
    
Cliente1 = precio_chevy(2500, "Spark", 1000)
Cliente2 = precio_chevy(10000, "Camaro", 10000)
Cliente3 = precio_chevy(5000, "Aveo", 2500)

Cliente1.precio()
Cliente2.precio()
Cliente3.precio()  
