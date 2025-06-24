# Singleton - dba o to by była jedna instancja klasy

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Regular:
    pass


r1 = Regular()
r2 = Regular()

print("------ klasa regularna -> dwa różne obiekty -----------")
print(r1 == r2)  # False
print(r1 is r2)  # False
print(id(r1))  # 2549896933264
print(id(r2))  # 2549899955088


class Sing(metaclass=Singleton):
    def __init__(self, kolor):
        self.kolor = kolor


s1 = Sing("czerwony")
s2 = Sing("niebieski")

print("------- Klasa Singleton -> dwa takie same obiekty -------")
print(s1 == s2)
print(s1 is s2)
print(s1)
print(s2)
# <__main__.Sing object at 0x0000020097FB70E0>
# <__main__.Sing object at 0x0000020097FB70E0>
print(id(s1))  # 2209570779360
print(id(s2))  # 2209570779360

print(s1.kolor)
print(s2.kolor)
# czerwony
# czerwony

