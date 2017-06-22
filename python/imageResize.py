# -*- coding: UTF-8 -*-
from __future__ import print_function
import os, sys
from PIL import Image
import requests
from io import BytesIO

pages = range(0,105)
imageCount = 0
totalCount = 0
#ALWAYS GET NEW TOKEN
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyIkX18iOnsic3RyaWN0TW9kZSI6dHJ1ZSwic2VsZWN0ZWQiOnsiX2lkIjoxLCJuYW1lIjoxLCJ1c2VybmFtZSI6MSwiYWRtaW4iOjEsInBhc3N3b3JkIjoxfSwiZ2V0dGVycyI6e30sIndhc1BvcHVsYXRlZCI6ZmFsc2UsImFjdGl2ZVBhdGhzIjp7InBhdGhzIjp7ImFkbWluIjoiaW5pdCIsInBhc3N3b3JkIjoiaW5pdCIsInVzZXJuYW1lIjoiaW5pdCIsIm5hbWUiOiJpbml0IiwiX2lkIjoiaW5pdCJ9LCJzdGF0ZXMiOnsiaWdub3JlIjp7fSwiZGVmYXVsdCI6e30sImluaXQiOnsiYWRtaW4iOnRydWUsInBhc3N3b3JkIjp0cnVlLCJ1c2VybmFtZSI6dHJ1ZSwibmFtZSI6dHJ1ZSwiX2lkIjp0cnVlfSwibW9kaWZ5Ijp7fSwicmVxdWlyZSI6e319LCJzdGF0ZU5hbWVzIjpbInJlcXVpcmUiLCJtb2RpZnkiLCJpbml0IiwiZGVmYXVsdCIsImlnbm9yZSJdfSwiZW1pdHRlciI6eyJkb21haW4iOm51bGwsIl9ldmVudHMiOnt9LCJfZXZlbnRzQ291bnQiOjAsIl9tYXhMaXN0ZW5lcnMiOjB9fSwiaXNOZXciOmZhbHNlLCJfZG9jIjp7ImFkbWluIjp0cnVlLCJwYXNzd29yZCI6ImZpdXNjaXNkYW0yMDE3IyIsInVzZXJuYW1lIjoiZml1c2Npc2RhbXVzZXIiLCJuYW1lIjoiU3VwZXIgVXNlciIsIl9pZCI6IjU4ZGMzMzYyMWM4NzM0NmYzN2U5OTY3MCJ9LCJpYXQiOjE0OTgxNDc3MjcsImV4cCI6MTQ5ODIzNDEyN30.ziEZtS-ZeQNlLfSPWWKlCuv1T1qGnxOBkUj_23dTCJY'
for page in pages:
    
    response = requests.get('http://assets.cs.fiu.edu:3000/api/v1/digitalassets?skip='+ str(page*100) +'&token=' + token)
    images = response.json()
    for image in images['response']:
        totalCount += 1
        try:
            
            if "tif" in image['relativePath'] or "TIF" in image['relativePath']:
                imageCount += 1
                print(image['relativePath'], imageCount)
                r = requests.get(image['url'])
                img = Image.open(BytesIO(r.content))

                print (img.format, img.size, img.mode)
                if "tif" in image['relativePath']:
                    outfile = image['relativePath'].replace('.tif', '.jpg')
                
                if "TIF" in image['relativePath']:
                    outfile = image['relativePath'].replace('.TIF', '.jpg')

                print(outfile)

                try:
                    img.save(outfile)
                except IOError:
                    print("cannot convert image")

                size = (img.size[0] * .2, img.size[1]* .2)

                print(size)

                img.thumbnail(size)

                if "tif" in image['relativePath']:
                    thumbOutfile = image['relativePath'].replace('.tif', '.jpg')
                    finalThumbOutfile = thumbOutfile.replace('/disk/assets', '/disk/assets/thumbnails')
                
                if "TIF" in image['relativePath']:
                    thumbOutfile = image['relativePath'].replace('.TIF', '.jpg')
                    finalThumbOutfile = thumbOutfile.replace('/disk/assets', '/disk/assets/thumbnails')
                
                print(finalThumbOutfile)
                
                try:
                    img.save(finalThumbOutfile)
                except IOError:
                    print("cannot create thumbnail")
                
                print('*************END OF IMAGE PROCESSING************')
        
        except IOError:
                print("cannot create thumbnail for", image['relativePath'])

print(imageCount)
print(totalCount)