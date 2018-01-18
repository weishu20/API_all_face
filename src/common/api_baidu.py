import requests
import base64
from json import JSONDecoder
from utils.base import isNull,save
from common.api import API

HTTP_URL = "https://aip.baidubce.com/rest/2.0/face/v2/"
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
ACCESS_TOKEN = "24.d3c76b3b992fc7e5d35c51e761828092.2592000.1518171145.282335-10628712"

def myRequest(http_url, data, filepath="", save_file=""):
    headers = HEADERS
    if filepath != "":
        img = open(filepath, 'rb')
        img = base64.b64encode(img.read())
        data["image"] = img
        response = requests.post(http_url, data=data, headers=headers)
    else:
        response = requests.post(http_url, data=data, headers=headers)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict)
    save(save_file, req_dict)
    return req_dict


class Baidu(object):
    def __init__(self):
        pass

    def detect(self, filepath, max_face_num=1, face_fields="", save_file=""):
        if isNull(filepath):
            return
        http_url = HTTP_URL+"detect?access_token="+ACCESS_TOKEN
        data = {"max_face_num": max_face_num}
        if face_fields != "":
            data["face_fields"] = face_fields
        return myRequest(http_url, data, filepath, save_file)

    def compare(self,file1, file2, ext_fields="",image_liveness="",types="",save_file=""):
        if isNull(file1) or isNull(file2):
            return
        http_url = HTTP_URL+"match?access_token="+ACCESS_TOKEN

        # 二进制方式打开图片文件
        f1 = open(file1, 'rb')
        img1 = base64.b64encode(f1.read())
        f2 = open(file2, 'rb')
        img2 = base64.b64encode(f2.read())

        data = {"images": img1 + b',' + img2}
        if ext_fields != "":
            data["ext_fields"]=ext_fields
        if image_liveness != "":
            data["image_liveness"]=image_liveness
        if types != "":
            data["types"]=types

        return myRequest(http_url, data, save_file)

    def search(self,filepath, group_id, ext_fields="", user_top_num=1, save_file=""):
        if isNull(filepath) or isNull(group_id):
            return
        http_url = HTTP_URL+"identify?access_token="+ACCESS_TOKEN

        data = {"group_id": group_id,
                "user_top_num": user_top_num}
        if ext_fields != "":
            data["ext_fields"]=ext_fields

        return myRequest(http_url, data, filepath, save_file)

    def multi_search(self, filepath, group_id, ext_fields="",detect_top_num = 1, user_top_num=1, save_file=""):
        if isNull(filepath) or isNull(group_id):
            return
        http_url = HTTP_URL+"multi-identify?access_token="+ACCESS_TOKEN

        data = {"group_id": group_id,
                "user_top_num": user_top_num,
                "detect_top_num": detect_top_num}
        if ext_fields != "":
            data["ext_fields"]=ext_fields

        return myRequest(http_url, data, filepath, save_file)


    def verify(self,filepath, uid,group_id, ext_fields="", top_num=1, save_file=""):
        if isNull(uid) or isNull(group_id) or isNull(filepath):
            return
        http_url = HTTP_URL+"verify?access_token="+ACCESS_TOKEN

        data = {"uid": uid,
                "group_id": group_id,
                "top_num": top_num}
        if ext_fields != "":
            data["ext_fields"]=ext_fields

        return myRequest(http_url, data, filepath, save_file)

class User(object):
    def __init__(self, uid,user_info,group_id,filepath,action_type="append",save_file=""):
        if isNull(uid) or isNull(user_info)or isNull(group_id)or isNull(filepath):
            return
        http_url = HTTP_URL+"faceset/user/add?access_token="+ACCESS_TOKEN

        data = {"uid": uid,
                "user_info": user_info,
                "group_id": group_id,
                "action_type": action_type}
        ##可以是多张图片
        req_dict = myRequest(http_url, data, filepath, save_file)
        self.uid = uid

    def updateUser(self,filepath, user_info,group_id,action_type="", save_file=""):
        if isNull(user_info)or isNull(group_id)or isNull(filepath):
            return
        http_url = HTTP_URL+"faceset/user/update?access_token="+ACCESS_TOKEN

        data = {"uid": self.uid,
                "user_info": user_info,
                "group_id": group_id,
                "action_type": action_type}
        return myRequest(http_url, data, filepath, save_file)

    def deleteUser(self, group_id="", save_file=""):
        http_url = HTTP_URL+"faceset/user/delete?access_token="+ACCESS_TOKEN

        data = {"uid": self.uid}
        if group_id != "":
            data["group_id"] = group_id

        return myRequest(http_url, data, save_file)

    def getUser(self, group_id, save_file=""):
        http_url = HTTP_URL+"faceset/user/get?access_token="+ACCESS_TOKEN

        data = {"uid": self.uid}
        if group_id != "":
            data["group_id"] = group_id
        return myRequest(http_url, data, save_file)



class Group(object):
    def __init__(self,group_id):
        self.group_id = group_id

    def getlist_group(self,start=0,num=100, save_file=""):
        http_url = HTTP_URL + "faceset/group/getlist?access_token=" + ACCESS_TOKEN

        data = {"start": start,
                "num": num}

        return myRequest(http_url, data, save_file)

    def getUsers(self, start=0,num=100, save_file=""):
        http_url = HTTP_URL + "faceset/group/getusers?access_token=" + ACCESS_TOKEN

        data = {"group_id": self.group_id,
                "start": start,
                "num": num}

        return myRequest(http_url, data, save_file)

    def copyUser(self,uid,src_group_id, save_file=""):
        if isNull(uid) or isNull(src_group_id):
            return
        http_url = HTTP_URL + "faceset/group/adduser?access_token=" + ACCESS_TOKEN

        data = {"group_id": self.group_id,
                "uid": uid,
                "src_group_id": src_group_id}

        return myRequest(http_url, data, save_file)
    def deleteOneUser(self, uid, save_file=""):
        if isNull(uid):
            return
        http_url = HTTP_URL+"faceset/group/deleteuser?access_token="+ACCESS_TOKEN

        data = {"uid": uid,
                "group_id":self.group_id}

        return myRequest(http_url, data, save_file)