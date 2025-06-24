# metaklasy -
class MojaMeta(type):
    def __new__(cls, clsname, superclasses, attrs):
        """
        cls - klasa
        :param clsname:
        :param superclasses:
        :param attrs:
        """
        print(f"_____________ {cls.__class__.__name__} ______________")
        print(f"nazwa klasy: {clsname}")
        print(f"Klasy dziedziczone: {superclasses}")
        print(f"Słownik atrybutów klas: {attrs}")
        return type.__new__(cls, clsname, superclasses, attrs)

    def jedynka(cls):
        return 1


class S:
    pass


class F:
    """ Dokumentacja"""


class Specjalna(S, metaclass=MojaMeta):
    pass


# _____________ type ______________
# nazwa klasy: Specjalna
# Klasy dziedziczone: (<class '__main__.S'>,)
# Słownik atrybutów klas: {'__module__': '__main__', '__qualname__': 'Specjalna', '__firstlineno__': 28, '__static_attributes__': ()}

class B(Specjalna):
    pass


# _____________ type ______________
# nazwa klasy: B
# Klasy dziedziczone: (<class '__main__.Specjalna'>,)
# Słownik atrybutów klas: {'__module__': '__main__', '__qualname__': 'B', '__firstlineno__': 32, '__static_attributes__': ()}

class C(F, B):
    @property
    def info(self):
        print("abc...")


# _____________ type ______________
# nazwa klasy: C
# Klasy dziedziczone: (<class '__main__.F'>, <class '__main__.B'>)
# Słownik atrybutów klas: {'__module__': '__main__', '__qualname__': 'C', '__firstlineno__': 36, 'info': <property object at 0x000001BCDC5FB790>, '__static_attributes__': ()}

cf = C()
# print(cf.jedynka())  # AttributeError: 'C' object has no attribute 'jedynka'

cg = C
print(cg.jedynka())  # 1
