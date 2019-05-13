import requests
import json
import os
import config
import cognitive_face as CF

subscription_key = config.face_api_key
assert subscription_key

face_api_url = config.face_api_url
assert face_api_url

CF.Key.set(subscription_key)
CF.BaseUrl.set(face_api_url)

attrs = 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'

# faces = CF.face.detect('cloud-detector/resources/Dagestani_man_and_woman.jpg',
#                       face_id=True, landmarks=False, attributes=attrs)

faces = CF.face.detect('cloud-detector/resources/streamers.png',
                       face_id=True, landmarks=False, attributes=attrs)

print(faces)
