class State:
    pass

class Full(State):
    def handle(self, store):
        store.set_state(self)
        print("Store is now full.")

class Empty(State):
    def handle(self, store):
        store.set_state(self)
        print("Store is now empty.")
