__author__ = 'Robert'
from images2gif import writeGif
from PIL import Image
import os

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.gif')))
#['animationframa.png', 'animationframb.png', ...] "

images = [Image.open(fn) for fn in file_names]

size = (1280,720)
for im in images:
    im.thumbnail(size, Image.ANTIALIAS)

print writeGif.__doc__

filename = "my_gif.GIF"
writeGif(filename, images, duration=0.2)