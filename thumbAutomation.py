# -*- coding: UTF-8 -*-
import requests
import exifread

# GET RELATIVE URLS FROM FILE AND MAKE ABSOLUTE PATHS
with open('dataAdded.txt') as f: #change to dataAdded.txt
    relativePaths = f.read().splitlines()

# print "\nrelativePaths List"
# print "=================="
# print(relativePaths)

# print "\nrelativePaths type"
# print "=================="
#list
# print type(relativePaths) 

# print "\nrelativePaths length"
# print "===================="
# print len(relativePaths)

absolutePathPrefix = '/disk/'
absolutePaths = [absolutePathPrefix + x for x in relativePaths]

# print "\nabsolutePaths List"
# print "=================="
# print(absolutePaths)

# print "\nabsolutePaths type"
# print "=================="
#list
# print type(absolutePaths)

# print "\nabsolutePaths length"
# print "===================="
# print len(absolutePaths)

 # GET ALL IMAGES FROM DATABASE AND GET ID

get_url = "http://assets.cs.fiu.edu:3000/api/v1/digitalassets"

headers = {
'cache-control': "no-cache",
'postman-token': "2d5ecaf6-fa57-fb91-de5b-53840ef16c41"
}

allImages = requests.request("GET", get_url, headers=headers)

# for index, y in  enumerate(allImages.json()['response']):
#     print index
#     print y['url'] #unicode
#     print type(y['url']) #unicode
#     print y['url'].encode('ascii', 'ignore') #string
#     print type(y['url'].encode('ascii', 'ignore')) #string
#     print y['_id']
#     print type(y['_id']) #unicode
#     print y['_id'].encode('ascii', 'ignore')
#     print type(y['_id'].encode('ascii', 'ignore')) #string
    
# LOOP THROUGH ABSOLUTE PATHS
for index, x in enumerate(absolutePaths):
    # print allImages.json()['response'][index]['url'].encode('ascii', 'ignore')
    # print type(allImages.json()['response'][index]['url'].encode('ascii', 'ignore'))
    # print allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')
    # print type(allImages.json()['response'][index]['_id'].encode('ascii', 'ignore'))
    
    print "\nabsolutePath"
    print "==="
    print x

    print "\nindex"
    print "====="
    print index

    # print "\nindex type"
    # print "=========="
    #int
    # print type(index) 
    # print "\n"

    # GET EXIF DATA
    # Open image file for reading (binary mode)
    f = open(x, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    # print tags
    # print tags["Image Make"]
    # print tags["Image Model"]
    # print tags["EXIF ExifImageWidth"]
    # print tags["EXIF ExifImageLength"]
    # print tags["EXIF DateTimeOriginal"]
    # print tags["EXIF FileSource"]
    # print tags["EXIF ExposureMode"]
    # print tags["EXIF ExposureTime"]
    # print tags["EXIF MaxApertureValue"]
    # print tags["EXIF ISOSpeedRatings"]
    # print tags["EXIF ExposureBiasValue"]
    # print tags["EXIF Flash"]
    # print tags["Image Orientation"]

    print "\n"
    #dict
    # print type(tags)
    #string
    # print type(tags["Image Make"].__class__.__name__)
    # print tags.get("Image Make")
    # print str(tags["Image Make"])
    # UPDATE EXIF DATA USING ID

    # url = "http://localhost:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')
    url = "http://assets.cs.fiu.edu:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')#use in access.cs.fiu.edu
    # print url

    # if str(tags["EXIF FileSource"]) is None:
    payload = "{\"exif\": {\"make\": \"" + str(tags["Image Make"]) + "\",\"model\": \"" + str(tags["Image Model"]) + "\",\"width\": " + str(tags["EXIF ExifImageWidth"]) + ",\"length\": " + str(tags["EXIF ExifImageLength"]) + ",\"created\": \"" + str(tags["EXIF DateTimeOriginal"]) + "\"}}" 
    # payload = "{\"exif\": {\"make\": \"" + str(tags["Image Make"]) + "\",\"model\": \"" + str(tags["Image Model"]) + ",\"created\": \"" + str(tags["EXIF DateTimeOriginal"]) + "\"}}"
    # else:
    #      payload = "{\"exif\": {\"make\": \"" + str(tags["Image Make"]) + "\",\"model\": \"" + str(tags["Image Model"]) + "\",\"width\": " + str(tags["EXIF ExifImageWidth"]) + ",\"length\": " + str(tags["EXIF ExifImageLength"]) + ",\"created\": \"" + str(tags["EXIF DateTimeOriginal"]) + "\",\"fileSource\": \"" + str(tags["EXIF FileSource"]) + "\",\"exposureMode\":\"" + str(tags["EXIF ExposureMode"]) + "\",\"exposureTime\": \"" + str(tags["EXIF ExposureTime"]) + "\",\"aperture\": \"" + str(tags["EXIF MaxApertureValue"]) + "\", \"iso\": \"" + str(tags["EXIF ISOSpeedRatings"]) + "\",\"flash\": \"" + str(tags["EXIF Flash"]) + "\",\"orientation\": \"" + str(tags["Image Orientation"]) + "\"}}"

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "fde7de20-b559-351c-0521-354ec6436131"
        }

    response = requests.request("PUT", url, data=payload, headers=headers)

    # print(response.text)