#14-2
import random
import tkinter
from tkinter import *

def click_try():
    global k
    var = entry_1.get()
    if label_2.cget("text") != "":
        if var.isalpha():
            if k != 0:
                if var == dictionary[rus]:
                    label_5.config(text="Ответ правильный!")
                    k = 5
                else:
                    label_5.config(text="Ответ неправильный! Попыток:" + str(k))
                    k -= 1
            else:
                label_5.config(text="Ответ неправильный! Попыток не осталось! Сгенерируйте новое слово")
                click_rand()
                k = 5
        else:
            label_5.config(text="Ошибка ввода! Введите слово заново!")
    else:
        label_5.config(text="Вы не сгенерировали слово!")


def click_rand():
    global rus, eng
    rus, eng = random.choice(list(dictionary.items()))
    label_2.config(text=rus)


window = tkinter.Tk()
window.title("Угадай слово")

dictionary = {"яблоко": "apple",
              "база": "base",
              "питон": "python",
              "лучший язык программирования": "C#",
              "персик": "peach",
              "арбуз": "watermelon",
              "лимон": "lemon",
              "Доппио": "Diavolo",
              }

window.config(bg="gray")
window.geometry('500x300')

k = 5
rus = ""
eng = ""
label_1 = Label(text="Случайное слово->", width=30, borderwidth=2, relief="solid")
label_1.grid(row=0, column=0, pady=10, padx=10)

label_2 = Label(width=30, borderwidth=2, relief="solid")
label_2.grid(row=0, column=1, pady=10, padx=10)

label_3 = Label(text="Ответ->", width=30, borderwidth=2, relief="solid")
label_3.grid(row=3, column=0, pady=10, padx=10)

entry_1 = Entry(width=30, borderwidth=2, relief="solid")
entry_1.grid(row=3, column=1, pady=10, padx=10)

button_1 = Button(text="Сгенерировать", width=30, command=lambda: click_rand())
button_1.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

button_2 = Button(text="Проверка", width=30, command=lambda: click_try())
button_2.grid(row=4, column=0, columnspan=3, pady=10, padx=10)

label_5 = Label(width=60, height=3, borderwidth=2, relief="solid")
label_5.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

exet = Button(window, text='Выйти из программы', command=window.destroy)
exet.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

exet = Button(window, text='Выйти из программы', command=lambda: window.destroy)
window.mainloop()