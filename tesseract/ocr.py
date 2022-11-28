import os
import cv2
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'
img = cv2.imread(r'/Users/fsangap/PycharmProjects/tesseract/oktaf4.png')
def getNotAngka():

    baseImg = Image.open(r'/Users/fsangap/PycharmProjects/tesseract/oktaf4.png')
    notAngka = []
    heightImg, weightImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    sortNum = 0
    for b in boxes.splitlines():
        b = b.split(' ')
        value = b[0]
        # if value.isnumeric():
        if value.isnumeric() or value == '.':
            notAngka.append(value)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            left = x - 5
            right = (heightImg - y) + 5
            up = w + 5
            down = (heightImg - h) - 5
            cv2.rectangle(img, (left, right), (up, down), (0, 0, 255), 1)
            # crop = img[y:y + h, x:x + w]
            # cv2.imshow("cropped", crop)
            imgCrop = baseImg.crop((left, down, up, right))
            value = "dot" if value == "." else value
            print(value, left, down, up, right)
            imgCrop.save(f"/Users/fsangap/Documents/Dataset/1/{value}[{sortNum}].png")
            sortNum += 1

    return notAngka
getNotAngka()

# print(notAngka())

cv2.imshow('Result', img)
cv2.waitKey(0)