from state import Full, Empty

class Truck:
    def visit(self, store, state):
        state.handle(store)
