#13-3
class StringVar():
    text = ""

    def __init__(self, newText):
        self.text = newText

    def set(self, newText):
        self.text = newText

    def get(self):
        return self.text

myString = StringVar("яре яре")

print(myString.get())
print("Уверен?")
myString.set(input("Попробуй еще раз\n"))
print(myString.get())