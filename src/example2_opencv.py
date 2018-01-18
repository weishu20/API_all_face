# -*- coding: utf-8 -*-
import urllib2
import urllib
import ssl
import time
import cv2
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "89W9C9NTm0Je9BBGZbro2fmnit41ajT7"
secret = "j0dCqm5hwKcNy1xhu0z1XIO1hFix4LzP"
filepath = r"../images/test_image.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)
img  = cv2.imread(filepath)
cv2.namedWindow('img1', cv2.WINDOW_NORMAL)
cv2.imshow('img1',img)
http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
    # req.add_header('Referer','http://remotserver.com/')
    context = ssl._create_unverified_context()
    resp = urllib2.urlopen(req, timeout=5, context=context)
    # get response
    qrcont = resp.read()
    print(qrcont)
    dict = eval(qrcont)
    faces = dict['faces']
    print(len(faces))
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
    cv2.namedWindow("img2", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("img2", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow("img2", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
except urllib2.HTTPError as e:
    print(e.read())