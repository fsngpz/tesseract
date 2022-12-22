import os
import cv2
import pytesseract
from PIL import Image
import time
import pickle
from OCR_KNN import predict

# imgLoc = r'C:\Users\User\PycharmProjects\tesseract\notAngka.png'
# pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
def getNotAngka(pathImg):
    imgLoc = pathImg
    img = cv2.imread(imgLoc)
    baseImg = Image.open(imgLoc)
    notAngka = []
    heightImg, weightImg, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    sortNum = 0
    for b in boxes.splitlines():
        b = b.split(' ')
        value = b[0]
        # if value.isnumeric():
        if value.isnumeric():
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
            # print(value, left, down, up, right)
            # imgCrop.save(f"/Users/fsangap/Documents/Dataset/1/{value}[{sortNum}].png")

            path = fr"C:\Users\User\Documents\Dataset\{value}[{sortNum}].png"
            imgCrop.save(path)
            imgCropped = cv2.resize(cv2.imread(path, 0), (28, 28))
            result = predict(path)
            if result != "0" and result != "DOT":
                notAngka.append(result)
            cv2.putText(img, result, (left,right+25), cv2.FONT_HERSHEY_COMPLEX,0.7,(50,50,255), 1)
            sortNum += 1

    return notAngka

# cv2.imshow('Result', img)
# cv2.waitKey(0)

if __name__ == "__main__":
    getNotAngka(r'C:\Users\User\PycharmProjects\tesseract\notAngka.png')