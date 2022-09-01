from PIL import Image


def rotate(path, method):
    imageOpen = Image.open(path)
    imageRotate = imageOpen.rotate(45, method, expand=1)
    imageRotate.show()


def resizing(path, method):
    imageOPen = Image.open(path)
    imageResizing = imageOPen.resize((128, 128), method)
    imageResizing.show()


rotate('images/united.jpg', Image.BILINEAR)
resizing('images/united.jpg', Image.BILINEAR)
