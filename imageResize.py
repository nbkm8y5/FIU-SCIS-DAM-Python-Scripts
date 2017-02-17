# -*- coding: UTF-8 -*-
import os
from PIL import Image

# GET RELATIVE URLS FROM FILE AND MAKE URLS
# with open('dataAdded.txt') as f:
with open('cd3.jpg') as f:
    relativePaths = f.read().splitlines()

print "\nrelativePaths List"
print "=================="
print(relativePaths[0:10])

print "\nrelativePaths type"
print "=================="
print type(relativePaths) #list

print "\nrelativePaths length"
print "===================="
print len(relativePaths)

size = (320, 240)


# //loop here
outfile= 'thumb_'+'cd3.jpg'
im = Image.open('cd3.jpg')

im.thumbnail(size)
im.save(outfile, "JPEG")


print im.format, im.size, im.mode
# tempRelativePath = relativePaths[index]
# tempFileName, tempFileExtension = os.path.splitext('/disk/' + tempRelativePath)



    # fiuUrl = "http://localhost:3000/api/v1/digitalassets"

    # modelPayload = {
    #         'fileName': tempFileName,
    #         'title': 'CHANGE',
    #         'caption': 'CHANGE',
    #         'altText': 'CHANGE',
    #         'description': 'CHANGE',
    #         'fileType': tempFileExtension,
    #         'uploadedBy': 'rmore071',
    #         'fileSize': b,
    #         'url': x,
    #         'relativePath': tempRelativePath,
    #         'tags': tempConceptsList
    #         # 'exif': tempExifDict
    #         }

    # fiuResponse = requests.request("POST", fiuUrl, json=modelPayload)
    # print index