import math
import random
'''Rename me - is the center bubble and spokes and polygon '''


class Bubble():

    SPOKE_COUNT = 10

    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.color = c
        self.spokes = []
        self.polygon = []

        self.init_spokes()
        #self.init_polygon()


    def __str__(self):
        return '%s bubble' % self.color

    def init_spokes(self):

        count = self.SPOKE_COUNT

        circle = math.pi * 2
        angle = circle / count

        a = 0

        for spoke in range(count):
            s = Spoke(a, self.x, self.y)
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
        #print('any spokes growing?? ', growing)
        return any(growing)


    def check_spokes(self, other_bubbles, frame_segs):

        #print('check spokes')

        if not self.spokes_growing():
            return

        # for every other bubble
        for other_bubble in other_bubbles:
            # print('check bubbles')
            polygon = other_bubble.update_polygon()

            for spoke in self.spokes:
                # print('check segs')

                if spoke.growing:

                    for p in range(len(polygon)):    # A polyseg is a list of (x,y) tuples, one per points
                        polyseg = polygon[p]
                        next_polyseg = polygon[(p+1) % len(polygon) ]  # Wrap
                        x = polyseg[0]
                        y = polyseg[1]
                        next_x = next_polyseg[0]
                        next_y = next_polyseg[1]

                        #print(x, y, next_x, next_y)

                        if intersect(spoke, polyseg, next_polyseg):
                            print('INTERSECT detected stopping spoke')
                            spoke.stop()

                        if intersect_frame(spoke, frame_segs):
                            print('INTERSECT with frame detected stopping spoke')
                            spoke.stop()



class Spoke():

    def __init__(self, angle, bubble_x, bubble_y):
        """ x, y are root of spoke - same as bubble location it grows from """
        self.x = bubble_x
        self.y = bubble_y
        self.angle = angle
        self.bubble_x = bubble_x
        self.bubble_y = bubble_y
        self.growing = True


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


#     def line():
#         return Line(self.x, self.y, bubble_x, bubble_y)
#
# class Line():
#
#     def __init__(self, pt1_x, pt1_y, p2_x, pt2_y):
#         self.pt1_x = pt
#         self.pt1_y = pt1_y
#         self.p2_x = pt2_x
#         self.pt2_y = pt2_y




def intersect_frame(spoke, frames):

    # Convert frame into polysegs, call intersect

    for f in range(len(frames)):

        this_frame = frames[f]
        next_frame = frames[(f+1) % len(frames)]

        # print(this_frame)
        # print(next_frame)

        if intersect(spoke, this_frame, next_frame):
            return True

    return False


def on_both_sides(spoke_base, angle, poly_seg_1, poly_seg_2):
    pass


