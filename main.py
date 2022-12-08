from tkinter import Tk, BOTH, Canvas
class Window(object):
    def __init__(self, width, height):
        self.__root = Tk()
        self.title = root
        self.canvas = None
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idealtasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(Line, fill_color):
        Line.draw(canvas, fill_color)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(Canvas, fill_color):
        canvas.create_line(
            x1, y1, x2, y2, fill_color, width = 2
        )

def main():
    win = Window(800, 600)
    win.wait_for_close

main()