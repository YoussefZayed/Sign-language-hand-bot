import serial
import cv2

SAVE_FILE = 'saved_image.jpg'
ARDUINO_PORT = '/dev/ttyACM0'


def video_cap(arduino):
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', 2000, 2000)

        h, w, _ = frame.shapes
        h, w = int(h/2), int(w/2)
        x, y = w - int(w/2), h - int(h/2)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        elif cv2.waitKey(1) & 0xFF == ord('s'):
            roi = frame[y:y+h, x:x+w]
            cv2.imwrite(SAVE_FILE, roi)

            # get letter based on image
            # send_data(arduino, letter)

        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.imshow('frame', img)

    cap.release()
    cv2.destroyAllWindows()

u
def init_arduino_comm():
    return serial.Serial(ARDUINO_PORT, 115200, timeout=.1)


def send_data(arduino, data):
    arduino.write(str.encode(data))


if __name__ == '__main__':

    arduino = init_arduino_comm()
    video_cap(arduino)
