
from abc import ABC, abstractmethod
import copy
from state import FullState, EmptyState
from visitor import Visitor

class Tienda(ABC):
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.empty_state = EmptyState()
        self.full_state = FullState()
        self._state = self.empty_state

    @abstractmethod
    def mostrar_informacion(self):
        pass

    def clone(self):
        return copy.deepcopy(self)

    def set_state(self, state):
        self._state = state

    def check_state(self):
        self._state.handle(self)

    def accept(self, visitor: Visitor):
        visitor.visit(self)

class ConcreteBranch(Tienda):
    def __init__(self, nombre, direccion):
        super().__init__(nombre, direccion)

    def mostrar_informacion(self):
        return f"Tienda: {self.nombre}, Dirección: {self.direccion}"