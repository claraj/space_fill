from geometry import Bubble


def start_bubbles(bubble, callback):

    for bubble in bubbles:
        point.init_spokes()

    while growmore(bubbles):
        for point in points:
            # grow each spoke

            # check if it insersects with any part of any other point's polygon. Stop it if so
            pass

        time.sleep(0.1)




def growmore(bubbles):
    # all bubbles done?
    for bubble in bubbles:
        if bubble.spokes_growing():
            return True

    return False
