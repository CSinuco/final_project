from admin import Admin
from tienda import Branch
from state import FullState, EmptyState
from visitor import Camion

# Crear la instancia única de Admin
admin = Admin("Alice")

# Prototipo de la tienda principal
tienda_prototype = Branch("Tienda Central", "Calle Principal 123")

# Crear nuevas sucursales usando el prototipo
sucursal1 = admin.create_branch(tienda_prototype, "Calle Secundaria 456")
sucursal2 = admin.create_branch(tienda_prototype, "Avenida Tercera 789")

# Verificar estados iniciales de las sucursales
sucursal1.check_state()  # Output: La tienda Tienda Central en Calle Secundaria 456 está vacía de productos.
sucursal2.check_state()  # Output: La tienda Tienda Central en Avenida Tercera 789 está vacía de productos.

# Crear instancia de Camion (Visitor)
camion = Camion()

# El Camion visita las sucursales y cambia su estado a lleno
sucursal1.accept(camion)
sucursal2.accept(camion)

# Verificar estados después de la visita del Camion
sucursal1.check_state()  # Output: La tienda Tienda Central en Calle Secundaria 456 está llena de productos.
sucursal2.check_state()  # Output: La tienda Tienda Central en Avenida Tercera 789 está llena de productos.