import requests
import json
import os
import config

subscription_key = config.face_api_key
assert subscription_key

face_api_url = config.face_api_url

img_data = open(
    'cloud-detector/resources/Dagestani_man_and_woman.jpg', 'rb').read()

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params, data=img_data,
                         headers=headers)
print(json.dumps(response.json()))
