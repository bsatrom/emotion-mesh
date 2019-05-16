import requests
import json
import os
import config
import operator
import argparse

import cognitive_face as CF
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--image_path',
                    help='Path to a local image file to process',
                    default='webcam-what-demo.png')
args = parser.parse_args()

subscription_key = config.face_api_key
assert subscription_key

face_api_url = config.face_api_url
assert face_api_url

image_base_path = 'cloud-detector/resources/'
image_name = os.path.splitext(args.image_path)[0]
image_path = image_base_path + args.image_path

CF.Key.set(subscription_key)
CF.BaseUrl.set(face_api_url)

attrs = 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'

faces = CF.face.detect(image_path, face_id=True,
                       landmarks=False, attributes=attrs)


def getCoordsForText(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    return (left, top - 10)

# Convert width height to a point in a rectangle


def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))


def getMainEmotion(faceDictionary):
    # Get the emotion collection and sort in acending order to get the top result
    emotions = faceDictionary['faceAttributes']['emotion']
    # print(emotions)
    emotions = sorted(emotions, key=emotions.get, reverse=True)
    return emotions[0]


img = Image.open(image_path)

# For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)
for face in faces:
    # draw a rectangle on each face
    draw.rectangle(getRectangle(face), outline='red')
    # write the predominant emotion over the bounding box
    draw.text(getCoordsForText(face), getMainEmotion(
        face), fill=(255, 255, 255, 255))

# Display the image in the users default image browser.
img.show()
img.save(image_base_path + image_name + "_modified.png", "PNG")

# print(faces)
