def anaglifo(img):
    print("Anaglifo", img.firstImage.name, img.secondImage.name)

def sideBySide(img):
    print("Side by side", img.firstImage.name, img.secondImage.name)

def topDown(img):
    print("Top-down", img.firstImage.name, img.secondImage.name)

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
        self.firstImage = img1
        self.secondImage = img2