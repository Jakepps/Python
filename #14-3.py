#14-3
import tkinter
from tkinter import filedialog
from tkinter import *


html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""

def savetxt():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write(entry_1.get())
        f.close()


def savehtml():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        f.write(html_template1)
        f.write(entry_1.get())
        f.write(html_template2)
        f.close()


window = tkinter.Tk()

window.title('Notepad')
window.geometry('320x200')

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Сохранить в txt", command=savetxt)
filemenu.add_command(label="Сохранить в html", command=savehtml)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=window.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

entry_1 = Entry(width=50, borderwidth=2, relief="solid")
entry_1.grid(row=0, column=1, pady=10, padx=10)
exet = Button(window, text='Выйти из программы', command=window.destroy)
exet.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

window.config(menu=menubar)
window.config(bg="gray")
window.mainloop()