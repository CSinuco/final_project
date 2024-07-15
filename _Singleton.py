def singleton(cls):
    _instances={}
    def verify_singleton(*args,**kewargs):
        if cls not in _instances:
            _instances[cls]=cls(*args,**kewargs)
        return _instances[cls]
    return verify_singleton