class SingleOne(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(SingleOne, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(SingleOne):
    s = 1

class SingleTwo(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(SingleTwo, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

class MyClassTwo(SingleTwo):
    s = 1

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 101
        print(num)
    inner()
    print(num)
outer()