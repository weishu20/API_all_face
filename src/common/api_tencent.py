import requests
import json
import base64
from json import JSONDecoder
import random
import time
from utils.base import isNull,save,to_sha1_base64_tencent
from common.api import API

HTTP_URL = "http://service.image.myqcloud.com/face/"

APPID="10114911"
BUCKET="1362663533-1255821374"
SECRET_ID="AKID9D9uWzWiLlz3xuq2GMG0d9UVQCqPm9pa"
SECRET_KEY=b'2jVcedZKtJcjeS4VkBXpz3veBVr7FB1m'

def getAuthorzation():
    current = time.time()
    expired = current+2592000
    rdm = random.randint(1,9999999999)
    userid = 0
    fileid = ""
    stringToSign = 'a='+APPID+'&b='+BUCKET+'&k='+SECRET_ID+'&e='+str(expired)\
                   +'&t='+str(current)+'&r='+str(rdm)+'&u='+str(userid)+'&f='
    signature = to_sha1_base64_tencent(stringToSign.encode(), SECRET_KEY)
    return signature.decode()

AUTHORIZATION=getAuthorzation() #b'd5PHfwzDXZcXlwTcKwVh7lDe8OM='

HEADERS1 = {#"Content-Type": "multipart/form-data",
           "Authorization": AUTHORIZATION}
HEADERS2 = {#"Content-Type": "application/json",
                 "Authorization":AUTHORIZATION}

def myRequest(http_url, data,filepath="", save_file=""):
    data["appid"] = APPID
    if filepath != "":
        img = open(filepath, 'rb')
        #img = base64.b64encode(img.read())
        files = {"image": img}
        response = requests.post(http_url, data=data, files=files, headers=HEADERS1)
        # data["image"]=img
        # response = requests.post(http_url, data=data, headers=HEADERS2)
    else:
        response = requests.post(http_url, data=data, headers=HEADERS2)
    print(response)
    try:
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        save(save_file, req_dict)
        return req_dict
    except:
        return {}

def myRequest2(http_url, data,filepath1,filepath2, save_file=""):
    data["appid"] = APPID
    img1 = open(filepath1, 'rb')
    #img1 = base64.b64encode(img1.read())
    img2 = open(filepath2, 'rb')
    #img2 = base64.b64encode(img2.read())
    files = {"imageA":img1,
             "imageB":img2}
    response = requests.post(http_url, data=data,files = files, headers=HEADERS1)
    print(response)
    try:
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        save(save_file, req_dict)
        return req_dict
    except:
        return {}

class Tencent(API):
    def __init__(self):
        pass

    def detect(self,filepath,mode=0,save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"detect"
        data = {"mode": mode}
        return myRequest( http_url, data, filepath, save_file)

    def shape(self, filepath, mode=0, save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL + "shape"
        data = {"mode": mode}
        return myRequest(http_url, data, filepath, save_file)



    def compare(self,file1, file2,save_file=""):
        if isNull(file1) or isNull(file2):
            return
        http_url = HTTP_URL+"compare"
        data = {}
        return myRequest2(http_url, data,file1,file2, save_file)

    def search(self,filepath, group_id, save_file=""):
        if isNull(filepath) or isNull(group_id):
            return
        http_url = HTTP_URL+"identify"

        data = {"group_id": group_id}

        return myRequest(http_url, data, filepath, save_file)


    def verify(self,filepath, person_id, save_file=""):
        if isNull(person_id) or isNull(filepath):
            return
        http_url = HTTP_URL+"verify"

        data = {"person_id": person_id}

        return myRequest(http_url, data, filepath, save_file)


class Face(object):
    def __init__(self,face_id):
        self.face_id = face_id

    def getInfo_Face(self, save_file=""):
        http_url = HTTP_URL+"getfaceinfo"

        data = {"Face_id": self.face_id}
        return myRequest(http_url, data, save_file)

class Person(object):
    def __init__(self, person_id,group_ids,filepath,person_name="",tag="",save_file=""):
        if isNull(person_id)or isNull(group_ids)or isNull(filepath):
            return
        http_url = HTTP_URL+"newperson"

        data = {"person_id": person_id,
                "group_ids": group_ids}
        if person_name != "":
            data["person_name"] = person_name
        if tag != "":
            data["tag"] = tag
        ##可以是多张图片
        myRequest(http_url, data, filepath, save_file)
        self.person_id = person_id

    def deletePerson(self,  save_file=""):
        http_url = HTTP_URL+"delperson"

        data = {"person_id": self.person_id}

        return myRequest(http_url, data, save_file)

    def addFace_Person(self, filepath, save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"addface"

        data = {"person_id": self.person_id}

        return myRequest(http_url, data,filepath, save_file)

    def deleteFace_Person(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"delface"

        data = {"person_id": self.person_id,
                "face_ids":face_ids}

        return myRequest(http_url, data, save_file)

    def setInfo_Person(self,person_name="", tag="", save_file=""):
        http_url = HTTP_URL+"setinfo"

        data = {"person_id": self.person_id}
        if person_name != "":
            data["person_name"] = person_name
        if tag != "":
            data["tag"] = tag
        return myRequest(http_url, data, save_file)

    def getInfo_Person(self, save_file=""):
        http_url = HTTP_URL+"getinfo"

        data = {"person_id": self.person_id}
        return myRequest(http_url, data, save_file)

    def getList_Person(self, save_file=""):
        http_url = HTTP_URL+"getfaceids"

        data = {"person_id": self.person_id}
        return myRequest(http_url, data, save_file)


class Group(object):
    def __init__(self,group_id):
        self.group_id = group_id

    def getlist_group(self,save_file=""):
        http_url = HTTP_URL + "getgroupids"
        data={}
        return myRequest(http_url, data, save_file)

    def getPersons(self, save_file=""):
        http_url = HTTP_URL + "getpersonids"

        data = {"group_id": self.group_id}

        return myRequest(http_url, data, save_file)

    def copyPerson(self,person_id,src_group_id, save_file=""):
        if isNull(person_id) or isNull(src_group_id):
            return
        http_url = HTTP_URL + "faceset/group/addperson"

        data = {"group_id": self.group_id,
                "person_id": person_id,
                "src_group_id": src_group_id}

        return myRequest(http_url, data, save_file)
    def deleteOnePerson(self, person_id, save_file=""):
        if isNull(person_id):
            return
        http_url = HTTP_URL+"faceset/group/deleteperson"

        data = {"person_id": person_id,
                "group_id":self.group_id}

        return myRequest(http_url, data, save_file)