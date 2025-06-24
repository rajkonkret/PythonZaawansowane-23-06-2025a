class LogDelete:
    def __init__(self, default=None):
        self.default = default
        self.value = default

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        print(f"Ustawienie wartości: {value}")
        self.value = value

    def __delete__(self, instance):
        print(f"Usuwanie atrybutu. Poprzednia wartość: {self.value}")
        self.value = self.default


class MojLog:
    x = LogDelete(0)
    y = LogDelete("brak")
