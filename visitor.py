from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, tienda):
        pass

class Camion(Visitor):
    def visit(self, tienda):
        print(f"Camion visitando la tienda {tienda.nombre} en {tienda.direccion}")
        tienda.set_state(tienda.full_state)