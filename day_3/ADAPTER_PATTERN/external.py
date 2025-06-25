from mimetypes import inited


class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Wykonawca (muzyk) {self.name}"

    def play(self):
        return "gra muzykę!"


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Tancerka {self.name}"

    def play(self):
        return "Tańczy przy muzyce"
