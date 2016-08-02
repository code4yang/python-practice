"""
将图片转成iphone5s的分辨率，使用到了pillow库
"""
from PIL import Image


def convert2ip5s(filename, out="out.jpg"):
    """
    将指定文件转成小于iPhone5s的分辨率
    :param out: 输出路径,默认为当前路径下的out.jpg
    :param filename: 文件名
    :return:
    """
    # iphone5s分辨率 1136*640
    img = Image.open(filename, 'r')
    width = img.width
    height = img.height
    if width > 1136:
        img = img.resize((1136, int(height * (1136 / width))))
        height = img.height
        width = img.width
    if height > 640:
        img.resize((int(width * (640 / height)), 640))
    img.save(out)


convert2ip5s('pic.jpg')
