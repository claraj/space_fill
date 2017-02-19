import math

'''Rename me - is the center bubble and spokes and polygon '''

class Bubble():

    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.color = c
        self.spokes = []
        self.polygon = []

        self.init_spokes()
        self.init_polygon()


    def init_spokes(self, count):

        circle = math.pi * 2
        angle = circle / count

        a = 0

        for spoke in range(count):
            s = Spoke(bubble, a)
            a += angle
            self.spokes.append(s)


    def init_polygon(self):

        for spoke in self.spokes:
            pt = (spoke.x, spoke.y)
            self.polygon.append(pt)


    def spokes_growing():
        growing = [ spoke.growing for spoke in self.spokes]
        return any(growing)


class Spoke():

    def __init__(self, angle, bubble):
        ''' x, y are root of spoke - same as bubble location it grows from '''
        self.x = bubble.x
        self.y = bubble.y
        self.angle = angle
        self.bubble = bubble
        self.growing = True

    def grow(self):

        # expand one growth unit in direction of angle
        dx = math.sin(angle)
        dy = math.cos(angle)
        self.x += dx
        self.y += dy


    def line():
        return Line(self.x, self.y, bubble.x, bubble.y)




class Line():

    def __init__(self, pt1_x, pt1_y, p2_x, pt2_y):
        self.pt1_x = pt
        self.pt1_y = pt1_y
        self.p2_x = pt2_x
        self.pt2_y = pt2_y


def intersect(line1, line2):
    pass
    # MATH HERE
