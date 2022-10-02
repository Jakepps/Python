#13-5
class Animal():
    def __init__(self):
        print("Родилось животное")


class Dog(Animal):
    name = ""

    def __init__(self, newName = ""):
        self.name = newName
        print("Родилась собака", self.name)
        Animal.__init__(self)

    def makeNoise(self):
        print(self.name, "говорит ГаВ")

class Cat(Animal):
    name = ""

    def __init__(self, newName = ""):
        self.name = newName
        print("Родился котик", self.name)
        Animal.__init__(self)

    def makeNoise(self):
        print(self.name, "говорит мЯу")

dude = Dog("Шарик")
dude.makeNoise()
duuude=Cat("Рыжик")
duuude.makeNoise()
