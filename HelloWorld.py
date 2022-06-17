import cv2 as cv
import sys

im_path = 'D:\git\imageprocessing\opencv\Example_Images\Volt.jpg'
img = cv.imread(im_path)

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("volt_processed.png", img)
