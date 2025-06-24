import datetime


# obiekt klasy stał się funkcją

class Greeting:
    def __call__(self, hour_=None):
        if hour_ is None:
            hour_ = datetime.datetime.now().hour

        if 5 <= hour_ < 12:
            return "Dzień dobry"
        elif 12 <= hour_ < 18:
            return "Miłego popołudnia"
        elif 18 <= hour_ < 22:
            return "Dobry wieczór"
        else:
            return "Dobranoc"


greet = Greeting()
print(greet)  # <__main__.Greeting object at 0x00000211B7C96E40>

print(greet())  # Miłego popołudnia
print(greet(10))  # Dzień dobry
print(greet(17))  # Miłego popołudnia
print(greet(23))  # Dobranoc
