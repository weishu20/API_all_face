import requests
import cv2
import json
import base64
from json import JSONDecoder
import random
import time
import struct
from utils.base import isNull,save
from common.api import API

HTTP_URL = "https://api.cognitive.azure.cn/face/v1.0/"

OCPAPIMSUBSCRIPTIONKEY= "0b51d2c1e79646c497a238e9b080f050"
HEADERS1 = {"Content-Type":"application/octet-stream",
            "Ocp-Apim-Subscription-Key": OCPAPIMSUBSCRIPTIONKEY}

HEADERS2 = {"Content-Type":"application/json",
            "Ocp-Apim-Subscription-Key": OCPAPIMSUBSCRIPTIONKEY}
def myRequest(http_url, data,filepath="", save_file=""):
    if filepath != "":
        img = open(filepath, 'rb')
        #img = base64.b64encode(img.read())

        #data["image"] = img.read().decode()
        #img = cv2.imread(filepath)
        files = {"image": img}
        response = requests.post(http_url,files = files,headers=HEADERS1)
    else:
        response = requests.post(http_url, data=data, headers=HEADERS2)
    try:
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        save(save_file, req_dict)
        return req_dict
    except:
        return {}

class Microsoft(object):
    def __init__(self):
        pass

    def detect(self,filepath,returnFaceId="true",returnFaceLandmarks="false",returnFaceAttributes="",save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"detect?"+"returnFaceId="+ returnFaceId+"&returnFaceLandmarks="+returnFaceLandmarks
        if not isNull(returnFaceAttributes):
            http_url = http_url +"&returnFaceAttributes="+returnFaceAttributes
        data = {}
        # data = {"returnFaceId": returnFaceId,
        #         "returnFaceLandmarks": returnFaceLandmarks}
        # if not isNull(returnFaceAttributes):
        #     data["returnFaceAttributes"] = returnFaceAttributes
        return myRequest(http_url, data, filepath, save_file)

    def verify(self,faceId1, faceId2, save_file=""):
        if isNull(faceId1) or isNull(faceId2):
            return
        http_url = HTTP_URL+"verify"

        data = {"faceId1": faceId1,
                "faceId2": faceId2}
        return myRequest(http_url, data, save_file)
