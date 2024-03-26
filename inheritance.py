class Animal:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
    def breath(self):
        print("Inhale, Exhale")
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Under_water")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.breath()

