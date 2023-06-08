import inspect


def plus(a, b):
    return a + b

def test1():
    assert plus(2, 2) == 4


def test():
    assert plus(100, 9) == 4


def test3():
    assert plus(-1, 1) == 0


def test4():
    assert plus(0, 0) == 0


g = globals().copy()
for k, v in g.items():
     if k.startswith('test') and inspect.isfunction(v)
         print(v)

