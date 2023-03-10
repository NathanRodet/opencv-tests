# __init__.py

import cv2
import numpy
import mss
import time
from win32 import win32gui
from win32gui import GetWindowRect, FindWindow


def get_screen_capture():
    print("----------------- Getting Captures  ---------------------")
    global img

    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = numpy.array(sct.grab(window_rect))

    # Display the picture
    cv2.imshow("OpenCV/Numpy normal", img)
    # print(f"fps: {1 / (time.time() - last_time)}")


def get_window_size():
    print("----------------- Getting Window Size -------------------")
    global window_rect

    window_handle = FindWindow(
        None, "gank.jpg ‎- Photos")
    window_rect = GetWindowRect(window_handle)


def compare_capture_to_template():
    print("----------------- Comparing image to template -----------")

    result = cv2.matchTemplate(img, template_en, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(, max_val, min_loc, max_loc)
    print(max_val)

    # Check if the template is found
    if treshold < max_val:
        print("Found")
        cv2.rectangle(img, max_loc, (max_loc[0] + 100, max_loc[1] + 100),
                      (0, 0, 255), 2)


def main():
    print("---------------------------------------------------------")
    print("------------------ Program Started ----------------------")
    print("---------------------------------------------------------")
    global sct
    try:
        print("----------------- Starting to Record --------------------")
        with mss.mss() as sct:
            while "Screen capturing":
                get_window_size()
                get_screen_capture()
                compare_capture_to_template()
                # Press "q" to quit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break
    except ValueError:
        print(ValueError)


template = cv2.imread("./lifebar.png", cv2.IMREAD_UNCHANGED)
template_en = cv2.imread("./lifebar_en.png", cv2.IMREAD_UNCHANGED)
treshold = 0.35

main()
