#13-4
class Point():
    pos_x = 0
    pos_y = 0

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def show_pos(self):
        print("Координаты точки:", self.pos_x, "-", self.pos_y)

    def setPosX(self, x):  
        self.pos_x = x

    def setPosY(self, y):  
        self.pos_y = y

    def setPoint(self, x, y): 
        self.pos_x = x
        self.pos_y = y

    def del_pos(self):  
        self.pos_x = 0
        self.pos_y = 0


newP = Point(1, 4)
newP.show_pos()
newP.del_pos()
newP.show_pos()
newP.setPosX(10)
newP.show_pos()
newP.setPosY(10)
newP.show_pos()
newP.setPoint(12, 20)
newP.show_pos()
newP.del_pos()
newP.show_pos()