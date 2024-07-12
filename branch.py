
from abc import ABC, abstractmethod
import copy

class Tienda(ABC):
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass

    def clone(self):
        return copy.deepcopy(self)

class ConcreteBranch(Tienda):
    def __init__(self, nombre, direccion):
        super().__init__(nombre, direccion)

    def mostrar_informacion(self):
        return f"Tienda: {self.nombre}, Dirección: {self.direccion}"