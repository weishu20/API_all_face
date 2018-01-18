import cv2
import datetime
import base64
import hmac
import hashlib
import json

def isNull(thing):
    if thing.strip()== '':
        print("input parameter is null!")
        return True
    return False

def isNull_list(thing):
    if thing == []:
        print("input parameter is []!")
        return True
    return False

def save(save_file,req_dict):
    if save_file == "":
        return
    with open(save_file, 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))

def get_current_date():
    date = datetime.datetime.strftime(datetime.datetime.utcnow(), "%a, %d %b %Y %H:%M:%S GMT")
    return date


def to_md5_base64(strBody):
    m = hashlib.md5()
    m.update(strBody)
    return hash.digest().encode('base64').strip()
    #return m.digest()

def to_sha1_base64(stringToSign, secret):
    hmacsha1 = hmac.new(secret.encode(), stringToSign.encode(), hashlib.sha1)
    return base64.b64encode(hmacsha1.digest())

def to_sha1_base64_tencent(stringToSign, secret):
    hmacsha1 = hmac.new(secret, stringToSign, hashlib.sha1)
    return base64.b64encode(hmacsha1.digest()+stringToSign)


def draw_face_rectangle(faces,img,filepath):
    for i in range(len(faces)):
        face_rectangle = faces[i]['face_rectangle']
        width = face_rectangle['width']
        top = face_rectangle['top']
        left = face_rectangle['left']
        height = face_rectangle['height']
        start = (left, top)
        end = (left + width, top + height)
        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)
    cv2.imwrite(filepath, img)

def draw_face_rectangle_microsoft(faces,img,filepath):
    for i in range(len(faces)):
        face_rectangle = faces[i]['faceRectangle']
        width = face_rectangle['width']
        top = face_rectangle['top']
        left = face_rectangle['left']
        height = face_rectangle['height']
        start = (left, top)
        end = (left + width, top + height)
        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)
    cv2.imwrite(filepath, img)

def draw_face_rectangle_baidu(faces,img,filepath):
    for i in range(len(faces)):
        face_rectangle = faces[i]['location']
        width = face_rectangle['width']
        top = face_rectangle['top']
        left = face_rectangle['left']
        height = face_rectangle['height']
        start = (left, top)
        end = (left + width, top + height)
        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)
    cv2.imwrite(filepath, img)

def draw_face_rectangle_ali(face_rect,img,filepath):
    num = len(face_rect)
    for i in range(num/4):
        width = face_rect[i*4]
        top = face_rect[i*4+1]
        left = face_rect[i*4+2]
        height = face_rect[i*4+3]
        start = (left, top)
        end = (left + width, top + height)
        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)
    cv2.imwrite(filepath, img)

def draw_face_rectangle_tencent(faces,img,filepath):
    for i in range(len(faces)):
        x = faces[i]['x']
        y = faces[i]['y']
        width = faces[i]['width']
        height = faces[i]['height']
        start = (x, y)
        end = (int(x + width),int( y + height))
        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)
    cv2.imwrite(filepath, img)