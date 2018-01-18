import requests
import base64
from json import JSONDecoder
from utils.base import isNull,save
from common.api import API

HTTP_URL = "http://api.eyekey.com/"
APP_ID = "6242aab536fe479ba79daac5c5c4aa4f"
APP_KEY = "fef6cc2e6a084835b64670b8e2da2888"

def myRequest(http_url, data, filepath="", save_file=""):
    data["app_id"] = APP_ID
    data["app_key"] = APP_KEY
    if filepath != "":
        img = open(filepath, 'rb')
        img = base64.b64encode(img.read())
        data["img"] = img
        response = requests.post(http_url, data=data)
    else:
        response = requests.post(http_url, data=data)
    print(response)
    req_con = response.content.decode('utf-8')
    try:
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        save(save_file, req_dict)
        return req_dict
    except:
        return {}

def myRequest_get(http_url, params, save_file=""):
    params["app_id"] = APP_ID
    params["app_key"] = APP_KEY
    response = requests.get(http_url, params=params)
    print(response)
    req_con = response.content.decode('utf-8')
    try:
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        save(save_file, req_dict)
        return req_dict
    except:
        return {}

class Eyekey(API):
    def __init__(self):
        pass

    def detect(self,filepath, tip="", save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"face/Check/checking"

        data = {}
        if tip != "":
            data["tip"] = tip

        return myRequest(http_url, data, filepath, save_file)


    def compare(self,file1, file2, save_file=""):
        if isNull(file1) or isNull(file2):
            return
        http_url = HTTP_URL+"face/Match/match_compare"

        params = {"face_id1": file1,
                "face_id2": file2}
        return myRequest_get(http_url, params, save_file)

    #people_id 或 people_name
    def verify(self, face_id, people_id, save_file=""):
        if isNull(face_id) or isNull(people_id):
            return
        http_url = HTTP_URL+"face/Match/match_verify"

        data = {"face_id": face_id,
                "people_id": people_id}
        return myRequest(http_url, data, save_file)

    # people_id 或 people_name
    def confirm(self,dynamicode, people_id, save_file=""):
        if isNull(dynamicode) or isNull(people_id):
            return
        http_url = HTTP_URL+"face/Match/match_confirm"

        data = {"dynamicode": dynamicode,
                "people_id": people_id}
        return myRequest(http_url, data, save_file)

    #facegather_id 或 facegather_name
    def search(self,face_id, facegather_id, count=3, save_file=""):
        if isNull(face_id) or isNull(facegather_id):
            return
        http_url = HTTP_URL+"face/Match/match_search"

        data = {"face_id": face_id,
                "facegather_id": facegather_id,
                "count": count}

        return myRequest(http_url, data, save_file)

    #crowd_id 或 crowd_name
    def identify(self,crowd_id, face_id, save_file=""):
        if isNull(crowd_id) or isNull(face_id):
            return
        http_url = HTTP_URL+"face/Match/match_identify"

        data = {"crowd_id": crowd_id,
                "face_id": face_id}
        return myRequest(http_url, data, save_file)


class People(object):
    def __init__(self,people_name="",face_id="",tip="",crowd_id="", save_file=""):
        http_url = HTTP_URL + "People/people_create"
        data = {}
        if people_name != "":
            data["people_name"] = people_name
        if face_id != "":
            data["face_id"] = face_id
        if tip != "":
            data["tip"] = tip
        if crowd_id != "":
            data["crowd_id"] = crowd_id
        req_dict = myRequest(http_url, data, save_file)

        self.people_id = req_dict["people_id"]

    def delete_people(self, save_file=""):

        http_url = HTTP_URL+"People/people_delete"

        data = {"people_id": self.people_id}

        return myRequest(http_url, data, save_file)

    def addFaces_people(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"People/people_add"

        data = {"people_id": self.people_id,
                "face_id": face_ids}

        return myRequest(http_url, data, save_file)

    def removeFaces_people(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"People/people_remove"

        data = {"people_id": self.people_id,
                "face_id": face_ids}

        return myRequest(http_url, data, save_file)

    def getInfo_people(self, type="face", save_file=""):
        http_url = HTTP_URL+"People/people_get"

        data = {"people_id": self.people_id,
                "type":type}

        return myRequest(http_url, data, save_file)

    def SetInfo_people(self, name="",tip = "", save_file=""):
        http_url = HTTP_URL+"People/people_set"

        data = {"people_id": self.people_id}
        if name != "":
            data["name"] = name
        if tip != "":
            data["tip"] = tip
        return myRequest(http_url, data, save_file)

class Crowd(object):
    def __init__(self,crowd_name="",people_id="",tip="", save_file=""):
        http_url = HTTP_URL + "Crowd/crowd_create"
        data = {}
        if crowd_name != "":
            data["crowd_name"] = crowd_name
        if people_id != "":
            data["people_id"] = people_id
        if tip != "":
            data["tip"] = tip
        req_dict = myRequest(http_url, data, save_file)

        self.crowd_id = req_dict["crowd_id"]

    def delete_crowd(self, save_file=""):

        http_url = HTTP_URL+"Crowd/crowd_delete"

        data = {"crowd_id": self.crowd_id}

        return myRequest(http_url, data, save_file)

    def addFaces_crowd(self, people_ids, save_file=""):
        if isNull(people_ids):
            return
        http_url = HTTP_URL+"Crowd/crowd_add"

        data = {"crowd_id": self.crowd_id,
                "people_id": people_ids}

        return myRequest(http_url, data, save_file)

    def removeFaces_crowd(self, people_ids, save_file=""):
        if isNull(people_ids):
            return
        http_url = HTTP_URL+"Crowd/crowd_remove"

        data = {"crowd_id": self.crowd_id,
                "people_id": people_ids}

        return myRequest(http_url, data, save_file)

    def getInfo_crowd(self, save_file=""):
        http_url = HTTP_URL+"Crowd/crowd_get"

        data = {"crowd_id": self.crowd_id}

        return myRequest(http_url, data, save_file)

class FaceGather(object):
    def __init__(self,facegather_name="",face_id="",tip="", save_file=""):
        http_url = HTTP_URL + "FaceGather/facegather_create"
        data = {}
        if facegather_name != "":
            data["facegather_name"] = facegather_name
        if face_id != "":
            data["face_id"] = face_id
        if tip != "":
            data["tip"] = tip
        req_dict = myRequest(http_url, data, save_file)

        self.facegather_id = req_dict["facegather_id"]

    def delete_facegather(self, save_file=""):

        http_url = HTTP_URL+"FaceGather/facegather_delete"

        data = {"facegather_id": self.facegather_id}

        return myRequest(http_url, data, save_file)

    def addFaces_facegather(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"FaceGather/facegather_addface"

        data = {"facegather_id": self.facegather_id,
                "face_id": face_ids}

        return myRequest(http_url, data, save_file)

    def removeFaces_facegather(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"FaceGather/facegather_removeface"

        data = {"facegather_id": self.facegather_id,
                "face_id": face_ids}

        return myRequest(http_url, data, save_file)

    def getInfo_facegather(self, save_file=""):
        http_url = HTTP_URL+"FaceGather/facegather_get"

        data = {"facegather_id": self.facegather_id}

        return myRequest(http_url, data, save_file)

    def SetInfo_facegather(self, name="",tip= "", save_file=""):
        http_url = HTTP_URL+"FaceGather/facegather_set"

        data = {"facegather_id": self.facegather_id}
        if name != "":
            data["name"] = name
        if tip != "":
            data["tip"] = tip
        return myRequest(http_url, data, save_file)

    
class Face(object):
    def __init__(self,face_id):
        self.face_id = face_id


    def landmark_face(self,type="49", save_file=""):
        http_url = HTTP_URL+"Check/check_mark"

        data = {"face_id":self.face_id,
                "type": type}

        return myRequest(http_url, data, save_file)


    def feature_face(self,type="life", save_file=""):
        http_url = HTTP_URL+"detection/feature"

        data = {"face_id":self.face_id,
                "type": type}

        return myRequest(http_url, data, save_file)



    def attributes_face(self, save_file=""):
        http_url = HTTP_URL+"detection/attributes"

        data = {"face_id":self.face_id}

        return myRequest(http_url, data, save_file)

    def beauty_face(self, save_file=""):
        http_url = HTTP_URL+"detection/beauty"

        data = {"face_id":self.face_id}

        return myRequest(http_url, data, save_file)



    def getInfo_face(self, save_file=""):
        http_url = HTTP_URL+"face/get_info"

        data = {"face_id": self.face_id}

        return myRequest(http_url, data, save_file)

    def setLabel_face(self,label, save_file=""):
        http_url = HTTP_URL+"face/set_label"

        data = {"face_id": self.face_id,
                "label": label}

        return myRequest(http_url, data, save_file)

