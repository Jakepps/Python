#13-1
class Cat():
    name = ""
    color = ""
    weight = 0

    def meow(self):
        print(self.name, "мяукнул")


myCat = Cat()
myCat.name = "Мурзик"
myCat.color = "рыжий"
myCat.weight = 4
myCat.meow()

