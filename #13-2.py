#13-2
from unicodedata import name


class Animal():
    name = ""

    def eat(self):
        print("Намнём")
        print(self.name,"покушал")

    def __init__(self, newName):
        self.name = newName
        print("Родилось животное ", self.name)

    def set_name(self, newName):
        self.name = newName

    def get_name(self):
        return self.name

    def makeNoise(self):
        print(self.name, "говорит игого")


horse = Animal("Плотва")
print("Имя лошади -> ", horse.get_name())
print("Геральт никогда не меняет имя лошедям. Но вы можете!")
horse.set_name(input())
horse.eat()
horse.makeNoise()