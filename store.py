from observer import Subject
from state import Empty  # Importar Empty directamente aquí si es necesario

class Store(Subject):
    def __init__(self, address):
        super().__init__()
        self.address = address
        self.state = None

    def set_state(self, state):
        self.state = state
        self.notify_observers()

class ConcreteStore(Store):
    def __init__(self, address):
        super().__init__(address)

    def clone(self):
        return ConcreteStore(self.address)
