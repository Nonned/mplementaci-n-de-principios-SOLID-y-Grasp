from enum import Enum
from abc import abstractmethod

class Clubs (Enum):
    Club_natacion = 1
    Club_ciclismo = 2
    Club_atletismo = 3

class estudiantes ():
    def __init__(self, nombre):
        self.nombre = nombre

class membresia__ ():
    @abstractmethod
    def encontrar_esudiantes(self, club):
        pass

class membresia (membresia__):
    def __init__(self):
        self.Cmembresia = []
    
    def añadir_membresia(self, estudiante, club):
        self.Cmembresia.append((estudiante, club))
    
    def encontrar_esudiantes(self, club):
        for miembros in self.Cmembresia:
            if miembros[1] == club:
                yield miembros[0].nombre

class Busqueda ():
    def __init__(self, membresiaa):
        for estudiante in membresiaa.encontrar_esudiantes(Clubs.Club_natacion):
            print(f"{estudiante} está en el club de natación")

        for estudiante in membresiaa.encontrar_esudiantes(Clubs.Club_ciclismo):
            print(f"{estudiante} está en el club de ciclismo")  

        for estudiante in membresiaa.encontrar_esudiantes(Clubs.Club_atletismo):
            print(f"{estudiante} está en el club de atletismo")      
    

estudiante1 = estudiantes("Carlos")
estudiante2 = estudiantes("Juan")
estudiante3 = estudiantes("David")

membresia_club = membresia()
membresia_club.añadir_membresia(estudiante1, Clubs.Club_atletismo)
membresia_club.añadir_membresia(estudiante2, Clubs.Club_natacion)
membresia_club.añadir_membresia(estudiante3, Clubs.Club_ciclismo)
            

Busqueda(membresia_club)

























       
        


