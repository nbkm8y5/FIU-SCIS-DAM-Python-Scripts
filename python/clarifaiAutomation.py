# -*- coding: UTF-8 -*-
import requests
import json
import os
# import exifread


# GET RELATIVE URLS FROM FILE AND MAKE URLS
with open('dataBeingAdded.txt') as f:
    relativePaths = f.read().splitlines()

# print "\nrelativePaths List"
# print "=================="
# print(relativePaths[0:1])

# print "\nrelativePaths type"
# print "=================="
# print type(relativePaths) #list

# print "\nrelativePaths length"
# print "===================="
# print len(relativePaths)

urlDomain = 'http://assets.cs.fiu.edu:3000/'
urls = [urlDomain + x for x in relativePaths]

# print"\nurls List"
# print "========="
# print urls[0:1]

# print"\nurls type"
# print "========="
# print type(urls) #list

# print"\nurls length"
# print "==========="
# print len(urls)


# GET TOKEN

tokenUrl = "https://api.clarifai.com/v2/token"

# print"\ntokenUrl"
# print "============="
# print tokenUrl

# print"\ntokenHeaders type"
# print "=================="
# print type(tokenUrl) #str

tokenHeaders = {
    'authorization': "Basic",
    'cache-control': "no-cache",
    'postman-token': "5c599874-45c2-fbc6-3c21-a4b8f967ae64"
    }

# print"\ntokenHeaders"
# print "============="
# print tokenHeaders

# print"\ntokenHeaders type"
# print "=================="
# print type(tokenHeaders) #dict

tokenResponse = requests.request("POST", tokenUrl, headers=tokenHeaders)

# print"\ntokenResponse"
# print "============="
# print tokenResponse

# print"\ntokenResponse type"
# print "=================="
# print type(tokenResponse) #class

# print"\ntokenResponse.json()"
# print "===================="
# print tokenResponse.json()

# print"\ntokenResponse.json() type"
# print "========================="
# print type(tokenResponse.json()) #dict

# print"\njson.dump(tokenResponse.json())"
# print "==============================="
# print json.dumps(tokenResponse.json())

# print"\njson.dump(tokenResponse.json()) type"
# print "===================================="
# print type(json.dumps(tokenResponse.json())) #str

# print"\ntokenResponse.json()[\"access_token\"]"
# print "===================================="
# print tokenResponse.json()["access_token"]

# print"\ntokenResponse.json()[\"access_token\"] type"
# print "========================================="
# print type(tokenResponse.json()["access_token"]) #unicode


# GET CLARIFAI API INFORMATION

clarifaiUrl = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
# moreno.ronline@gmail.com
clarifaiHeaders = {
    'Authorization': "Bearer",
    'Content-Type' : "application/json"
    }
# moreno.rbusiness@gmail.com
# clarifaiHeaders = {
#     'Authorization': "Bearer " + tokenResponse.json()["access_token"],
#     'Content-Type' : "application/json"
#     }

# print"\nclarifaiHeaders"
# print "=============="
# print clarifaiHeaders

# print"\nclarifaiHeaders type"
# print "==================="
# print type(clarifaiHeaders) #dict

for index, x in enumerate(urls):
    
    # print "\nurl"
    # print "==="
    # print x

    # print "\nindex"
    # print "====="
    # print i

    # print "\nindex type"
    # print "=========="
    # print type(i) #int

    payload = {
        "inputs": [
            {
            "data": {
                "image": {
                "url": x
                }
            }
            }
        ]
        }
    
    encodedPayload = json.dumps(payload)
    
    # print "\npayload"
    # print "======="
    # print payload

    # print "\npayload type"
    # print "============"
    # print type(payload) #dict

    # print "\nencodedPayload"
    # print "=============="
    # print encodedPayload

    # print "\nencodedPayload type"
    # print "==================="
    # print type(encodedPayload) #str

    clarifaiResponse = requests.request("POST", clarifaiUrl, headers=clarifaiHeaders, data=encodedPayload)

    # print "\nclarifaiResponse"
    # print "================="
    # print clarifaiResponse

    # print "\nclarifaiResponse type"
    # print "====================="
    # print type(clarifaiResponse) #class

    # print "\nclarifaiResponse.json()"
    # print "======================="
    # print clarifaiResponse.json()

    # print "\nclarifaiResponse.json() type"
    # print "============================"
    # print type(clarifaiResponse.json()) #dict

    tempConcepts = clarifaiResponse.json()["outputs"][0]["data"]["concepts"]

    encodedTempConcepts = json.dumps(tempConcepts)

    # print "\ntempConcepts"
    # print "============"
    # print tempConcepts

    # print "\ntempConcepts type"
    # print "================="
    # print type(tempConcepts) #list

    tempConceptsList = []
    for concept in tempConcepts:
        tempConceptsDict = {
            'name' : concept["name"],
            'value' : concept["value"]
        }
        tempConceptsList.append(tempConceptsDict)

    
    # print len(tempList)
    # print tempList
    # print type(tempList)

# PASS IMAGE DATA TO MONGODB IN ASSETS.CS.FIU.EDU

    fiuUrl = "http://localhost:3000/api/v1/digitalassets"

    tempRelativePath = relativePaths[index]
    tempFileName, tempFileExtension = os.path.splitext('/disk/' + tempRelativePath)
    b = os.path.getsize('/disk/' + tempRelativePath)

    # Open image file for reading (binary mode)
    # f = open('/disk/' + tempRelativePath, 'rb')
    # Return Exif tags
    # tags = exifread.process_file(f)

    # tempExifDict = {
    #     'make' : tags["Image Make"],
    #     'model': tags["Image Model"],
    #     'width': tags["EXIF ExifImageWidth"],
    #     'length' : tags["EXIF ExifImageLength"],
    #     'created' : tags["EXIF DateTimeOriginal"],
    #     'fileSource': tags["EXIF FileSource"],
    #     'exposureMode': tags["EXIF ExposureMode"],
    #     'exposureTime': tags["EXIF ExposureTime"],
    #     'aperture' : tags["EXIF MaxApertureValue"],
    #     'iso' : tags["EXIF ISOSpeedRatings"],
    #     'exposureBias' : tags["EXIF ExposureBiasValue"],
    #     'flash' : tags["EXIF Flash"],
    #     'orientation' : tags["Image Orientation"]
    # }

    

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
    # print type(tags)

    # print json.dumps(tempExifDict, ensure_ascii=False)


    modelPayload = {
            'fileName': tempFileName,
            'title': 'CHANGE',
            'caption': 'CHANGE',
            'altText': 'CHANGE',
            'description': 'CHANGE',
            'fileType': tempFileExtension,
            'uploadedBy': 'rmore071',
            'fileSize': b,
            'url': x,
            'relativePath': tempRelativePath,
            'tags': tempConceptsList
            # 'exif': tempExifDict
            }

    fiuResponse = requests.request("POST", fiuUrl, json=modelPayload)
    print index
    # print json.dumps(fiuResponse.json())  