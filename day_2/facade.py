# Facade - ukrycie zbędnych elementów projektu przed widokiem dla końcowego użytkownika
from enum import Enum
from abc import ABCMeta, abstractmethod, ABC

State = Enum("State", "new running sleeping restart zombie")


class User:
    pass


class Process:
    pass


class File:
    pass


# class Server(metaclass=ABCMeta):
class Server(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self):
        self.name = "FileServer"
        self.stats = State.new

    def boot(self):
        print(f"Bootowanie systemu {self}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"Usuwanie {self}")
        self.state = State.restart if restart else State.zombie

    def create_file(selfself, user, name, permission):
        print(f"Próba utworzenia pliku {name} dla użytkownika {user} z uprawnieniami: {permission}.")


class ProcessServer(Server):

    def __init__(self):
        self.name = "ProcessServer"
        self.state = State.new

    def boot(self):
        print(f'Bootowanie systemu {self}')
        self.status = State.running

    def kill(self, restart=True):
        print(f"Usuwanie {self}")
        self.state = State.restart if restart else State.zombie

    def create_process(selfself, user, name):
        print(f"Próba utworzenia procesu {name} dla użytkownika {user}.")


class WindoServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permission):
        return self.fs.create_file(user, name, permission)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('abc', 'hello', '=rw-r-r')
    os.create_process('bar', 'ls/tmp')


if __name__ == '__main__':
    main()
# Bootowanie systemu FileServer
# Bootowanie systemu ProcessServer
# Próba utworzenia pliku hello dla użytkownika abc z uprawnieniami: =rw-r-r.
# Próba utworzenia procesu ls/tmp dla użytkownika bar.
