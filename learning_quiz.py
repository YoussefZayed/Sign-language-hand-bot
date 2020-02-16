import serial, time
import cv2
from verify import predict

SAVE_FILE = 'verifier/saved_image.jpg'
SEQUENCE = ['C', 'B', 'C', 'D', 'E']


def video_cap():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Stream', 2000, 1500)

    i = 0
    correct = False
    ts = time.time()
    guessed = ''

    while i < len(SEQUENCE):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        roi_scale = 2
        h, w, _ = frame.shape
        roi_size = int(h/roi_scale)
        x, y = int(w/2) - int(roi_size/2), int(h/2) - int(roi_size/2)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        if correct and time.time() - ts > 3:
            correct = False

        if correct:
            img = cv2.rectangle(frame, (x, y), (x + roi_size, y + roi_size), (0, 255, 0), 1)
            cv2.putText(img, 'Target: ' + guessed, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(img, 'Actual: ' + guessed, (x + 150, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

        else:
            img = cv2.rectangle(frame, (x, y), (x + roi_size, y + roi_size), (0, 0, 255), 1)
            cv2.putText(img, 'Target: ' + SEQUENCE[i], (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(img, 'Actual: ' + guessed, (x + 150, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                roi = frame[y:y + roi_size, x:x + roi_size]
                cv2.imwrite(SAVE_FILE, roi)

                guessed = predict()

                if guessed == SEQUENCE[i]:
                    correct = True
                    ts = time.time()
                    i += 1

        cv2.imshow('Video Stream', img)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    video_cap()
