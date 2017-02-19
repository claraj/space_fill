from tkinter import Tk, Canvas, Frame, Scale, Button, BOTH, LEFT, X, HORIZONTAL
import sys
import random
import time
from threading import Thread
# Helpful: http://zetcode.com/gui/tkinter/drawing/

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.parent.title('Bubble Fill')
        self.pack(fill=X, expand=1)

        self.canvas = Canvas(self)

        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.pack()

        go_button = Button(self, text="Go", command=go)
        go_button.pack(side=LEFT)

        quit_button = Button(self, text="Quit", command=quit)
        quit_button.pack(side=LEFT)

        self.pack()


def go():
    print("go click!")
    start(update)


def update():
    print('update message received')
    #draw random line
    win.canvas.create_line(random.randint(1, 300), random.randint(1, 300), random.randint(1, 300), random.randint(1, 300), fill="green")

def quit():
    sys.exit()

def start(callback):

    # for a in range(5):
    task_thread = Thread(target=dotask, args=[callback])
    task_thread.start()


count = 1

def dotask(callback):
    global count
    print('do task')
    time.sleep(1)
    callback()
    count +=1

    if count <= 5:
        print('start thread')

        task_thread = Thread(target=dotask, args=[callback])
        task_thread.start()

    else:
        print('done')


win = None

def main():
    global win
    root = Tk()
    win = Window(root)
    root.geometry("300x300")
    root.mainloop()

if __name__ == '__main__':
    main()
