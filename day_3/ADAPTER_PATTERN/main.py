from external import Musician, Dancer


class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Klub {self.name}"

    def organize_event(self):
        return "Koncert muzyczny z oprawą taneczną!"


class Adapter:
    def __init__(self, obj, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Club("Jazz Cafe"), Musician("Black Rain"), Dancer("Mary B")]
    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            if hasattr(obj, 'play'):
                adapted_method = dict(organize_event=obj.play)
            elif hasattr(obj, 'dance'):
                adapted_method = dict(organize_event=obj.dance)
            obj = Adapter(obj, adapted_method)
        print(f'{obj} {obj.organize_event()}')


if __name__ == '__main__':
    main()
