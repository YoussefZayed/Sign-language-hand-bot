import serial, time
import cv2
import numpy as np


def video_cap(arduino):
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', 2000, 2000)

        h, w, _ = frame.shape
        h, w = int(h/2), int(w/2)
        x, y = w - int(w/2), h - int(h/2)

        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        elif cv2.waitKey(1) & 0xFF == ord('s'):
            # send over some data to arduino
            send_data(arduino, 'test')

    cap.release()
    cv2.destroyAllWindows()


def init_arduino_comm():
    return serial.Serial('/dev/ttyACM0', 115200, timeout=.1)


def send_data(arduino, data):
    arduino.write(str.encode(data))


if __name__ == '__main__':

    arduino = init_arduino_comm()
    video_cap(arduino)
