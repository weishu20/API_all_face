import requests

from json import JSONDecoder
from utils.base import isNull,save
from common.api import API

HTTP_URL = "http://api.faceall.cn/v2/"
API_KEY = ""
API_SECRET = ""


def myRequest( http_url, data, filepath="", save_file=""):
    data["api_key"] = API_KEY
    data["api_secret"] = API_SECRET
    if filepath != "":
        img = open(filepath, 'rb')
        files = {"img_file": img}
        response = requests.post(http_url, data=data, files=files)
    else:
        response = requests.post(http_url, data=data)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    save(save_file, req_dict)
    return req_dict

class Faceall(API):
    def __init__(self):
        pass

    def detect(self,filepath, attributes="false", save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"detection/detect"

        data = {"attributes": attributes}

        return myRequest( http_url, data, filepath, save_file)

    def compare(self,file1, file2, type="life", save_file=""):
        if isNull(file1) or isNull(file2):
            return
        http_url = HTTP_URL+"recognition/compare_face"

        data = {"type": type}
        data["face_id1"] = file1
        data["face_id2"] = file2
        return myRequest( http_url, data, save_file)

    def search(self,face_id, faceset_id, limit=5, save_file=""):
        if isNull(face_id) or isNull(faceset_id):
            return
        http_url = HTTP_URL+"recognition/compare_face_faceset"


        data = {"face_id": face_id,
                "faceset_id": faceset_id,
                "limit": limit}

        return myRequest( http_url, data, save_file)


class FaceSet(object):
    def __init__(self,faceset_name="", save_file=""):
        http_url = HTTP_URL + "faceset/create"
        data = {}
        if faceset_name != "":
            data["faceset_name"] = faceset_name
        req_dict = myRequest( http_url, data, save_file)

        self.faceset_id = req_dict["id"]

    def delete_faceSet(self, save_file=""):

        http_url = HTTP_URL+"faceset/delete"

        data = {"faceset_id": self.faceset_id}

        return myRequest( http_url, data, save_file)

    def addFaces_faceSet(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"faceset/add_faces"

        data = {"faceset_id": self.faceset_id,
                "face_id": face_ids}

        return myRequest( http_url, data, save_file)

    def removeFaces_faceSet(self, face_ids, save_file=""):
        if isNull(face_ids):
            return
        http_url = HTTP_URL+"faceset/remove_faces"

        data = {"faceset_id": self.faceset_id,
                "face_id": face_ids}

        return myRequest( http_url, data, save_file)


    def train_faceSet(self, type = "life",async="true", save_file=""):
        http_url = HTTP_URL+"faceset/train"

        data = {"faceset_id": self.faceset_id,
                "type": type,
                "async": async}

        return myRequest( http_url, data, save_file)

    def get_faceSetList(self, save_file=""):
        http_url = HTTP_URL+"faceset/get_list"
        data = {}
        return myRequest( http_url, data, save_file)

    def getInfo_faceSet(self, save_file=""):
        http_url = HTTP_URL+"faceset/get_info"

        data = {"faceset_id": self.faceset_id}

        return myRequest( http_url, data, save_file)

    def SetInfo_faceSet(self, faceset_name, save_file=""):
        if isNull(faceset_name):
            return
        http_url = HTTP_URL+"faceset/set_info"

        data = {"faceset_id": self.faceset_id,
                "faceset_name": faceset_name}

        return myRequest( http_url, data, save_file)



class Face(object):
    def __init__(self,face_id):
        self.face_id = face_id

    def feature_face(self,type="life", save_file=""):
        http_url = HTTP_URL+"detection/feature"

        data = {"face_id":self.face_id,
                "type": type}

        return myRequest( http_url, data, save_file)

    def landmark_face(self,type="68p", save_file=""):
        http_url = HTTP_URL+"detection/landmark"

        data = {"face_id":self.face_id,
                "type": type}

        return myRequest( http_url, data, save_file)

    def attributes_face(self, save_file=""):
        http_url = HTTP_URL+"detection/attributes"

        data = {"face_id":self.face_id}

        return myRequest( http_url, data, save_file)

    def beauty_face(self, save_file=""):
        http_url = HTTP_URL+"detection/beauty"

        data = {"face_id":self.face_id}

        return myRequest( http_url, data, save_file)



    def getInfo_face(self, save_file=""):
        http_url = HTTP_URL+"face/get_info"

        data = {"face_id": self.face_id}

        return myRequest( http_url, data, save_file)

    def setLabel_face(self,label, save_file=""):
        http_url = HTTP_URL+"face/set_label"

        data = {"face_id": self.face_id,
                "label": label}

        return myRequest( http_url, data, save_file)

