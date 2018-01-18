import requests
import base64
from json import JSONDecoder
from utils.base import isNull,save
from common.api import API

HTTP_URL="https://cloudapi.linkface.cn/"
API_ID ="90f2beea5339494586d50bcc6d8735d0"
API_SECRET="f77682ebc66a41beac860181108fcda5"
def myRequest(http_url, data, filepath="",file={}, save_file=""):
    data["api_id"] = API_ID
    data["api_secret"] = API_SECRET
    if filepath != "":
        img = open(filepath, 'rb')
        files = {"file": img}
        response = requests.post(http_url, data=data, files=files)
    elif file != {}:
        response = requests.post(http_url, data=data, files=file)
    else:
        response = requests.post(http_url, data=data)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    save(save_file, req_dict)
    return req_dict

class Linkface(API):
    def __init__(self):
        pass

    def detect(self,filepath,auto_rotate="false", save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"face/face_detect"
        data = {"auto_rotate":auto_rotate}
        return myRequest( http_url, data, filepath, save_file)

    def attribute(self,filepath,auto_rotate="false", save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"face/face_attributes_detect"
        data = {"auto_rotate":auto_rotate}
        return myRequest( http_url, data, filepath, save_file)

    #当图片中存在多个人脸时，系统会选出其中最大的人脸进行比对。
    def compare(self,selfie_file, historical_selfie_file,selfie_auto_rotate="false",historical_selfie_auto_rotate="false", save_file=""):
        if isNull(selfie_file) or isNull(historical_selfie_file):
            return
        http_url = HTTP_URL+"identity/historical_selfie_verification"

        img1 = open(selfie_file, 'rb')
        #img1 = base64.b64encode(img1.read())
        img2 = open(historical_selfie_file, 'rb')
        #img2 = base64.b64encode(img2.read())
        data = {"selfie_auto_rotate": selfie_auto_rotate,
                "historical_selfie_auto_rotate": historical_selfie_auto_rotate}
        file = {"selfie_file": img1,
                "historical_selfie_file": img2}
        return myRequest(http_url, data,file=file, save_file=save_file)

    # 要求每张图片的人脸不超过4个！
    def compareFaces(self,image_one_file, image_two_file,image_one_auto_rotate="false",image_two_auto_rotate="false", save_file=""):
        if isNull(image_one_file) or isNull(image_two_file):
            return
        http_url = HTTP_URL+"identity/compare_faces_in_two_images"

        img1 = open(image_one_file, 'rb')
        img2 = open(image_two_file, 'rb')
        data = {"image_one_file": img1,
                "historical_selfie_file": img2,
                "image_one_auto_rotate": image_one_auto_rotate,
                "image_two_auto_rotate": image_two_auto_rotate}
        return myRequest( http_url, data, save_file)

    def search(self, name, selfie_file,image_auto_rotate="false", save_file=""):
        if isNull(name) or isNull(selfie_file):
            return
        http_url = HTTP_URL+"search/image/search"

        img = open(selfie_file, 'rb')
        data = {"name": name,
                "historical_selfie_file": img,
                "image_auto_rotate": image_auto_rotate}
        return myRequest(http_url, data, save_file)

class FaceSet(object):
    def __init__(self,name, desc="", save_file=""):
        http_url = HTTP_URL + "search/db/create"

        data = {"name": name}
        if desc != "":
            data["desc"] = desc

        myRequest( http_url, data, save_file)

        self.name = name

    def delete_faceSet(self, save_file=""):

        http_url = HTTP_URL+"search/db/delete"

        data = {"name": self.name}

        return myRequest( http_url, data, save_file)


    def getDetail_faceSet(self, save_file=""):
        http_url = HTTP_URL+"search/db/info"

        data = {"name": self.name}

        return myRequest( http_url, data, save_file)


    def get_faceSet(self, save_file=""):
        http_url = HTTP_URL+"search/db/list"

        data = {}
        return myRequest( http_url, data, save_file)

    def getList_faceSet(self, save_file=""):
        http_url = HTTP_URL+"search/db/person_list"

        data = {"name": self.name}

        return myRequest( http_url, data, save_file)


    def addFace_faceSet(self, selfie_file,selfie_auto_rotate="false",person_uuid="",desc="", save_file=""):
        if isNull(selfie_file):
            return
        http_url = HTTP_URL+"search/image/insert"
        img = open(selfie_file, 'rb')
        data = {"name": self.name,
                "selfie_file": img,
                "selfie_auto_rotate": selfie_auto_rotate}
        if not isNull(person_uuid):
            data["person_uuid"]=person_uuid
        if not isNull(desc):
            data["desc"] = desc


        return myRequest( http_url, data,selfie_file, save_file)

    def removeFace_faceSet(self, selfie_image_id, save_file=""):
        if isNull(selfie_image_id):
            return
        http_url = HTTP_URL+"search/image/delete"

        data = {"name": self.name,
                "selfie_image_id": selfie_image_id}

        return myRequest( http_url, data, save_file)

    def removePerson_faceSet(self, person_uuid, save_file=""):
        if isNull(person_uuid):
            return
        http_url = HTTP_URL+"search/image/delete_person"

        data = {"name": self.name,
                "person_uuid": person_uuid}

        return myRequest( http_url, data, save_file)





