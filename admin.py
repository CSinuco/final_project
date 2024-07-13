#admin
class Admin:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def __init__(self, name):
        if not self._initialized:
            self.name = name
            self._initialized = True

    def create_branch(self, prototype, new_address):
        branch = prototype.clone()
        branch.direccion = new_address
        return branch