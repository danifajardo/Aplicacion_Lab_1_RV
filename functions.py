import cv2

width = 683
height = 384
size = (width, height)
size2 = (width, height*2)

def anaglifo(img):
    print("Anaglifo", img.firstImagePath, img.secondImagePath)

def sideBySide(img):
    resized1 = cv2.resize(img.firstImage, size2, interpolation = cv2.INTER_AREA)
    resized2 = cv2.resize(img.secondImage, size2, interpolation = cv2.INTER_AREA)
    horizontal = cv2.hconcat([resized1, resized2])
    cv2.imshow('Side by side', horizontal)
    cv2.waitKey(0)

def topDown(img):
    resized1 = cv2.resize(img.firstImage, size, interpolation = cv2.INTER_AREA)
    resized2 = cv2.resize(img.secondImage, size, interpolation = cv2.INTER_AREA)
    vertical = cv2.vconcat([resized1, resized2])
    cv2.imshow('Top-down', vertical)
    cv2.waitKey(0)

def selecFun(arg, img1, img2):
    objImagen = Img(img1 = img1,img2 = img2)
    if arg == 1:
        anaglifo(objImagen)
    elif arg == 2:
        sideBySide(objImagen)
    else:
        topDown(objImagen)


class Img():
    def __init__(self, img1, img2):
        self.firstImagePath = img1.name
        self.secondImagePath = img2.name
        self.firstImage = None
        self.secondImage = None
        self.convertedImages()

    def convertedImages(self):
        self.firstImage = cv2.imread(self.firstImagePath)
        self.secondImage = cv2.imread(self.secondImagePath)
