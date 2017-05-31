# -*- coding: UTF-8 -*-
from __future__ import print_function
import os, sys
from PIL import Image
import requests
from io import BytesIO



# for i in data:
    # print(i)

    # try:
    #     im = Image.open(i)
    #     outfile = i.replace('/disk/assets', '/disk/assets/thumbnails')

    #     size = (im.size[0] * .1, im.size[1]* .1)

        # print(size)
    
        # print (im.format, im.size, im.mode)
        # print(outfile)

        # im.thumbnail(size)
        # im.save(outfile, "JPEG")
    # except IOError:
    #         print("cannot create thumbnail for", i)