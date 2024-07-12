from branch_admin import Admin
from branch import ConcreteBranch

# Crear la instancia única de Admin
admin = Admin("Alice")

# Prototipo de la tienda principal
tienda_prototype = ConcreteBranch("Tienda Central", "Calle Principal 123")

# Crear nuevas sucursales usando el prototipo
sucursal1 = admin.create_branch(tienda_prototype, "Calle Secundaria 456")
sucursal2 = admin.create_branch(tienda_prototype, "Avenida Tercera 789")
print(sucursal1.mostrar_informacion())  # Output: Tienda: Tienda Central, Dirección: Calle Secundaria 456
print(sucursal2.mostrar_informacion())  # Output: Tienda: Tienda Central, Dirección: Avenida Tercera 789