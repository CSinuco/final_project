from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, tienda):
        pass

class FullState(State):
    def handle(self, tienda):
        print(f"La tienda {tienda.nombre} en {tienda.direccion} está llena de productos.")
        tienda.set_state(self)

class EmptyState(State):
    def handle(self, tienda):
        print(f"La tienda {tienda.nombre} en {tienda.direccion} está vacía de productos.")
        tienda.set_state(self)