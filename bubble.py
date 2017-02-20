from copy import copy
import time
from threading import Thread

iters = 0

last_run = 0


def start_bubbles(bubbles, frame, update_callback, done_callback):

    global last_run
    last_run = time.time()

    if grow_more(bubbles):

        grow = Thread(target=grow_one, args=[bubbles, frame, update_callback, done_callback])
        grow.start()


def grow_one(bubbles, frame, callback, done_callback):
    global last_run

    time_now = time.time()
    print('Last run took %f', (time_now-last_run))

    last_run = time_now

    global iters

    for bubble in bubbles:
        # grow each spoke
        bubble.grow_all_spokes()

    for bubble in bubbles:
        other_bubbles = copy(bubbles)
        other_bubbles.remove(bubble)
        bubble.check_spokes(other_bubbles, frame)


    callback(bubbles)

    if grow_more(bubbles):
        iters += 1
        grow_again = Thread(target=grow_one, args=[bubbles, frame, callback, done_callback])
        grow_again.start()

    else:
        done_callback(bubbles, iters)



def grow_more(bubbles):

    # all bubbles done?
    for bubble in bubbles:
        if bubble.spokes_growing():
            return True

    return False
