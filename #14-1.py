#14-1
import tkinter
def click():
    faren = entry.get()
    try:
        res = (float(faren) - 32) / 1.8
        label.config(text=res)
    except:
        label.config(text="Ошибка, введите число!")

window = tkinter.Tk()
window.title("Перевод градусы в Фаренгейты")
window.geometry('200x100+700+200')
window.config(bg="white")
frame = tkinter.Frame(window)
frame.pack(side='top')
entry = tkinter.Entry(frame)
entry.pack(side='top')
label = tkinter.Label(frame)
label.pack(side='top')
button = tkinter.Button(frame, text='Коневертировать!', command=click)
button.pack(side='top')
exet = tkinter.Button(window, text='Выйти из программы', command=window.destroy).pack(side='top')
window.mainloop()