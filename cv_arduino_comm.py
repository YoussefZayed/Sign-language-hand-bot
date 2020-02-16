import serial
import cv2
from verify import predict

SAVE_FILE = 'verifier/saved_image.jpg'
ARDUINO_PORT = '/dev/ttyACM0'


def video_cap(arduino):
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Stream', 2000, 1500)

    letter = ' '

    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        roi_scale = 2
        h, w, _ = frame.shape
        roi_size = int(h/roi_scale)
        x, y = int(w/2) - int(roi_size/2), int(h/2) - int(roi_size/2)

        img = cv2.rectangle(frame, (x, y), (x + roi_size, y + roi_size), (0, 255, 0), 1)
        cv2.putText(img, letter, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Video Stream', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        if cv2.waitKey(1) & 0xFF == ord('s'):
            roi = frame[y:y + roi_size, x:x + roi_size]
            cv2.imwrite(SAVE_FILE, roi)

            letter = predict()

            if letter == 'nothing':
                send_data(arduino, '[')
            elif letter == 'space':
                send_data(arduino, '\\')
            else:
                send_data(arduino, letter)

    cap.release()
    cv2.destroyAllWindows()


def init_arduino_comm():
    return serial.Serial(ARDUINO_PORT, 115200, timeout=.1)


def send_data(arduino, data):
    arduino.write(str.encode(data))


if __name__ == '__main__':

    arduino = init_arduino_comm()
    video_cap(arduino)
