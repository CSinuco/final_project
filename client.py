from observer import Observer
from state import Full

class Client(Observer):
    def update(self, subject):
        if isinstance(subject.state, Full):
            print(f"Client Notification: Store at {subject.address} is full.")
