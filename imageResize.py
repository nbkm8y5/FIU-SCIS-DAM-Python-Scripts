# -*- coding: UTF-8 -*-
import os
from PIL import Image

# GET RELATIVE URLS FROM FILE AND MAKE URLS
with open('dataAdded.txt') as f:
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

im = Image.open('cd3.jpg')

print im.format, im.size, im.mode
# tempRelativePath = relativePaths[index]
# tempFileName, tempFileExtension = os.path.splitext('/disk/' + tempRelativePath)



    # fiuUrl = "http://assets.cs.fiu.edu:3000/api/v1/digitalassets"

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