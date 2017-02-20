from tkinter import Tk, Canvas, Frame, Scale, Button, BOTH, LEFT, X, HORIZONTAL, DISABLED
import sys
import bubble
from geometry import Bubble
import threading

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

        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.pack()

        #self.draw(self.canvas)

        scale = Scale(self, from_=10, to=100, orient=HORIZONTAL)
        scale.pack(side=LEFT)

        self.go_button = Button(self, text="Go", command=go)
        self.go_button.pack(side=LEFT)

        quit_button = Button(self, text="Quit", command=quit)
        quit_button.pack(side=LEFT)

        self.pack()


    def draw(self, canvas):

        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(15.5, 25.5, 200.5, 25.5, fill="red")


def canvas_click(event):
    global color

    if len(bubbles) >= len(colors):
        print('max bubbles, no more.')
        return

    color = (color+1) % len(colors)
    print(color)
    print(event.x, event.y)
    win.canvas.create_rectangle(event.x-1, event.y-1, event.x, event.y, fill=colors[color])
    b = Bubble(event.x, event.y, colors[color])
    bubbles.append(b)
    print(bubbles)


def go():

    x = int(win.canvas['width'])
    y = int(win.canvas['height'])

    print("go!", x, y)
    win.go_button['state'] = DISABLED


    frame = [(0, 0), (0, y), (x, 0), (x, y)]
    bubble.start_bubbles(bubbles, frame, update, done)


def update(bubbles_and_spokes):
    print('update message received')
    # Draw all lines
    print('threads running = ', threading.active_count())

    for bub in bubbles_and_spokes:
        # draw bubbles
        for spoke in bub.spokes:
            # draw spoke
            win.canvas.create_line(bub.x, bub.y, spoke.x, spoke.y, fill=bub.color)


def done(bubbles_and_spokes, iters):
    print('done after %d iterations' % iters)
    # Draw all lines
    # draw polygons
    # output list of polygon point for each bubble

    print('Polygon Coordinates')


    for bub in bubbles_and_spokes:


        polygon = bub.update_polygon()
        print('--------------------------------------------------------')
        print(bub.x, bub.y)
        print(polygon)

        # draw bubbles
        for p in range(len(polygon)):    # A polyseg is a list of (x,y) tuples, one per points
            # draw spoke
            polyseg = polygon[p]
            next_polyseg = polygon[(p+1) % len(polygon)]  # Wrap
            x = polyseg[0]
            y = polyseg[1]
            next_x = next_polyseg[0]
            next_y = next_polyseg[1]


            # print(x, y, next_x, next_y)

            win.canvas.create_line(x, y, next_x, next_y, fill=bub.color)

        print('--------------------------------------------------------')



def quit():
    sys.exit()


color = 0
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'magenta', 'cyan']

bubbles = []

win = None

width = 400
height = 250

def main():
    global win
    root = Tk()
    win = Window(root)



    root.geometry("%dx%d" % (width, height))
    root.mainloop()

if __name__ == '__main__':
    main()
