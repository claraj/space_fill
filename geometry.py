import math
import random


class Bubble:


    def __init__(self, x, y, c, spokes):
        self.x = x
        self.y = y
        self.color = c
        self.spokes = []
        self.polygon = []

        self.init_spokes(spokes)


    def __str__(self):
        return '%s bubble' % self.color


    def init_spokes(self, count):

        circle = math.pi * 2
        angle = circle / count

        a = 0

        for spoke in range(count):
            s = Spoke(a, self.x, self.y, spoke)
            a += angle
            self.spokes.append(s)


    def update_polygon(self):

        self.polygon = []
        for spoke in self.spokes:
            pt = (spoke.x, spoke.y)
            self.polygon.append(pt)
        return self.polygon


    def grow_all_spokes(self):
        for spoke in self.spokes:
            spoke.grow()


    def spokes_growing(self):
        growing = [spoke.growing for spoke in self.spokes]
        return any(growing)


    def active_spokes(self):
        growing_spokes = [spoke for spoke in self.spokes if spoke.growing]
        return growing_spokes


    def check_spokes(self, other_bubbles, frame_segs):

        print('number spokes active for ', self , 'is', len(self.active_spokes()))

        if not self.spokes_growing():
            return

        # for every other bubble
        for other_bubble in other_bubbles:
            polygon = other_bubble.update_polygon()

            for spoke in self.active_spokes():

                if spoke.growing:

                    for p in range(len(polygon)):    # A polyseg is a list of (x,y) tuples, one per points
                        polyseg = polygon[p]
                        next_polyseg = polygon[(p+1) % len(polygon) ]  # Wrap

                        if intersect(spoke, polyseg, next_polyseg):
                            print('INTERSECT detected stopping spoke')
                            spoke.stop()

        for spoke in self.active_spokes():
            if intersect_frame(spoke, frame_segs):
                print('INTERSECT with frame detected stopping spoke')
                spoke.stop()



class Spoke:

    def __init__(self, angle, bubble_x, bubble_y, id):
        """ x, y are root of spoke - same as bubble location it grows from """
        self.x = bubble_x
        self.y = bubble_y
        self.angle = angle
        self.bubble_x = bubble_x
        self.bubble_y = bubble_y
        self.growing = True
        self.id = id


    def grow(self):

        if self.growing:
            # expand one growth unit in direction of angle
            dx = math.sin(self.angle)
            dy = math.cos(self.angle)
            self.x += dx
            self.y += dy


    def stop(self):
        self.growing = False
        print('spoke stop')


    def __str__(self):
        return 'Spoke %d base %f %f tip %f %f growing? %s', self.id, self.bubble_x, self.bubble_y, self.x, self.y, self.growing


def intersect_frame(spoke, frames):

    # Convert frame into polysegs, call intersect

    for f in range(len(frames)):

        this_frame = frames[f]
        next_frame = frames[(f+1) % len(frames)]

        if intersect(spoke, this_frame, next_frame):
            return True

    return False



def atan(opp, adj):

    if opp == 0 and adj == 0:
        return 0

    if opp >= 0 and adj >= 0:     # both pos. correct(?)
        if adj == 0:
            return math.pi / 2
        else:
            return math.atan(opp / adj)

    if opp >= 0 and adj < 0:    # opp positive, adj negative

        if opp == 0:
            return math.pi
        small = math.atan(adj/opp)
        return (math.pi/2) + abs(small)

    if opp < 0 and adj < 0:   # both neg

        return math.atan(opp/adj) + math.pi   # add 180 deg

    if opp < 0 and adj >= 0:    # opp negative, adj positive

        if adj == 0:
            return 1.5 * math.pi

        small = math.atan(adj/opp)
        return (math.pi * 1.5) + abs(small)



def on_both_sides(base, angle, pt1, pt2):

    # Shift to put base at (0,0)

    dx = 0 - base[0]
    dy = 0 - base[1]

    pt1_x = pt1[0] + dx
    pt1_y = pt1[1] + dy

    pt2_x = pt2[0] + dx
    pt2_y = pt2[1] + dy

    pt1angle = atan(pt1_x, pt1_y)
    pt2angle = atan(pt2_x, pt2_y)


    # Subtract angle from both

    norm_pt1angle = (pt1angle - angle) % (2 * math.pi)
    norm_pt2angle = (pt2angle - angle) % (2 * math.pi)

    # If intersect, then spoke_base_angle will be between 0 and PI
    # and spoke_tip_angle will be between PI and 2PI. Or vice-versa
    # Both 0 or both PI ok too

    a1 = min(norm_pt1angle, norm_pt2angle)
    a2 = max(norm_pt1angle, norm_pt2angle)

    if a1 < 0 or a1 > math.pi:
        # Nope, outside range 0 - PI
        # print('false smaller angle not on range 0-pi', a1, a2)
        return False

    if a2 < math.pi or a2 > math.pi * 2:
        # Nope, outside range PI-2*PI
        # print('false larger angle not in range pi-2pi', a1, a2)
        return False

    return True


def intersect(spoke, poly_seg_1, poly_seg_2):

    ''' Spoke has spoke.x and spoke.y, the coords of one end, the tip
    spoke.bubble_x , spoke.bubble_y coords of the end
    spoke.angle, angle in rads

    poly_seg_1 and poly_seg_2 are tuples (x, y) of each point in the polygon segment.

    '''

    # redundant?
    if spoke.x == poly_seg_1[0] and spoke.y == poly_seg_1[1]:
        # print('intersct spoke tip x and polyseg1')
        return True

    if spoke.x == poly_seg_2[0] and spoke.y == poly_seg_2[1]:
        # print('intersct spoke tip and polyseg2')
        return True


    if spoke.bubble_x == poly_seg_1[0] and spoke.bubble_y == poly_seg_1[1]:
        # print('intersct spoke base x and polyseg1')
        return True

    if spoke.bubble_x == poly_seg_2[0] and spoke.bubble_y == poly_seg_2[1]:
        # print('intersect spoke base  and polyseg2')
        return True

    # TODO check for parallel lines ?


    # Calculate angle of poly segment

    dx = poly_seg_1[0] - poly_seg_2[0]
    dy = poly_seg_1[1] - poly_seg_2[1]

    poly_angle = atan(dx, dy)  # Check

    spoke_base = (spoke.bubble_x, spoke.bubble_y)
    spoke_tip = (spoke.x, spoke.y)

    polyseg_both_sides_of_spoke = on_both_sides(spoke_base, spoke.angle, poly_seg_1, poly_seg_2)
    
    spoke_both_sides_of_polyseg = on_both_sides(poly_seg_1, poly_angle, spoke_base, spoke_tip)


    if polyseg_both_sides_of_spoke and spoke_both_sides_of_polyseg:
        return True
    
    return False 

