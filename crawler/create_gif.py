#!/usr/bin/python3
import sys
from PIL import Image
images = []
for each in sys.argv[1:]:
	images.append(Image.open(each))
im = images[1]
im.save('gif.gif',save_all=True,append_images=images,loop=1,duration=1,comment=b"aaabbb")
