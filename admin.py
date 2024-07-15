#admin
from _Singleton import singleton
@singleton
class Admin:
    def __init__(self, name):
        self.name = name

    def create_branch(self, prototype, new_address):
        branch = prototype.clone()
        branch.direccion = new_address
        return branch