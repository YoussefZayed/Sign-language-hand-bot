import time
import random
import cv2
from verify import predict


LETTERS = ['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'nothing', 'O', 'P', 'Q',
           'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SAVE_FILE = 'verifier/saved_image.jpg'
sequence = []


def generate_sequence(size):
    random.seed()
    for i in range(size):
        sequence.append(LETTERS[random.randint(0, 28)])


def video_cap():
    sequence = ['A', 'B', 'C', 'D', 'E']

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Video Stream', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Stream', 2000, 1500)

    i = 0
    correct = False
    ts = time.time()
    guessed = ''
    show_congrats = False

    while i < len(sequence):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # get roi dimensions
        roi_scale = 2
        h, w, _ = frame.shape
        roi_size = int(h/roi_scale)
        x, y = int(w/2) - int(roi_size/2), int(h/2) - int(roi_size/2)

        key = cv2.waitKey(100)

        # exit
        if key & 0xFF == 27:
            break

        if correct and time.time() - ts > 3:
            correct = False
            i += 1
            if i == len(sequence):
                show_congrats = True

        if correct:
            img = cv2.rectangle(frame, (x, y), (x + roi_size, y + roi_size), (0, 255, 0), 1)
            cv2.putText(img, 'Target: ' + guessed, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(img, 'Actual: ' + guessed, (x + 150, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

        else:
            img = cv2.rectangle(frame, (x, y), (x + roi_size, y + roi_size), (0, 0, 255), 1)
            cv2.putText(img, 'Target: ' + sequence[i], (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            cv2.putText(img, 'Actual: ' + guessed, (x + 150, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

            if time.time() - ts > 2:
                roi = frame[y:y + roi_size, x:x + roi_size]
                cv2.imwrite(SAVE_FILE, roi)

                guessed = predict()

                ts = time.time()

                if guessed == sequence[i]:
                    correct = True
                    ts = time.time()

        cv2.imshow('Video Stream', img)

    # display congratulations
    if show_congrats:

        ts = time.time()
        while time.time() - ts < 5:
            ret, frame = cap.read()
            img = cv2.flip(frame, 1)

            h, w, _ = frame.shape

            cv2.putText(img, 'Congratulations!', (int(w/2) - int(w/4), int(h/2)), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Video Stream', img)

            key = cv2.waitKey(100)

            if key & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_cap()
