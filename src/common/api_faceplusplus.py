import requests
import base64
from json import JSONDecoder
from utils.base import isNull,save
from common.api import API

HTTP_URL = "https://api-cn.faceplusplus.com/facepp/v3/"
API_KEY = "QHV8eEZ1oKvr9QWdzzHpAZYc3YN64c21"
API_SECRET = "S626Pb1ZRLI1nDTPoYsf_i6uThYBSQTR"

def myRequest( http_url, data, filepath="", save_file=""):
    data["api_key"] = API_KEY
    data["api_secret"] = API_SECRET
    if filepath != "":
        img = open(filepath, 'rb')
        img = base64.b64encode(img.read())
        data["image_base64"] = img
        response = requests.post(http_url, data=data)
    else:
        response = requests.post(http_url, data=data)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    save(save_file, req_dict)
    return req_dict

class FacePlusPlus(object):
    def __init__(self):
        pass

    def detect(self,filepath, return_landmark=0, return_attributes="none", save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"detect"

        data = {"return_landmark": return_landmark,
                "return_attributes": return_attributes}

        return myRequest(http_url, data, filepath, save_file)

    def compare(self,file1, file2, return_landmark=0,is_file=0, save_file=""):
        if isNull(file1) or isNull(file2):
            return
        http_url = HTTP_URL+"compare"

        data = {"return_landmark": return_landmark}
        if is_file == 0:
            img1 = open(file1, "rb")
            img1 = base64.b64encode(img1.read())
            img2 = open(file2, "rb")
            img2 = base64.b64encode(img2.read())
            data["image_base64_1"] = img1
            data["image_base64_2"] = img2
            return myRequest(http_url, data, save_file)
        else :
            data["face_token1"] = file1
            data["face_token2"] = file2
            return myRequest(http_url, data, save_file)

    def search(self,face_token, faceset_token, return_result_count=1, save_file=""):
        if isNull(face_token) or isNull(faceset_token):
            return
        http_url = HTTP_URL+"search"


        data = {"face_token": face_token,
                "faceset_token": faceset_token,
                "return_result_count": return_result_count}

        return myRequest( http_url, data, save_file)


class FaceSet(object):
    def __init__(self,display_name="", outer_id="", tags="", face_tokens="", user_data="", force_merge=0, save_file=""):
        http_url = HTTP_URL + "faceset/create"
        data = {"force_merge": force_merge}
        if display_name != "":
            data["display_name"] = display_name
        if outer_id != "":
            data["outer_id"] = outer_id
        if tags != "":
            data["tags"] = tags
        if face_tokens != "":
            data["face_tokens"] = face_tokens
        if user_data != "":
            data["user_data"] = user_data
        req_dict = myRequest( http_url, data, save_file)

        self.faceset_token = req_dict["faceset_token"]
    def __init__(self,faceset_token):
        self.faceset_token = faceset_token

    def addFace_faceSet(self, face_tokens, save_file=""):
        if isNull(face_tokens):
            return
        http_url = HTTP_URL+"faceset/addface"

        data = {"faceset_token": self.faceset_token,
                "face_tokens": face_tokens}

        return myRequest( http_url, data, save_file)

    def removeFace_faceSet(self, face_tokens, save_file=""):
        if isNull(face_tokens):
            return
        http_url = HTTP_URL+"faceset/removeface"

        data = {"faceset_token": self.faceset_token,
                "face_tokens": face_tokens}

        return myRequest( http_url, data, save_file)

    def update_faceSet(self, new_outer_id, save_file=""):
        if isNull(new_outer_id):
            return
        http_url = HTTP_URL+"faceset/update"

        data = {"faceset_token": self.faceset_token,
                "new_outer_id": new_outer_id}

        return myRequest( http_url, data, save_file)

    def getDetail_faceSet(self, start=1, save_file=""):
        http_url = HTTP_URL+"faceset/getdetail"

        data = {"faceset_token": self.faceset_token,
                "start": start}

        return myRequest( http_url, data, save_file)

    def delete_faceSet(self, check_empty=1, save_file=""):

        http_url = HTTP_URL+"faceset/delete"

        data = {"faceset_token": self.faceset_token,
                "check_empty": check_empty}

        return myRequest( http_url, data, save_file)

    def get_faceSet(self,tags="", start=1, save_file=""):
        http_url = HTTP_URL+"faceset/getfacesets"

        data = {"start": start}
        if tags != "":
            data["tags"] = tags
        return myRequest( http_url, data, save_file)


class Face(object):
    def __init__(self,face_token):
        self.face_token = face_token

    def analyze_face(self,return_landmark = 0,return_attributes="none", save_file=""):
        http_url = HTTP_URL+"face/analyze"

        data = {"face_token":self.face_token,
                "return_landmark": return_landmark,
                "return_attributes": return_attributes}

        return myRequest( http_url, data, save_file)


    def getDetail_face(self, save_file=""):
        http_url = HTTP_URL+"face/getdetail"

        data = {"face_token": self.face_token}

        return myRequest( http_url, data, save_file)

    def setUserID_face(self,user_id, save_file=""):
        http_url = HTTP_URL+"face/setuserid"

        data = {"face_token": self.face_token,
                "user_id": user_id}

        return myRequest( http_url, data, save_file)

