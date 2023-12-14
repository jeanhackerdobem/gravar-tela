#pip install opencv-python & numpy & pyautogui

import  cv2
import numpy as np
import pyautogui

SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("suagravacao.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    img = pyautogui.screenshit()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitkey(1) == ord("q"):
        break


cv2.destroyAllWindows()
out.release()
