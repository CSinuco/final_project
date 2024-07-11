#admin
class Admin:
    _instance = None
    #comprueba si no hay instancia la crea, si hay la retorna
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def __init__(self, name):
        if not self._initialized:
            self.name = name
            self._initialized = True
    #Retornamos el nombre del admin (futuramente aplicar el proxy)
    def display_name(self):
        return f"Admin name: {self.name}"