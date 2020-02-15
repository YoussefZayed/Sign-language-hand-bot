import cv2 as cv


def show_cam():
    #starts the video stream and initializes window
    cam = cv.VideoCapture(0)
    cv.namedWindow("Video Stream", cv.WINDOW_NORMAL)
    cv.resizeWindow("Video Stream", 640, 480)
    while True:
        ret, img = cam.read()
        img = cv.flip(img, 1)

        if img is not None:
            img, roi = detection(img)
            cv.imshow("Video Stream", img)
            cv.imshow("ROI", roi)

        key = cv.waitKey(100) # wait 100 ms between frames & accept key input

        if key == 27:  # Press esc to exit
            print("Program exited")
            break
    cam.release()


def detection(img):
    h, w, c = img.shape
    #80 x 80 square around centre of video stream
    w_roi, h_roi = (w//2 - 80, w//2 + 80), (h//2 - 80, h//2 + 80)
    roi = img[h_roi[0]: h_roi[1], w_roi[0]: w_roi[1]]
    img = cv.rectangle(img, (w_roi[0],  h_roi[0]), (w_roi[1], h_roi[1]), (255, 255, 255))
    return img, roi


show_cam()
