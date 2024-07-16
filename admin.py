#admin
from observer import Observer
from store import ConcreteStore
from state import Empty  # Importar Empty directamente aquí si es necesario

class Admin(Observer):
    _instance = None
    _prototypes = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Admin, cls).__new__(cls)
        return cls._instance

    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype

    def create_store(self, name, address):
        prototype = self._prototypes.get(name)
        if prototype:
            store = prototype.clone()
            store.address = address
            return store
        return None

    def update(self, subject):
        if isinstance(subject.state, Empty):
            self.notify(f"Store at {subject.address} is empty.")

    def notify(self, message):
        print(f"Admin Notification: {message}")
