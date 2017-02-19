from geometry import Bubble
from copy import copy
import time
from threading import Thread

iters = 0

def start_bubbles(bubbles, update_callback, done_callback):

    for bubble in bubbles:
        bubble.init_spokes()

    if growmore(bubbles):

        grow = Thread(target=grow_one, args=[bubbles, update_callback, done_callback])
        grow.start()


def grow_one(bubbles, callback, done_callback):

    global iters

    for bubble in bubbles:
        # grow each spoke
        bubble.grow_all_spokes()

        # Do any spokes intersect a poly_seg? Stop if so.
        other_bubbles = copy(bubbles)
        other_bubbles.remove(bubble)
        bubble.check_spokes(bubbles)

    callback(bubbles)
    time.sleep(0.1)

    if growmore(bubbles):

        iters += 1

        grow_again = Thread(target=grow_one, args=[bubbles, callback, done_callback])
        grow_again.start()

    else:
        done_callback(bubbles, iters)


def growmore(bubbles):
    # global count
    # count+=1
    # if count > 50:
    #     return False
    # else:
    #     return True

    # all bubbles done?
    for bubble in bubbles:
        if bubble.spokes_growing():
            return True

    return False
