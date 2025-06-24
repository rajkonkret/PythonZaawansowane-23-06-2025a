import sys


class BezSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


bez_slots = BezSlots(1, 2)
print(bez_slots.x)
bez_slots.x = 90
print(bez_slots.x)
bez_slots.name = "Radek"
print(bez_slots.name)  # Radek


class ZeSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


ze_slots = ZeSlots(1, 2)
ze_slots.x = 90
print(ze_slots.x)
# ze_slots.z = 90 # AttributeError: 'ZeSlots' object has no attribute 'z' and no __dict__ for setting new attributes

a = [BezSlots(1,2) for _ in range(1_000_000)]
b = [ZeSlots(1,2) for _ in range(1_000_000)]

print("Bez slots:", sys.getsizeof(a[0].__dict__))
# print("slots:", sys.getsizeof(b[0].__dict__)) # AttributeError: 'ZeSlots' object has no attribute '__dict__'. Did you mean: '__dir__'?
print("slots:", sys.getsizeof(b[0])) # AttributeError: 'ZeSlots' object has no attribute '__dict__'. Did you mean: '__dir__'?
# Bez slots: 96
# slots: 48

total = sum(sys.getsizeof(x) + sys.getsizeof(x.__dict__) for x in a)
print("Total bez slots:", total)

total = sum(sys.getsizeof(x) for x in b)
print("Total ze slots:", total)
# Total bez slots: 144 000 000
# Total ze slots: 48 000 000