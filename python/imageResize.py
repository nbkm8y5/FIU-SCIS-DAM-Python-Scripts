# -*- coding: UTF-8 -*-
from __future__ import print_function
import os, sys
from PIL import Image
import requests
from io import BytesIO

# print(temp['attr'])

pages = range(0,105)
print(list(pages))
imageCount = 0
for page in pages:

    response = requests.get('http://assets.cs.fiu.edu:3000/api/v1/digitalassets?skip='+ str(page*100) +'&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyIkX18iOnsic3RyaWN0TW9kZSI6dHJ1ZSwic2VsZWN0ZWQiOnsiX2lkIjoxLCJuYW1lIjoxLCJ1c2VybmFtZSI6MSwiYWRtaW4iOjEsInBhc3N3b3JkIjoxfSwiZ2V0dGVycyI6e30sIndhc1BvcHVsYXRlZCI6ZmFsc2UsImFjdGl2ZVBhdGhzIjp7InBhdGhzIjp7ImFkbWluIjoiaW5pdCIsInBhc3N3b3JkIjoiaW5pdCIsInVzZXJuYW1lIjoiaW5pdCIsIm5hbWUiOiJpbml0IiwiX2lkIjoiaW5pdCJ9LCJzdGF0ZXMiOnsiaWdub3JlIjp7fSwiZGVmYXVsdCI6e30sImluaXQiOnsiYWRtaW4iOnRydWUsInBhc3N3b3JkIjp0cnVlLCJ1c2VybmFtZSI6dHJ1ZSwibmFtZSI6dHJ1ZSwiX2lkIjp0cnVlfSwibW9kaWZ5Ijp7fSwicmVxdWlyZSI6e319LCJzdGF0ZU5hbWVzIjpbInJlcXVpcmUiLCJtb2RpZnkiLCJpbml0IiwiZGVmYXVsdCIsImlnbm9yZSJdfSwiZW1pdHRlciI6eyJkb21haW4iOm51bGwsIl9ldmVudHMiOnt9LCJfZXZlbnRzQ291bnQiOjAsIl9tYXhMaXN0ZW5lcnMiOjB9fSwiaXNOZXciOmZhbHNlLCJfZG9jIjp7ImFkbWluIjp0cnVlLCJwYXNzd29yZCI6ImZpdXNjaXNkYW0yMDE3IyIsInVzZXJuYW1lIjoiZml1c2Npc2RhbXVzZXIiLCJuYW1lIjoiU3VwZXIgVXNlciIsIl9pZCI6IjU4ZGMzMzYyMWM4NzM0NmYzN2U5OTY3MCJ9LCJpYXQiOjE0OTYyNDYwNzAsImV4cCI6MTQ5NjMzMjQ3MH0.dtYgyrbqCX8DKwHJS790h5oywBs8hgeU-IBED2Z2YbM')
    images = response.json()
    for image in images['response']:
        try:
            
            if "tif" in image['relativePath'] or "TIF" in image['relativePath']:
                imageCount += 1
                print(image['relativePath'], imageCount)
                img = Image.open(image['relativePath'])
                print(img)
                print (img.format, img.size, img.mode)
        except IOError:
                print("cannot create thumbnail for", image['relativePath'])


    # try:
    #     im = Image.open(i)
    #     outfile = i.replace('/disk/assets', '/disk/assets/thumbnails')

    #     size = (im.size[0] * .1, im.size[1]* .1)

        # print(size)

        # print(outfile)

        # im.thumbnail(size)
        # im.save(outfile, "JPEG")
    # except IOError:
    #         print("cannot create thumbnail for", i)