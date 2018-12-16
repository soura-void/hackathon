#utils to be used
import cv2
def clickpic():

    camera = cv2.VideoCapture(2)
    return_value, image = camera.read()
    cv2.imwrite('download.jpg', image)
    del(camera)

clickpic()
