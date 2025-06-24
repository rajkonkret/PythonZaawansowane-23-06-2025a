class ClassRegistry(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        cls.registry[name] = new_class
        return new_class

    @classmethod
    def get_registred_classes(cls):
        return cls.registry

    @classmethod
    def get_bases_classes(cls):
        return cls.__bases__


class BaseClass(metaclass=ClassRegistry):
    pass


class FirstClass(BaseClass):
    pass


class SecondClass(BaseClass):
    pass


class ThirdClass(BaseClass):
    pass


class EmptyClass(metaclass=ClassRegistry):
    pass


print(f"""Wynik działnia metaklasy ClassRegistry:
{ClassRegistry.get_registred_classes()}""")
# {'BaseClass': <
#
#
# class '__main__.BaseClass'>, 'FirstClass': <
#
#
#     class '__main__.FirstClass'>, 'SecondClass': <
#
#
#     class '__main__.SecondClass'>, 'ThirdClass': <
#
#
#     class '__main__.ThirdClass'>, 'EmptyClass': <
#
#
#     class '__main__.EmptyClass'>}

print("Przodkowie klasy:", ClassRegistry.get_bases_classes())  # Przodkowie klasy: (<class 'type'>,)