def intersect(spoke, poly_seg_1, poly_seg_2):
    #
    # return False
    # r =  random.choice( [False]*20 + [True])
    # print('spoke stop', r)
    # return(r)


    ''' Spoke has spoke.x and spoke.y, the coords of one end, the tip
    spoke.bubble_x , spoke.bubble_y coords of the end
    spoke.angle, angle in rads

    poly_seg_1 and poly_seg_2 are tuples (x, y) of each point in the polygon segment.

    '''

    # Check if spoke is on one side of poly_seg
    # If spoke == poly_seg_1 == poly_seg_2

    #print('\n\n')


    if spoke.x == poly_seg_1[0] and spoke.y == poly_seg_1[1]:
        # print('intersct spoke tip x and polyseg1')
        return True

    if spoke.x == poly_seg_2[0] and spoke.y == poly_seg_2[1]:
        # print('intersct spoke tip and polyseg2')
        return True


    if spoke.bubble_x == poly_seg_1[0] and spoke.bubble_y == poly_seg_1[1]:
        # print('intersct spoke base x and polyseg1')
        return True

    if spoke.bubble_x == poly_seg_2[0] and spoke.bubble_y== poly_seg_2[1]:
        # print('intersct spoke base  and polyseg2')
        return True


    # What is polyseg angle?

    #print('calcs testing spoke bisects infinite polyseg')


    

    dx = poly_seg_1[0] - poly_seg_2[0]
    dy = poly_seg_1[1] - poly_seg_2[1]

    if dx == 0 and dy < 0:
        poly_angle = -math.pi / 2
    elif dx == 0 and dy >= 0:
        poly_angle = math.pi / 2
    else:
        poly_angle = math.atan( dy / dx )


    spoke_base = (spoke.bubble_x, spoke.bubble_y)
    spoke_tip = (spoke.x, spoke.y)

    polyseg_both_sides_of_spoke = on_both_sides(spoke_base, spoke.angle, poly_seg_1, poly_seg_2)
    
    spoke_both_sides_of_polyseg = on_both_sides(poly_seg_1, poly_angle, spoke_base, spoke_tip)


    if polyseg_both_sides_of_spoke and spoke_both_sides_of_polyseg:
        return True
    
    return False 


    # Shift to put poly_seg_1 at (0,0)

    dx = 0 - poly_seg_1[0]
    dy = 0 - poly_seg_1[1]

    s_tip_x = spoke.x + dx
    s_tip_y = spoke.y + dy

    s_base_x = spoke.bubble_x + dx
    s_base_y = spoke.bubble_y + dy

    # And shift other polyseg and spoke same way

    ps1x = poly_seg_1[0] + dx    # 0
    ps1y = poly_seg_1[1] + dy    # 0

    ps2x = poly_seg_2[0] + dx   # needed?
    ps2y = poly_seg_2[1] + dy


    if s_tip_y == 0:
        if s_tip_x < 0:
            spoke_tip_angle = - math.pi / 2
        else:
            spoke_tip_angle = - math.pi / 2
    else:
        spoke_tip_angle = math.atan(s_tip_x / s_tip_y)


    if s_base_y == 0:
        if s_base_x < 0:
            spoke_base_angle = - math.pi / 2
        else:
            spoke_base_angle = math.pi / 2
    else:
        spoke_base_angle = math.atan(s_base_x / s_base_y)


    # Subtract poly_seg_1 angle from both

    spoke_tip_angle = (spoke_tip_angle - poly_angle) % (2 * math.pi)
    spoke_base_angle = (spoke_base_angle - poly_angle) % (2 * math.pi)

    # If intersect, then spoke_base_angle will be between 0 and PI
    # and spoke_tip_angle will be between PI and 2PI. Or vice-versa
    # Both 0 or both PI ok too

    a1 = min(spoke_base_angle, spoke_tip_angle)
    a2 = max(spoke_base_angle, spoke_tip_angle)


    # print('diff spokes', a1 - a2)


    if a1 < 0 or a1 > math.pi:
        # Nope, outside range 0 - PI
        # print('false smaller angle not on range 0-pi', a1, a2)
        return False


    if a2 < math.pi or a2 > math.pi * 2:
        # Nope, outside range PI-2*PI
        # print('false larger angle not in range pi-2pi', a1, a2)
        return False



    # check if poly_seg points are on both sides of the spoke

    # print('calcs testing polysec bisects infinite spoke')

    # Shift all coords to put spoke tip at (0,0)

    dx = 0 - spoke.x
    dy = 0 - spoke.y

    sx = spoke.x + dx
    sy = spoke.y + dy

    # And shift polysegs same way

    ps1x = poly_seg_1[0] + dx
    ps1y = poly_seg_1[1] + dy

    ps2x = poly_seg_2[0] + dx
    ps2y = poly_seg_2[1] + dy


    if ps1y == 0:
        if ps1x < 0:
            ps1angle = -math.pi / 2
        else :
            ps1angle = math.pi / 2
    else:
        ps1angle = math.atan(ps1x / ps1y)

    if ps2y == 0:
        if ps2x < 0:
            ps2angle = - math.pi / 2
        else :
            ps2angle = math.pi / 2

    else:
        ps2angle = math.atan(ps2x / ps2y)

    # Subtract spoke angle from both

    dps1angle = (ps1angle - spoke.angle) % (2 * math.pi)
    dps2angle = (ps2angle - spoke.angle) % (2 * math.pi)

    # If intersect, then dps1angle will be between 0 and PI and dps2angle will be between PI and 2PI. Or vice-versa
    # Both 0 or both PI ok too

    a1 = min(dps1angle, dps2angle)
    a2 = max(dps1angle, dps2angle)

    # print('diff polyseg', a1 - a2)

    if a1 < 0 or a1 > math.pi:
        # Nope, outside range 0 - PI
        # print('false smaller angle not in range 0-pi ', a1, a2)
        return False


    if a2 < math.pi or a2 > math.pi * 2:
        # Nope, outside range PI-2*PI
        # print('false larger angle not in range pi-2pi', a1, a2)

        return False

    # TODO check for parallel lines, angles will be same



    return True
