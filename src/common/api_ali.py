import requests
import json
import base64
from json import JSONDecoder
from utils.base import isNull,save,to_sha1_base64,get_current_date,to_md5_base64
from common.api import API

HTTP_URL = "https://dtplus-cn-shanghai.data.aliyuncs.com/"
AK_ID = 'LTAIohlfBnVzFI6J'
AK_SECRET = 'mvHMhzCUkSmgv1wWyWRl5uALyaScrH'

def getAuthorzation(http_url,body):
    options = {
        'url': http_url,
        'method': 'POST',
        'body': body,
        'headers': {
            'accept': 'application/json',
            'content-type': 'application/json',
            'date': get_current_date()
        },
        "content":body["content"]
    }
    bodymd5 = to_md5_base64(options['body'])

    urlPath = options['url']

    stringToSign = options['method'] + '\n' + options['headers']['accept'] + '\n' + bodymd5 + '\n' + options['headers'][
        'content-type'] + '\n' + options['headers']['date'] + '\n' + urlPath
    signature = to_sha1_base64(stringToSign, AK_SECRET)
    authHeader = 'Dataplus ' + AK_ID + ':' + signature.decode("utf-8")
    print(authHeader)
    return authHeader

def myRequest(http_url, data, filepath="", save_file=""):
    if filepath != "":
        img = open(filepath, 'rb')
        img = base64.b64encode(img.read())
        data["content"] = img
    headers = {"Authorization": getAuthorzation(http_url,data)}
    response = requests.post(http_url, data=data,headers=headers)
    print(response)
    try:
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        save(save_file, req_dict)
        return req_dict
    except:
        return {}

class Ali(API):
    def __init__(self):
        pass

    def detect(self,type,filepath, save_file=""):
        if type !=0 and type != 1:
            return
        if isNull(filepath):
            return
        http_url = HTTP_URL+"face/detect"
        data = {"type":type}
        if type ==0:
            data["image_url"] =filepath
            return myRequest(http_url, data, save_file)
        else:
            return myRequest(http_url, data, filepath, save_file)

    def attribute(self,  filepath,type=1, save_file=""):
        if type !=0 and type != 1:
            return
        if isNull(filepath):
            return
        http_url = HTTP_URL+"face/attribute"
        data = {"type":type}
        if type ==0:
            data["image_url"] =filepath
            return myRequest(http_url, data, save_file)
        else:
            return myRequest(http_url, data, filepath, save_file)

    def compare(self, type, file1, file2, save_file=""):
        if type !=0 and type != 1:
            return
        if isNull(file1) or isNull(file2):
            return
        http_url = HTTP_URL+"verify"
        data = {"type": type}

        if type == 0:
            data["image_url_1"] = file1
            data["image_url_2"] = file2
        else:
            # 二进制方式打开图片文件
            f1 = open(file1, 'rb')
            img1 = base64.b64encode(f1.read())
            data["content_1"] = img1
            f2 = open(file2, 'rb')
            img2 = base64.b64encode(f2.read())
            data["content_2"] = img2
        return myRequest(http_url, data, save_file)