from geometry import Bubble
from copy import copy
import time
from threading import Thread

iters = 0

last_run  = 0

def start_bubbles(bubbles, frame, update_callback, done_callback):


    global last_run
    last_run = time.time()

    # for bubble in bubbles:
    #     bubble.init_spokes()

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

    # for bubble_num in range(len(bubbles)):
    #     # Do any spokes intersect a poly_seg? Stop if so.
    #     bubbles.pop(bubble_num)
    #     bubble.check_spokes(bubbles, frame)
    #     bubbles.insert(bubble_num, bubble)

    for bubble in bubbles:
        other_bubbles = copy(bubbles)
        other_bubbles.remove(bubble)
        bubble.check_spokes(other_bubbles, frame)


    callback(bubbles)

    #time.sleep(0.1)

    if grow_more(bubbles):
        iters += 1
        grow_again = Thread(target=grow_one, args=[bubbles, frame, callback, done_callback])
        grow_again.start()

    else:
        done_callback(bubbles, iters)


    #print('this thread ended')



def grow_more(bubbles):
    # global count
    # count+=1
    # if count > 50:
    #     return False
    # else:
    #     return True

    # all bubbles done?
    for bubble in bubbles:
        if bubble.spokes_growing():
            #print('grow more')
            return True

    #print('all done growing')
    return False
