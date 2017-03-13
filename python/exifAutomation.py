# -*- coding: UTF-8 -*-
# Greasyhacks image dimensions automation
#
import requests
from PIL import Image
import struct
import imghdr
from io import BytesIO

 # GET ALL IMAGES FROM DATABASE AND GET ID

try:
    allImages = requests.get("http://assets.cs.fiu.edu:3000/api/v1/digitalassets")
except ConnectionError as e:
   print e
   allImages = "No response from API GET /digitalassets"

for index, y in enumerate(allImages.json()['response']):

    try:
        imageFile = requests.get(y['url'].encode('ascii', 'ignore'))
    except ConnectionError as e:
        print e
        allImages = "No response from API GET /digitalassets"

    image = Image.open(BytesIO(imageFile.content))

    put_url = "http://assets.cs.fiu.edu:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')
  
    put_urlpayload = "{\"exif.width\": " + str(image.size[0]) + ",\"exif.length\": " + str(image.size[1]) + "}"

    headers_two = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

    try:
        response = requests.request("PUT", put_url, data=put_urlpayload, headers=headers_two)
        print(response.text)
    except ConnectionError as e:
        print e
        response = "No response from API PUT /digitalassets/:id"