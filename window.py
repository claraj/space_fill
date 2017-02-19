from tkinter import Tk, Canvas, Frame, Scale, Button, BOTH, X, HORIZONTAL
import sys
import bubble
from geometry import Point

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
        self.canvas.bind('<Button-1>', canvas_click)

        self.draw(self.canvas)

        scale = Scale(self, from_=10, to=100, orient=HORIZONTAL)
        scale.pack()

        go_button = Button(self, text="Go", command=go)
        go_button.pack()

        quit_button = Button(self, text="Quit", command=quit)
        quit_button.pack()

        self.pack()


    def draw(self, canvas):

        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(15.5, 25.5, 200.5, 25.5, fill="red")

        canvas.pack(fill=BOTH, expand=1)
        canvas.pack()


def canvas_click(event):
    global color

    if len(points) >= len(colors):
        print('max points, no more.')
        return

    color = (color+1) % len(colors)
    print(color)
    print(event.x, event.y)
    win.canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, fill=colors[color])
    p = Point(event.x, event.y, colors[color])
    points.append(p)
    print(points)


def go():
    print("click!")
    bubble.start_bubbles(points, update)


def update(points_and_spokes):
    print('update msg')
    # Draw all lines

    for point in points:
        # draw points
        for spoke in point.spokes:
            #draw spoke
            win.canvas.drawline(point.x, point.y, spoke.x, spoke.y, fill=point.color)


def quit():
    sys.exit()


color = 0
colors = ['red', 'orange', 'yellow', 'green', 'blue']

points = []

win = None

def main():
    global win
    root = Tk()
    win = Window(root)
    root.geometry("400x250+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()
