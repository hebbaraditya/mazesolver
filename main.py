from tkinter import Tk, BOTH, Canvas
class Window(object):
    def __init__(self, width, height):
        self.__root = Tk()
        self.__title = root
        self.__canvas = None
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idealtasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while __running:
            self.redraw()
    
    def close(self):
        self.__running = False

def main():
    win = Window(800, 600)
    win.wait_for_close

main()