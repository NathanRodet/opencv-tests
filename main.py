# __init__.py

import cv2
import numpy
import mss
import time
from win32 import win32gui
from win32gui import GetWindowRect, FindWindow


# def record_screen():
#     with mss.mss() as sct:

# with mss.mss() as sct:
#     # Part of the screen to capture
#     monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

#     while "Screen capturing":
#         last_time = time.time()

#         # Get raw pixels from the screen, save it to a Numpy array
#         img = numpy.array(sct.grab(monitor))

#         # Display the picture
#         cv2.imshow("OpenCV/Numpy normal", img)

#         # Display the picture in grayscale
#         # cv2.imshow('OpenCV/Numpy grayscale',
#         #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

#         print(f"fps: {1 / (time.time() - last_time)}")

#         # Press "q" to quit
#         if cv2.waitKey(25) & 0xFF == ord("q"):
#             cv2.destroyAllWindows()
#             break

def start_screen_recording():
    print("------------------ Starting to Record --------------------")
    with mss.mss() as sct:
        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(window_rect))

            # Display the picture
            cv2.imshow("OpenCV/Numpy normal", img)
            print(f"fps: {1 / (time.time() - last_time)}")

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


def get_window_size():
    print("------------------ Getting Window Size -------------------")
    global window_rect

    window_handle = FindWindow(None, "Invite de commandes")
    window_rect = GetWindowRect(window_handle)


def main():
    print("----------------------------------------------------------")
    print("-------------------- Program Started ---------------------")
    print("----------------------------------------------------------")
    try:
        get_window_size()
        start_screen_recording()
    except ValueError:
        print(ValueError)


main()
