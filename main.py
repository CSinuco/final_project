from admin import Admin
from store import ConcreteStore
from state import Full, Empty
from visitor import Truck
from client import Client

def main():
    # Crear admin y prototipos de tiendas
    admin = Admin()
    store_prototype = ConcreteStore("Prototype Address")
    admin.register_prototype("ConcreteStore", store_prototype)

    # Crear una tienda concreta
    store1 = admin.create_store("ConcreteStore", "123 Main St")
    store2 = admin.create_store("ConcreteStore", "456 Oak St")

    # Crear cliente y agregarlo como observador
    client = Client()
    store1.add_observer(client)
    store1.add_observer(admin)

    # Crear camion y cambiar estados
    truck = Truck()

    # Llenar la tienda
    truck.visit(store1, Full())
    # Vaciar la tienda
    truck.visit(store1, Empty())

if __name__ == "__main__":
    main()

