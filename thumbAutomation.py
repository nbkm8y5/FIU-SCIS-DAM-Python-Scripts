# -*- coding: UTF-8 -*-
#THIS IS READY TO GO
import requests
import os

get_url = "http://localhost:3000/api/v1/digitalassets"

headers = {
'cache-control': "no-cache",
'postman-token': "2d5ecaf6-fa57-fb91-de5b-53840ef16c41"
}

allImages = requests.request("GET", get_url, headers=headers)

for index, y in  enumerate(allImages.json()['response']):
    print index
    print y['url'] #unicode
    print type(y['url']) #unicode
    print y['url'].encode('ascii', 'ignore') #string
    print type(y['url'].encode('ascii', 'ignore')) #string
    print y['_id']
    print type(y['_id']) #unicode
    print y['_id'].encode('ascii', 'ignore')
    print type(y['_id'].encode('ascii', 'ignore')) #string

    url = "http://localhost:3000/api/v1/digitalassets/" + allImages.json()['response'][index]['_id'].encode('ascii', 'ignore')
    print os.path.basename(y['url'].encode('ascii', 'ignore'))
    payload = "{\"thumbnailUrl\": \"http://assets.cs.fiu.edu:3000/assets/thumbnails/thumbnail-" + os.path.basename(y['url'].encode('ascii', 'ignore')) + "\"}"
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "a96c6dd1-ace4-9d19-c145-1d488eb531a7"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    print(response.text)

  