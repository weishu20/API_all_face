

# output_path = 'result/campare/faceplusplus_/confidence.data'
#
# file = open(output_path)
#
# result = file.read().split("\n")
# print(result)
#
# sum = 0.0
# total = 0
# for i in range(len(result)-1):
#     sum += float(result[i])
#     total += 1
# print(total)
# print(str(sum/total))
# import json
# body = {"type": 1, "content": 0}
#
# print(json.dumps({"name": "hello","type":0}, separators=(',', ':')))
#
# print(json.dumps(body, separators=(',', ':')))

# from common.api_tencent import Tencent
#
# tencent = Tencent()
# tencent.detect("/home/shushi/Pic/IMDB-WIKI/wiki_crop/17/10000217_1981-05-05_2009.jpg")

# from hashlib import sha1
# import hmac
# import base64
#
# my_sign = hmac.new(b'123456', b'123456', sha1).digest()
# my_sign = base64.b64encode(my_sign)
# print(my_sign)#b'dLVbarK45DisgQQ142njBHs5UdA='

# import cv2
# img2 = cv2.imread("/home/shushi/Pic/idealtest/idealtest/051/051-015.bmp")
# cv2.imwrite("/home/shushi/projects/3face/face_api/src/result/campare_diff/tencent/051/051-0151.bmp", img2)

# data = {"error":{"a":1,"b":2}}
# keys = data["error"].keys()
# list(keys)
# print()
# print(data["error"][list(keys)[0]])
