# -*- coding: UTF-8 -*-
import requests
import exifread
import struct
import imghdr

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height

# GET RELATIVE URLS FROM FILE AND MAKE ABSOLUTE PATHS
with open('data.txt') as f: #change to dataAdded.txt
    relativePaths = f.read().splitlines()

# print "\nrelativePaths List"
# print "=================="
# print(relativePaths)

# print "\nrelativePaths type"
# print "=================="
# list
# print type(relativePaths) 

# print "\nrelativePaths length"
# print "===================="
# print len(relativePaths)

 # GET ALL IMAGES FROM DATABASE AND GET ID

get_url = "http://localhost:3000/api/v1/digitalassets"

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
    
# LOOP THROUGH RELATIVE PATHS

countWithExif = 0
countWithOutExif = 0
countWithOutImageTuple = 0

for index, relativePath in enumerate(relativePaths):
    # print allImages.json()['response'][index]['url'].encode('ascii', 'ignore')
    # print type(allImages.json()['response'][index]['url'].encode('ascii', 'ignore'))
    # print allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')
    # print type(allImages.json()['response'][index]['_id'].encode('ascii', 'ignore'))
    
    print "\nrelativePath"
    print "==="
    print relativePath

    print "\nindex"
    print "====="
    print index

    # GET EXIF DATA
    # Open image file for reading (binary mode)
    f = open(relativePath, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    
    if "EXIF ExifImageWidth" in tags:
        countWithExif += 1
        if "Image Orientation" in tags:
            
            if "Image Make" in tags:
                
                print tags["Image Make"]
                print tags["Image Model"]
                print tags["EXIF ExifImageWidth"]
                print tags["EXIF ExifImageLength"]
                print tags["EXIF DateTimeOriginal"]
                print tags["Image Orientation"]

                #dict
                # print type(tags)
                #string
                # print type(tags["Image Make"].__class__.__name__)
                # print tags.get("Image Make")
                # print str(tags["Image Make"])
                # UPDATE EXIF DATA USING ID

                put_url = "http://localhost:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')
                print "\nurl"
                print "====="
                print put_url

                put_urlpayload = "{\"exif\": {\"make\": \"" + str(tags["Image Make"]) + "\",\"model\": \"" + str(tags["Image Model"]) + "\",\"width\": " + str(tags["EXIF ExifImageWidth"]) + ",\"length\": " + str(tags["EXIF ExifImageLength"]) + ",\"created\": \"" + str(tags["EXIF DateTimeOriginal"]) + "\",\"orientation\": \"" + str(tags["Image Orientation"]) + "\"}}"

                print "\npayload"
                print "====="
                print put_urlpayload

                headers_two = {
                    'content-type': "application/json",
                    'cache-control': "no-cache",
                    'postman-token': "fde7de20-b559-351c-0521-354ec6436131"
                    }

                response = requests.request("PUT", put_url, data=put_urlpayload, headers=headers_two)

                print(response.text)
    else:
        countWithOutExif += 1
        print"\nImages Width and Length"
        imageTuple = get_image_size(relativePath)

        if imageTuple is not None:
            
            print imageTuple
            print imageTuple[0]
            print imageTuple[1]

            put_url_no_exif = "http://localhost:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')

            print "\nurl"
            print "====="
            print put_url_no_exif

            put_url_no_exif_payload = "{\"exif\": {\"width\": " + str(imageTuple[0]) + ",\"length\": " + str(imageTuple[1]) + "\"}}"

            print "\npayload"
            print "====="
            print put_url_no_exif_payload

            headers_three = {
                        'content-type': "application/json",
                        'cache-control': "no-cache",
                        'postman-token': "fde7de20-b559-351c-0521-354ec6436131"
                        }

            responseTwo = requests.request("PUT", put_url_no_exif, data=put_url_no_exif_payload, headers=headers_three)

            print(responseTwo.text)
        else:
            countWithOutImageTuple +=1

            put_url_no_image_tuple = "http://localhost:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')

            print "\nurl"
            print "====="
            print put_url_no_image_tuple

            put_url_no_image_tuple_payload = "{\"exif\": {\"width\": " + str(3200) + ",\"length\": " + str(2400) + "\"}}"

            print "\npayload"
            print "====="
            print put_url_no_image_tuple_payload

            headers_four = {
                        'content-type': "application/json",
                        'cache-control': "no-cache",
                        'postman-token': "fde7de20-b559-351c-0521-354ec6436131"
                        }

            responseThree = requests.request("PUT", put_url_no_image_tuple, data=put_url_no_image_tuple_payload, headers=headers_four)

            print(responsethree.text)

    print "\nCount with Exif Width and Length: ", countWithExif
    print "\nCount without Exif: ", countWithOutExif
    print "\nCount without Image Tuple: ", countWithOutImageTuple
    print "\nTotal: ", countWithOutExif + countWithExif