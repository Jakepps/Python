#13-7
class Animal():
    name = ""
    def __init__(self,newName):
        self.name = newName
    def setName(self, newName):
        self.name = newName
    def getName(self):
        print(self.name)


class Dog(Animal):
    def makeNoise(self):
        print(self.name, "говорит Гав")
    def eat(self):
        print(self.name, "скушал корм")

class Cat(Animal):

    def makeNoise(self):
        print(self.name, "говорит мяу")
    def eat(self):
        print(self.name, "скушал воробья")

class Student(Animal):
    def makeNoise(self):
        print(self.name, "говорит еще посплю пару минут")
    def eat(self):
        print(self.name, "скушала доширак")


dogname = Dog("Шарик")
dogname.setName("Лопух")
dogname.getName()
dogname.eat()
dogname.makeNoise()

catname = Cat("Рыжик")
catname.setName("Черныш")
catname.getName()
catname.eat()
catname.makeNoise()

Serega = Student("Серега")
Serega.getName()
Serega.eat()
Serega.makeNoise()