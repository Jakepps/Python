#12-9
def choice(grade):
    try:
        if grade=='A' or grade=='a':
            print("Оценка 5")
        elif grade=='B' or grade=='b':
            print("Оценка 4")
        elif grade=='C' or grade=='c':
            print("Оценка 3")
        elif grade=='D' or grade=='d':
            print("Оценка 2")
        elif grade=='F' or grade=='f':
            print("Отчислен.")
        elif grade=='5' or grade=='5':
            print("Оценка A")
        elif grade=='4' or grade=='4':
            print("Оценка B")
        elif grade=='3' or grade=='3':
            print("Оценка C")
        elif grade=='2' or grade=='2':
            print("Оценка D")
        elif grade=='Отчислен' or grade=="отчислен":
            print("Оценка F.")
    except SyntaxError:
        print("Неверный формат записи оценки.")

while True:
    g=input("Ввидите оценку=")
    print(choice(g))
    if not g:
        break  